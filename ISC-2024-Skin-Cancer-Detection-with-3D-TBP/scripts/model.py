#Model.py
#This script defines the model architecture.

import torch
import torch.nn as nn
import torchvision.models as models

class SkinCancerModel(nn.Module):
    def __init__(self, model_name='efficientnet_v2_m', pretrained=True):
        super(SkinCancerModel, self).__init__()
        
        # Load a pre-trained EfficientNetV2 model
        if model_name == 'efficientnet_v2_m':
            self.backbone = models.efficientnet_v2_m(weights=models.EfficientNet_V2_M_Weights.IMAGENET1K_V1 if pretrained else None)
        elif model_name == 'efficientnet_v2_s':
            self.backbone = models.efficientnet_v2_s(weights=models.EfficientNet_V2_S_Weights.IMAGENET1K_V1 if pretrained else None)
        else:
            raise ValueError(f"Model {model_name} is not supported")
        
        # Modify the classifier to fit our binary classification task
        num_features = self.backbone.classifier[1].in_features
        self.backbone.classifier = nn.Sequential(
            nn.Linear(num_features, 1)
        )
    
    def forward(self, x):
        return self.backbone(x)
