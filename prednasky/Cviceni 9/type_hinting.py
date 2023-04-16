# Needed imports for type hints
from typing import List, Dict, Optional, Any

###########################################
#python -m mypy --strict .\type_hinting.py#
###########################################

# Int returning an int
def square(x: int) -> int:
   return x * x


# List of floats returning an optional float
def calculate_average(numbers: List[float]) -> Optional[float]:
   if not numbers:
       return None
   return sum(numbers) / len(numbers)


# Merge two dictionaries with any key and value type returning a dictionary with any key and value type
def merge_dicts(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[Any, Any]:
   return {**a, **b}


# List of dictionaries with a str key and optional float value returning list of  optional floats (None or float)
def process_data(data: List[Dict[str,Optional[float]]]) -> List[Optional[float|None]]:
   results = []
   for d in data:
       if d.get("value"):
           results.append(d["value"])
   return results
