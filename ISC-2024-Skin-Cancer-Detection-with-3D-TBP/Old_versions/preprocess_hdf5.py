import h5py
import numpy as np
from PIL import Image
import os
import argparse

def preprocess_hdf5(input_file, output_dir):
    with h5py.File(input_file, "r") as hf:
        images = hf["images"]
        for i, img in enumerate(images):
            img = np.array(img)
            img = Image.fromarray(img)
            img = img.convert("RGB")
            img.save(os.path.join(output_dir, f"{i}.jpg"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, required=True, help='Path to the HDF5 file')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the images')
    args = parser.parse_args()

    preprocess_hdf5(args.input_file, args.output_dir)
    print(f"Preprocessed images saved to {args.output_dir}")
