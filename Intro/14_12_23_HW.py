import math

def apply_strategies(strategies, data):
    return [strategy(data) for strategy in strategies]

def find_min_strategy(strategies, data):
    results    = apply_strategies(strategies, data)
    min_result = min(results)
    return strategies[results.index(min_result)], min_result

strategies = [
    lambda data: sum(data) / len(data),  # Арифметичне середнє
    lambda data: math.prod(data) ** (1/len(data)),  # Геометричне середнє
    lambda data: len(data) / sum(1 / x for x in data)  # Гармонічне середнє
]

data = [1, 2, 3, 4, 5]  # Набір даних

min_strategy, min_value = find_min_strategy(strategies, data)
print(f"Minimum value: {min_value}")
