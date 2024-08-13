#datasets.py
# # This script contains the dataset class and data loading functionality.

import h5py
import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import io

class SkinCancerDataset(Dataset):
    def __init__(self, metadata_file, hdf5_file, transform=None):
        self.metadata = pd.read_csv(metadata_file)
        self.hdf5_file = h5py.File(hdf5_file, 'r')
        self.transform = transform

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        image_id = self.metadata.iloc[idx]['isic_id']
        label = self.metadata.iloc[idx]['target']

        if image_id in self.hdf5_file:
            image = self.hdf5_file[image_id][()]

            if isinstance(image, np.bytes_):
                # Decode the bytes into an image
                image = np.frombuffer(image, dtype=np.uint8)
                image = Image.open(io.BytesIO(image))
            elif isinstance(image, np.ndarray):
                # Convert numpy array to PIL Image
                image = Image.fromarray(image)
            else:
                raise TypeError(f"Unexpected data format for image ID {image_id}. Expected numpy array or bytes, got {type(image)}.")

            image = image.convert("RGB")  # Convert to RGB if necessary

            if self.transform:
                image = self.transform(image)

            return image, torch.tensor(label, dtype=torch.float32)
        else:
            raise KeyError(f"Image ID {image_id} not found in HDF5 file.")

    def __del__(self):
        self.hdf5_file.close()

def get_dataloader(metadata_file, hdf5_file, batch_size, mean, std, augment=False):
    if augment:
        transform = transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
        ])
    else:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
        ])
    
    dataset = SkinCancerDataset(metadata_file, hdf5_file, transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    
    return dataloader

