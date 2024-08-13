#inspect_hdf5_file.py
#Run the script to see the structure of your HDF5 files. This will list all the objects (datasets/groups) within the file.

# import h5py

# def inspect_hdf5_file(file_path):
#     with h5py.File(file_path, 'r') as f:
#         print("HDF5 file structure:")
#         f.visit(print)

# # Inspect the train HDF5 file
# inspect_hdf5_file('data/train-image.hdf5')

# # Inspect the test HDF5 file
# inspect_hdf5_file('data/test-image.hdf5')


# import h5py

# with h5py.File('data/train-image.hdf5', 'r') as f:
#     for key in f.keys():
#         print(f"Image ID: {key}, Shape: {f[key].shape}, Type: {f[key].dtype}")



import numpy as np
from PIL import Image
import io
import h5py

# Load a sample image from the HDF5 file
with h5py.File('data/train-image.hdf5', 'r') as f:
    sample_key = list(f.keys())[0]
    image_data = f[sample_key][()]
    if isinstance(image_data, np.bytes_):
        image_data = np.frombuffer(image_data, dtype=np.uint8)
        image = Image.open(io.BytesIO(image_data))
        image.show()  # Display the image to verify it opens correctly

