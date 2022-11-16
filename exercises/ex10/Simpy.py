"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730569341"


class Simpy:
    values: list[float]


    def __int__ (self, values: list[float]):
        self.values = values
    

    def __repr__(self) -> str:
        return f"Simpy({self.values})"

    
    def fill(self, num: float, instance: int) -> None: 
        """Mutates: repeat values specific amount of times."""
        result: Simpy = Simpy([])
        
        if isinstance(num, float):
            for value in self.values:
                result.values.append(num * instance[value])
        return result
            
    
        # TODO part 3
        def arrange(self, start: float, stop: float, step: Optional[float] = 1.0): 
            """Fill in values based on a range of values."""
            result: Simpy = Simpy([])
        
            assert step != 0.0
    
            for value in range(start, stop): 
                if start < stop:
                    result.value.append(step += ) 
            return result
        
        def sum(self) -> float:
            """Sum up all items with given values."""
            result: Simpy = Simpy([])
            result.value.append(sum(len(self.values)))
            return result

        
        def __add__ (self, rhs: Union[float, Simpy]) -> Simpy:
            """Overload summation of all items with given values."""
            return Simpy(self.values + rhs.values)


        def __pow__ (self, rhs: Union[float, Simpy]) -> Simpy:
            """Overload the multiplication operator for Simpy * float."""
            return Simpy(self.values * rhs.values)

        
        # Check for understanding 1


      
        def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
            """Overload of equality operator for Simpy and float."""
            if isinstance(rhs, Union[float, Simpy]):
                if rhs.values == self.values:
                    return True
            return False

 
        def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
            """Overload of greater than operator for Simpy and float."""
            if isinstance(rhs, Union[float, Simpy]):
                if rhs.values > self.values:
                    return True
            return False
        
         
        def __getitem__(self, rhs: int) -> float: 
            """Overload of subscription operator."""
            if rhs == int: 
                return self.values[rhs]
            else: 
                return TypeError


        # TODO part 10 
        def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
            """Select indvidual items based on a filter with a mask."""
        

    
        # Check for understanding 2


