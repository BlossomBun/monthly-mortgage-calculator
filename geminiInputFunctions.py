# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:18:00 2024

@author: 12aan
"""


import numpy as np

def get_input_ranges(default_ranges):
    """
    Gets user input to potentially modify default input ranges.

    Args:
        default_ranges: A dictionary of default input ranges, 
                        where keys are input names and values are tuples 
                        of (min, max, step).

    Returns:
        A dictionary of input ranges, where keys are input names and 
        values are tuples of (min, max, step).
    """

    print("The default values of this calculator are as follows and may be modified as desired.")
    
    for key, (min_val, max_val, step) in default_ranges.items():
        print(f"{key.upper()}: {min_val} - {max_val}, in increments of {step}")

    modified_ranges = {}
    while True:
        for key, _ in default_ranges.items():
            choice = input(f"Would you like to update {key}? (y/n): ").lower()
            if choice == 'y':
                min_val = get_float_input(f"Enter minimum value for {key}: ")
                max_val = get_float_input(f"Enter maximum value for {key}: ")
                step = get_float_input(f"Enter increment for {key}: ")
                modified_ranges[key] = (min_val, max_val, step)

        choice = input("Would you like to update any other values? (y/n): ").lower()
        if choice != 'y':
            break

    if not modified_ranges:
        print("Using default values.")
        return default_ranges

    for key, _ in default_ranges.items():
        if key not in modified_ranges:
            modified_ranges[key] = default_ranges[key]

    return modified_ranges

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    default_ranges = {
        "house_cost": (250000, 360000, 10000),
        "downpayment": (40000, 70000, 10000),
        "interest_rate": (0.07, 0.08, 0.0025),
        "loan_term": (20, 40, 10),
        "property_tax_rate": (0.010, 0.011, 0.001),
        "pmi_rate": (0.005, 0.02, 0.005),
    }

    input_ranges = get_input_ranges(default_ranges)

    # Generate input arrays
    input_arrays = {}
    for key, (min_val, max_val, step) in input_ranges.items():
        input_arrays[key] = np.arange(min_val, max_val + step, step)

    # Print the final input ranges
    print("\nThe program will use the following inputs:")
    for key, (min_val, max_val, step) in input_ranges.items():
        print(f"{key.replace("_"," ").upper()}: {min_val} - {max_val}, in increments of {step}")

    return input_arrays