#inference.py

import pandas as pd
import torch
from torchvision import transforms, models
from torch.utils.data import DataLoader
from dataset import SkinCancerDataset
import argparse
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def load_model(model_path, device):
    model = models.efficientnet_v2_m(weights=None)
    model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, 1)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model

def predict(model, data_loader, device):
    all_probs = []
    all_targets = []
    model.eval()
    with torch.no_grad():
        for images, targets in data_loader:
            images = images.to(device)
            targets = targets.to(device)
            output = model(images)
            probs = torch.sigmoid(output).cpu().numpy().flatten()
            all_probs.extend(probs)
            all_targets.extend(targets.cpu().numpy().flatten())
    return all_probs, all_targets

def calculate_metrics(probs, targets):
    preds = (np.array(probs) > 0.5).astype(int)  # Convert probabilities to binary predictions
    accuracy = accuracy_score(targets, preds)
    precision = precision_score(targets, preds)
    recall = recall_score(targets, preds)
    f1 = f1_score(targets, preds)
    auc = roc_auc_score(targets, probs)
    
    return accuracy, precision, recall, f1, auc

def main(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load test metadata
    df_meta = pd.read_csv(args.metadata_file)

    test_trans = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Create dataset and dataloader
    test_dataset = SkinCancerDataset(
        metadata_file=args.metadata_file,
        hdf5_file=args.hdf5_file,
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
        transform=test_trans
    )
    test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)  # Adjust batch_size based on GPU memory

    model = load_model(args.model_path, device)
    probs, targets = predict(model, test_loader, device)

    # Calculate metrics
    accuracy, precision, recall, f1, auc = calculate_metrics(probs, targets)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC AUC Score: {auc:.4f}")

    df_meta["target"] = probs
    df_meta[["isic_id", "target"]].to_csv(args.submission_file, index=False)
    print(f"Submission file saved to {args.submission_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata_file", type=str, required=True, help="Path to test metadata CSV file")
    parser.add_argument("--hdf5_file", type=str, required=True, help="Path to test HDF5 file containing images")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the trained model")
    parser.add_argument("--submission_file", type=str, required=True, help="Path to save the submission CSV file")
    args = parser.parse_args()
    
    main(args)
