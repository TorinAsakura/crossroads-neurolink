from simulation.traffic_simulation import TrafficSimulation


def evaluate_traffic_system(road_ids, steps):
    sim = TrafficSimulation(road_ids)
    total_density = 0.0

    for _ in range(steps):
        traffic_state, _ = sim.step()
        total_density += sum(road_info['traffic_density'] for road_info in traffic_state.values())

    average_density = total_density / (steps * len(road_ids))
    return average_density


def compute_average_time(traffic_simulation):
    total_time = 0
    total_cars = 0
    for car in traffic_simulation.cars:
        total_time += car.time
        total_cars += 1
    return total_time / total_cars if total_cars != 0 else 0
