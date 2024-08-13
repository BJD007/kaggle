import torch.nn as nn
import torchvision.models as models

class SkinCancerModel(nn.Module):
    def __init__(self):
        super(SkinCancerModel, self).__init__()
        self.cnn = models.resnet50(pretrained=True)
        self.cnn.fc = nn.Identity()  # Remove final FC layer
        
        self.metadata_fc = nn.Sequential(
            nn.Linear(25, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
        )
        
        self.fc = nn.Sequential(
            nn.Linear(2048 + 64, 512),
            nn.ReLU(),
            nn.Linear(512, 1)
        )
    
    def forward(self, x, metadata):
        cnn_out = self.cnn(x)
        metadata_out = self.metadata_fc(metadata)
        combined = torch.cat((cnn_out, metadata_out), dim=1)
        out = self.fc(combined)
        return out