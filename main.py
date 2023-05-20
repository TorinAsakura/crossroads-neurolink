from simulation.traffic_simulation import TrafficSimulation
from evaluation.evaluate import compute_average_time, evaluate_traffic_system
from model.traffic_net import TrafficNet
from model.train import train
import torch


def main():
    road_ids = ['A', 'B', 'C', 'D', 'E']
    steps = 1000

    average_density = evaluate_traffic_system(road_ids, steps)
    print(f"Средняя плотность трафика за {steps} шагов: {average_density}")


if __name__ == "__main__":
    # Создаем симуляцию
    traffic_simulation = TrafficSimulation()

    # Случайное состояние светофоров
    traffic_simulation.random_traffic_lights()
    average_time_random = compute_average_time(traffic_simulation)

    # Состояние светофоров, определяемое логическими условиями
    traffic_simulation.logic_based_traffic_lights()
    average_time_logic = compute_average_time(traffic_simulation)

    # Обучение и использование нейросети для управления светофорами
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = TrafficNet().to(device)
    train(model, traffic_simulation.dataloader, epochs=100, device=device)
    traffic_simulation.neural_network_based_traffic_lights(model, device)
    average_time_neural = compute_average_time(traffic_simulation)

    print("Среднее время прохождения маршрутов при случайном состоянии светофоров:", average_time_random)
    print("Среднее время прохождения маршрутов при состоянии светофоров, определяемом логическими условиями:", average_time_logic)
    print("Среднее время прохождения маршрутов при состоянии светофоров, контролируемом нейросетью:", average_time_neural)
