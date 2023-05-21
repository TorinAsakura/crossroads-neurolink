import random
from traffic_lights import manage_traffic_lights


class TrafficSimulation:
    def __init__(self, road_ids, min_density=0.0, max_density=1.0):
        self.traffic_state = {road_id: {'traffic_density': random.uniform(min_density, max_density)}
                              for road_id in road_ids}
        self.traffic_lights = manage_traffic_lights(self.traffic_state)

    def step(self):
        for road_id, road_info in self.traffic_state.items():
            if self.traffic_lights[road_id]:  # Если светофор зеленый
                # Уменьшаем плотность трафика, представляя, что машины покидают участок
                road_info['traffic_density'] -= random.uniform(0.0, 0.1)
            else:  # Если светофор красный
                # Увеличиваем плотность трафика, представляя, что машины прибывают на участок
                road_info['traffic_density'] += random.uniform(0.0, 0.1)

            # Обеспечиваем, чтобы плотность трафика оставалась в пределах [0, 1]
            road_info['traffic_density'] = min(max(road_info['traffic_density'], 0.0), 1.0)

        # Обновляем состояние светофоров на основе нового состояния трафика
        self.traffic_lights = manage_traffic_lights(self.traffic_state)

        return self.traffic_state, self.traffic_lights
