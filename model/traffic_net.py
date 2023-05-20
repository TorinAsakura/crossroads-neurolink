import torch
from torch import nn

class TrafficNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(TrafficNet, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.sigmoid(self.layer2(x))
        return x
