"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "730569341"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float


    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y


    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    

    def distance(self, other: Point) -> Point: 
        """Return the distance between two Point objects."""
        distance: float = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE


    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        self.location = self.location.add(self.direction)
        if self.sickness == constants.INFECTED: 
            self.sickness +=1 
        if self.sickness > constants.RECOVERY_PERIOD:
            self.sickness = Cell.is_immune


    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.sickness == Cell.is_vulnerable: 
            return "gray"
        if self.sickness == Cell.is_infected:
            return "red"
        if self.sickness == Cell.is_immune:
            return "green"


    def contract_disease(self) -> None:
        self.sickness = constants.INFECTED 
    

    def is_vulnerable(self) -> bool:
        """Indicate if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False


    def is_infected(self) -> bool:
        """Indicate if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False


    def contact_with(self, cell: Cell, other_cell: Cell) -> None:
        """When two Cell objects do not make contact."""
        if cell or other_cell == Cell.is_infected:
            other_cell == constants.INFECTED
    

    def immunize(self) -> None:
        self.sickness = constants.IMMUNE 
    

    def is_immune(self) -> bool:
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
    

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    num_infected_cells: int = 0
    start_immune_cells: int = 0 


    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        
        if Model.num_infected_cells >= cells: 
            return ValueError('Some cells must begin infected.')
    

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)


    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)


    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)


    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0


##########
    # def is_complete(self) -> bool:
    #     """Method to indicate when the simulation is complete."""
    #     #if all Cell objects in the population are either vulnerable or immune
    #         return True 
    #     #else when any of the Cell objects are infected
    #         return False
    
############
    def check_contacts(self) -> None:
        """Method to indicate when any two cell values come in contact with one another."""
    # compare the distance between every two cell object location attributes in the population
    #if any distance between two cells is less than constant CELL_RADIUS
        # call the cell.contact_with on 1 of the 2 cell objects, refer to other as an argument 



    