from typing import Final, Iterable
import time

from collections import Counter


data_array: Final[list[int]] = [34, 81, 6, 15, 33, 11, 86, 39, 18, 90]
centers_count: Final[int] = 3


def get_centers(data: Iterable[int], centers_cnt: int) -> list[int]:
    """ Получение наиболее частых значений из массива данных

    Args:
        data: Массив данных
        centers_cnt: Количество групп

    Returns:
        Список наиболее частых значений
    """

    counter = Counter(data)
    most_common = counter.most_common(centers_cnt)

    return [point for point, count in most_common]


def group_data_by_centers(
    data: Iterable[int],
    centers: list[int],
) -> list[int]:
    """ Группировка массива данных

    Args:
        data: Массив данных
        centers: Список наиболее частых значений

    Returns:
        Сгруппированный список данных
    """

    group_dict = {}
    for i, center in enumerate(centers):
        group_dict[center] = i + 1

    groups = []
    for i in data:
        closest_center = min(centers, key=lambda x: abs(x - i))
        groups.append(group_dict[closest_center])

    return groups


def main(centers_cnt: int) -> None:
    """ Запуск процесса

    Args:
        centers_cnt: Количество групп
    """

    start = time.perf_counter()

    centers = get_centers(data_array, centers_cnt)
    result = group_data_by_centers(data_array, centers)

    print(time.perf_counter() - start)
    print([i for i in zip(data_array, result)])


if __name__ == '__main__':
    main(centers_count)
