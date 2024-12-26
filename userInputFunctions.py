# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:12:55 2024

@author: natur
"""

import numpy as np
def input_array():

    house_cost = np.arange(250_000,360_000,10_000)

    downpayment = np.arange(40_000,70_000,10_000)

    interest_rate = np.arange(700, 800, 25) / (10_000)

    loan_term_years = np.arange(20, 40, 10)

    property_tax_rate = np.arange(.010, .011, .001)

    pmi_rate = np.arange(0.005,0.02,0.005)
     
    option = int(input(('The default values of this calculator are as follows and may be modified'
           ' as desired.\n'
           ' HOUSE COST: $200,000 - $400,000, in increments of $10,000.\n'
           ' DOWNPAYMENT: $0 - $70,000, in increments of $10,000.\n'
           ' INTEREST RATE: 7.00% - 8.00%, in increments of 0.25%.\n'
           ' LOAN TERM: 20 - 30 years, in increments of 10 years.\n'
           ' PROPERTY TAX: 1.0% - 1.1%, in increments of 0.1%.\n'
           ' PMI rate: 0.5% - 2.0% ,in increments of 0.05%.\n'
           'Please select what inputs you would like to consider using the '
           'following options: \n '
           '   1. Default values. \n'
           'No other options are available at this time.\n')))
    
    match option:
        case 1: print("You have selected the default option.")
             
        case 2: print("Program will use the default options.")
             
        case 3: print("Program will use the default options.")
        
        case _:
            print("Your input isn't recognized. Program will use the default options.")
            
    list_of_inputs = [house_cost, downpayment, interest_rate,
                                 loan_term_years, property_tax_rate, pmi_rate]
    
    return list_of_inputs
