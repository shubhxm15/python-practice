from typing import Dict, Union, Tuple       # advance typing methods

score: dict[str, int] = {"Rahul": 30, "Gogi": 20}

choice: Union[str, int] = "GOGI420", 1234

mix: Tuple[str, int] = {"Tappu", 88}

a: int = 5
b: int = 10

def sum(a: int, b: int) -> int:    # defining its return type will also be an integer
    return a + b

print(sum(a, b))