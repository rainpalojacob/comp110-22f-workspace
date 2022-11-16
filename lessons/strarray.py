"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    
    def __init__ (self, items: list[str]): 
        self.items = items

    def __repr__(self) -> str:
        return f"StrArrary({self.items})"
    

    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            # Your job (NEXT QUIZ ITEM):
            # Loop through every item in self's items list
            for item in self.items:
                # Concatenate the rhs parameter
                # Append the concatenated string to results' items attirbute
                result.items.append(item + rhs)
            else:
                assert len(self.items) == len(rhs.items)
                # otherwise, loop through each index of self's items
                for i in range(len(self.items)):
                # concatenate the corresponding value of rhs's items at the same index
                # append the resulting string to result's item list
                    result.items.append(self.items[i] + rhs.items[i])
            return result

a: StrArray = StrArray(["Armandi", "Pete", "Leaky"])
b: StrArray = StrArray({"Bacot", "Nance", "Black"})
print(a)
print(a + "!")
print(a + "" + b)
    
