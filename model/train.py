import torch
from torch import nn, optim
from traffic_net import TrafficNet


def train(model, dataloader, epochs, device):
    # Определение функции потерь (loss function) и оптимизатора
    criterion = nn.BCELoss()  # Binary Cross-Entropy Loss подходит для бинарной классификации
    optimizer = optim.Adam(model.parameters())

    model = model.to(device)

    for epoch in range(epochs):
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()  # Обнуляем градиенты перед каждым шагом обучения

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()  # Вычисляем градиенты
            optimizer.step()  # Обновляем параметры модели

        print(f'Epoch {epoch+1}/{epochs}.. '
              f'Train loss: {loss.item():.3f}.. ')

    print('Training complete.')
