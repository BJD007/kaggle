import torch
import torch.optim as optim
import torch.nn as nn
from scripts.model import SkinCancerModel
from scripts.dataset import get_dataloader
from scripts.utils import train_model, save_model

# Define device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
batch_size = 32
num_epochs = 20
learning_rate = 0.001

# Prepare data loaders
metadata_file = '/home/bhaskarhertzwell/Documents/Bhaskar_GITHUB/kaggle/ISIC-2024 - Skin-Cancer-Detection-with-3D-TBP/data/train-metadata.csv'
hdf5_file = '/home/bhaskarhertzwell/Documents/Bhaskar_GITHUB/kaggle/ISIC-2024 - Skin-Cancer-Detection-with-3D-TBP/data/train-image.hdf5'
train_loader = get_dataloader(metadata_file, hdf5_file, batch_size)

# Initialize model, loss function, optimizer
model = SkinCancerModel().to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
train_model(model, train_loader, criterion, optimizer, num_epochs)

# Save the model
save_model(model, '/home/bhaskarhertzwell/Documents/Bhaskar_GITHUB/kaggle/ISIC-2024 - Skin-Cancer-Detection-with-3D-TBP/models/model.pth')
