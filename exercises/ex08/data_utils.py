"""Dictionary related utility functions."""

__author__ = "730569341"

# Define your functions below

# Part 0
from csv import DictReader
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(data_rows: list[dict[str, str]], column: str) -> list[str]: 
    """Produce a list of string of column values."""
    result: list[str] = []
    for i in range(len(data_rows)): 
        if column[i]:
            result.append(data_rows[i])
    return result
 

def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a table as a list of rows into a dictionary of columns."""
    result: dict[str, list[str]] = []

    first_row: dict[str, str] = data_rows[0]
    for column in data_rows:
        result[column] = column_values(data_rows, column)
    return result


# Part 1 
def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column table with only the rows of data for each column."""
    result: dict[str, list[str]] = []
    if rows >= len(table):
        rows = len(table)
    for column in table:
        a_list: list[str] = []
        for i in range(rows):
            a_list.append(table[column][i])
        result[column] = a_list
    return result


def select(data_cols: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]: 
    """Produce a new column table with a subset of original."""
    result: dict[str, list[str]] = []
    for columns in data_cols:
        result[columns] = data_cols.values()  
    return result


def concat(data_cols_head: dict[str,list[str]], additional_table: dict[str,list[str]]) -> dict[str,list[str]]:
    """Produce a new column table with two column tables combined."""
    result: dict[str,list[str]] = []
    for key in data_cols_head:
        result[key] = data_cols_head[key]
    for key in additional_table:
        if key in result:
            result[key] += data_cols_head[key]
        else:
            result[key] += data_cols_head[key]
    return result


# Part 2 
def count(a_list: list[str] -> dict[str, int]):
    """Count the number of times a value appears in an input list."""
    result: dict[str, int] = []

    for item in range(len(a_list)):
        if a_list[item] not in result:
            result[a_list[item]] = 1 
        else:
            result[a_list[item]] += 1 
    return result