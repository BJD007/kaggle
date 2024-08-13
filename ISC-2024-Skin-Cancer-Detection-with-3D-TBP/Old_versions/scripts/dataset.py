import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torch
from torchvision import transforms
import h5py
import io

class SkinCancerDataset(Dataset):
    def __init__(self, metadata_file, hdf5_file):
        self.metadata = pd.read_csv(metadata_file, low_memory=False)
        self.hdf5_file = hdf5_file
        self.hdf5_data = h5py.File(hdf5_file, 'r')
        # Define any necessary transformations
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Adjust size as needed
            transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        # Get the image ID and corresponding file path
        isic_id = self.metadata.iloc[idx]['isic_id']
        image_data = self.hdf5_data[isic_id][()]
        
        # Convert binary data to image
        image_bytes = io.BytesIO(image_data)
        image = Image.open(image_bytes).convert('RGB')

        if self.transform:
            image = self.transform(image)
        
        # Extract metadata and target
        metadata = self.metadata.iloc[idx, 2:-1].values.astype(np.float32)  # Adjust based on column indices
        target = self.metadata.iloc[idx]['target']
        
        return image, metadata, target

    def collate_fn(self, batch):
        images, metadata, targets = zip(*batch)
        images = torch.stack(images)
        metadata = torch.tensor(metadata, dtype=torch.float32)
        targets = torch.tensor(targets, dtype=torch.float32)
        return images, metadata, targets

def get_dataloader(metadata_file, hdf5_file, batch_size):
    dataset = SkinCancerDataset(metadata_file, hdf5_file)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=dataset.collate_fn)
    return dataloader
