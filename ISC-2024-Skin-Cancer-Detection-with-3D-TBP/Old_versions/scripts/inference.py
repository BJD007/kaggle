import torch
import pandas as pd
from scripts.model import SkinCancerModel
from scripts.dataset import get_dataloader
from scripts.utils import load_model, evaluate_model

# Load model
model = SkinCancerModel().to(device)
model = load_model(model, 'models/model.pth')

# Prepare test data loader
test_loader = get_dataloader('data/test-metadata.csv', 'data/test-image.hdf5', batch_size=1)

# Generate predictions
predictions = evaluate_model(model, test_loader)

# Prepare submission file
submission_df = pd.DataFrame({
    'isic_id': test_loader.dataset.metadata[:, 0],
    'target': predictions[:, 0]
})

submission_df.to_csv('submission.csv', index=False)