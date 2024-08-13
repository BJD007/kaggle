python3 scripts/train.py \
    --model_name EfficientNet-B0 \
    --num_epochs 1 \
    --batch_size 2 \
    --save_path models/model.pth \
    --train_metadata_file data/train-metadata.csv \
    --train_hdf5_file data/train-image.hdf5 \
    --test_metadata_file data/test-metadata.csv \
    --test_hdf5_file data/test-image.hdf5
    
    
    
