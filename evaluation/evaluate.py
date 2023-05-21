from simulation.traffic_simulation import TrafficSimulation


def evaluate_traffic_system(road_ids, steps):
    sim = TrafficSimulation(road_ids)
    total_density = 0.0

    for _ in range(steps):
        traffic_state, _ = sim.step()
        total_density += sum(road_info['traffic_density'] for road_info in traffic_state.values())

    average_density = total_density / (steps * len(road_ids))
    return average_density
