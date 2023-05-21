from evaluation.evaluate import evaluate_traffic_system


def main():
    road_ids = ['A', 'B', 'C', 'D', 'E']
    steps = 1000

    average_density = evaluate_traffic_system(road_ids, steps)
    print(f"Средняя плотность трафика за {steps} шагов: {average_density}")


if __name__ == "__main__":
    main()
