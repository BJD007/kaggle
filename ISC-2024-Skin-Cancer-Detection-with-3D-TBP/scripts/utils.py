#utils.py
import torch
import torch.optim as optim
import torch.nn as nn
from tqdm import tqdm
from torch.cuda.amp import GradScaler, autocast

def train_model(model, train_loader, test_loader, num_epochs, learning_rate, save_path, device, accumulation_steps=4):
    model.to(device)
    
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scaler = GradScaler()  # Initialize the GradScaler for mixed precision
    
    best_val_loss = float('inf')
    
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        
        for step, (images, targets) in enumerate(tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs}", leave=False)):
            images, targets = images.to(device), targets.to(device)
            
            with autocast():  # Enable mixed precision
                outputs = model(images)
                loss = criterion(outputs, targets.unsqueeze(1))
                loss = loss / accumulation_steps  # Normalize the loss
            
            scaler.scale(loss).backward()  # Scale the gradients
            
            if (step + 1) % accumulation_steps == 0:
                scaler.step(optimizer)  # Update the weights
                scaler.update()  # Update the scaler
                optimizer.zero_grad()  # Zero gradients
            
            running_loss += loss.item() * images.size(0)
        
        # Clean up GPU memory
        torch.cuda.empty_cache()

        epoch_loss = running_loss / len(train_loader.dataset)
        
        val_loss = validate_model(model, test_loader, criterion, device)
        
        print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {epoch_loss:.4f} - Val Loss: {val_loss:.4f}")
        
        # Save model if validation loss improves
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            save_model(model, save_path)

def validate_model(model, test_loader, criterion, device):
    model.eval()
    running_loss = 0.0
    
    with torch.no_grad():
        for images, targets in test_loader:
            images, targets = images.to(device), targets.to(device)
            
            with autocast():  # Enable mixed precision
                outputs = model(images)
                loss = criterion(outputs, targets.unsqueeze(1))
            
            running_loss += loss.item() * images.size(0)
    
    val_loss = running_loss / len(test_loader.dataset)
    return val_loss

def save_model(model, save_path):
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")
