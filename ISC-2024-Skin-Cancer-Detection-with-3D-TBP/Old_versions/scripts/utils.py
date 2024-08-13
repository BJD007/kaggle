import torch
import numpy as np

def train_model(model, dataloader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for images, metadata, targets in dataloader:
            images, metadata, targets = images.to(device), metadata.to(device), targets.to(device)
            
            optimizer.zero_grad()
            outputs = model(images, metadata).squeeze()
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * images.size(0)
        
        epoch_loss = running_loss / len(dataloader.dataset)
        print(f'Epoch {epoch}/{num_epochs - 1}, Loss: {epoch_loss:.4f}')

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(model, path):
    model.load_state_dict(torch.load(path))
    return model

def evaluate_model(model, dataloader):
    model.eval()
    predictions = []
    with torch.no_grad():
        for images, metadata in dataloader:
            images, metadata = images.to(device), metadata.to(device)
            outputs = model(images, metadata)
            preds = torch.sigmoid(outputs).cpu().numpy()
            predictions.extend(preds)
    return np.array(predictions)