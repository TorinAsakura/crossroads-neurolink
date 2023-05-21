import random


def manage_traffic_lights(traffic_state):
    """Функция, управляющая состоянием светофоров.

    Args:
        traffic_state (dict): Словарь, в котором ключи - идентификаторы дорог,
        а значения - словари с информацией о состоянии дороги.

    Returns:
        traffic_lights (dict): Словарь, в котором ключи - идентификаторы светофоров,
        а значения - состояния светофоров.
    """

    # Начальное состояние светофоров (рандом)
    traffic_lights = {road_id: bool(random.getrandbits(1)) for road_id in traffic_state.keys()}

    # Используем правила управления светофорами исходя из состояния дорог
    for road_id, road_info in traffic_state.items():
        if road_info['traffic_density'] > 0.7:
            traffic_lights[road_id] = True
        elif road_info['traffic_density'] < 0.3:
            traffic_lights[road_id] = False
        else:
            # Если плотность трафика в диапазоне от 0.3 до 0.7 - не меняем состояние
            pass

    return traffic_lights
