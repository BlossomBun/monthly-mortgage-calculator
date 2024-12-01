# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:12:55 2024

@author: natur
"""


def input_array():

    """Calculates monthly mortgage payment with optional PMI.

    Args:
        principal (float): Mortgage amount.
        interest_rate (float): Annual interest rate (as a decimal).
        loan_term (int): Loan term in years.
        

    Returns:
        float: Monthly mortgage payment, with PMI.
    """

    house_cost = np.arange(250_000,360_000,10_000)

    downpayment = np.arange(40_000,70_000,10_000)

    interest_rate = np.arange(700, 800, 25) / (10_000)

    loan_term_years = np.arange(30, 40, 10)

    property_tax_rate = np.arange(.010, .011, .001)

    pmi_rate = np.arange(0.005,0.02,0.005)
    
    list_of_inputs = [house_cost, downpayment, interest_rate,
                                 loan_term_years, property_tax_rate, pmi_rate]
    
    return list_of_inputs
