# import h5py

# hdf5_file_path = '/home/bhaskarhertzwell/Documents/Bhaskar_GITHUB/kaggle/ISIC-2024 - Skin-Cancer-Detection-with-3D-TBP/data/train-image.hdf5'
# with h5py.File(hdf5_file_path, 'r') as f:
#     print(list(f.keys()))  # List all datasets
#     for dataset in f.keys():
#         print(f[dataset].shape)  # Print the shape of each dataset


import h5py

hdf5_file_path = '/home/bhaskarhertzwell/Documents/Bhaskar_GITHUB/kaggle/ISIC-2024 - Skin-Cancer-Detection-with-3D-TBP/data/train-image.hdf5'

with h5py.File(hdf5_file_path, 'r') as f:
    print("Datasets in the file:")
    for key in f.keys():
        print(f"Dataset: {key}")
        data = f[key]
        print(f"Shape: {data.shape}")
        print(f"Dtype: {data.dtype}")
