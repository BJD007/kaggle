import torch
from torchvision import models
from dataset import get_dataloader
from utils import train_model

def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Mean and std for normalization
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    # Set parameters directly in the script
    model_name = 'EfficientNet-B0'
    num_epochs = 1
    batch_size = 2
    save_path = 'models/model.pth'
    train_metadata_file = 'data/train-metadata.csv'
    train_hdf5_file = 'data/train-image.hdf5'
    test_metadata_file = 'data/test-metadata.csv'
    test_hdf5_file = 'data/test-image.hdf5'

    # Load data
    train_loader = get_dataloader(
        metadata_file=train_metadata_file,
        hdf5_file=train_hdf5_file,
        batch_size=batch_size,
        mean=mean,
        std=std,
        augment=True
    )
    
    test_loader = get_dataloader(
        metadata_file=test_metadata_file,
        hdf5_file=test_hdf5_file,
        batch_size=batch_size,
        mean=mean,
        std=std,
        augment=False
    )

    # Load model
    model = models.efficientnet_v2_m(weights='DEFAULT')
    model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, 1)  # Adjust the output layer for binary classification

    # Train model
    train_model(model, train_loader, test_loader, num_epochs=num_epochs, learning_rate=0.001, save_path=save_path, device=device)

if __name__ == "__main__":
    main()
