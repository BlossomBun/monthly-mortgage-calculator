# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:12:55 2024

@author: natur
"""

import numpy as np

def input_array():
    default_ranges = {
        "condo_cost": (250000, 400000, 10000, "$"),
        "downpayment": (30000, 80000, 10000, "$"),
        "interest_rate": (6.25, 7.5, 0.25, "%"),
        "loan_term": (30, 30, 10, " years"),
        "property_tax_rate": (1.0, 1.0, 0.1, "%"),
        "pmi_rate": (0.5, 1.5, 0.5, "%"),
    }

    # Get user inputs
    input_ranges = get_input_ranges(default_ranges)


    # Generate input arrays
    input_arrays = {}
    for key, (min_val, max_val, step, unit) in input_ranges.items():
        if unit == "%":
            min_val /= 100
            max_val /= 100
            step /= 100
        input_arrays[key] = np.arange(min_val, max_val + step, step)

    # Print the final input ranges
    print("\nThe program will use the following inputs:")
    print_range(input_ranges)

    return input_arrays


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_range(ranges):
    for key, (min_val, max_val, step, unit) in ranges.items():
        if unit == "$":
            print(f"{key.replace('_',' ').upper()}: ",
                   f"{unit}{min_val} - {unit}{max_val},",
                   f" in increments of {unit}{step}")
        else:
            print(f"{key.replace('_',' ').upper()}: ",
                   f"{min_val}{unit} - {max_val}{unit},",
                   f" in increments of {step}{unit}")       
               
    
def get_input_ranges(default_ranges):
    """
    Gets user input to potentially modify default input ranges.

    Args:
        default_ranges: A dictionary of default input ranges, 
                        where keys are input names and values are tuples 
                        of (min, max, step, unit).

    Returns:
        A dictionary of input ranges, where keys are input names and 
        values are tuples of (min, max, step, unit).
    """

    print("The default values of this calculator are as follows:")
    print_range(default_ranges)

    modified_ranges = {}
    while True:
        choice = input("Would you like to update any values? (y/n): ").lower()
        
        if choice != 'y':
            break    
        
        for key, _ in default_ranges.items():
            choice = input(f"Would you like to update {key.replace('_',' ')}? (y/n): ").lower()
            if choice == 'y':
                min_val = get_float_input(f"Enter minimum value for {key.replace('_',' ')}: ")
                max_val = get_float_input(f"Enter maximum value for {key.replace('_',' ')}: ")
                step = get_float_input(f"Enter increment for {key.replace('_',' ')}: ")
                unit = default_ranges[key][3]
                modified_ranges[key] = (min_val, max_val, step, unit)

        choice = input("Would you like to update any other values? (y/n): ").lower()
        if choice != 'y':
            break

    if not modified_ranges:
        return default_ranges

    for key, _ in default_ranges.items():
        if key not in modified_ranges:
            modified_ranges[key] = default_ranges[key]

    return modified_ranges