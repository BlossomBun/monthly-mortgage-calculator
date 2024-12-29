# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:35:06 2024

@author: 12aan
"""

import numpy_financial as npf
import pandas as pd

def calculate_mortgage_payment_simple(loan_amount, interest_rate, loan_term_years):
    """Calculates the monthly mortgage payment.
    
    Args:
      loan_amount: The total amount of the loan.
      interest_rate: The annual interest rate (as a decimal).
      loan_term_years: The loan term in years.
    
    Returns:
      The monthly mortgage payment.
    """
    
    monthly_rate = interest_rate / 12
    num_payments = loan_term_years * 12
    
    return npf.pmt(monthly_rate, num_payments, loan_amount)

def calculate_mortgage(principal, interest_rate, loan_term, per = 1):

    """Calculates monthly mortgage payment with optional PMI.

    Args:
        principal (float): Mortgage amount.
        interest_rate (float): Annual interest rate (as a decimal).
        loan_term (int): Loan term in years.
        

    Returns:
        float: Monthly mortgage payment, with PMI.
    """

    monthly_rate = interest_rate / 12
    num_payments = loan_term * 12

    ipmt = npf.ipmt(monthly_rate, per, num_payments, principal)
    ppmt = npf.ppmt(monthly_rate, per, num_payments, principal)
    monthly_mortgage_payment = ipmt + ppmt
    
    return monthly_mortgage_payment, ipmt, ppmt

def calculate_property_tax(assessed_house_amount, property_tax_rate):
    """Calculates the monthly mortgage payment.
    
    Args:
      assessed_house_amount: The assessed value of the house.
      porperty_tax_rate: The annual tax rate (as a decimal).
    
    Returns:
      The monthly property tax payment.
    """ 
    yearly_tax = assessed_house_amount * property_tax_rate
    
    return yearly_tax / 12
      

def calculate_pmi(house_cost, pmi_rate=0.005, downpayment=0):
    """Calculates the monthly mortgage payment.
    
    Args:
        house_cost: Sticker price of the house.
        down_payment (float, optional): Down payment amount. 
                                        Defaults to 0.
        pmi_rate (float, optional): PMI interest rate (as a decimal). 
                                    Defaults to 0.005. (0.5%)
    Returns:
      The monthly property tax payment.
    """ 
    if downpayment < 0.2 * house_cost:
        pmi = pmi_rate * house_cost / 12
    else:
        pmi = 0

    return pmi
      

def create_df_matrix(list_of_arrays, list_of_names):
    """Creates a dataframe with all combinations of values in input arrays.
    
    Args:
        list_of_arrays (list): A list of arrays containing values.
        
        list_of_names (list): A list of strings.
            Become the column headers for the final dataframe
            
    Returns:
      The monthly property tax payment.
    """ 
    
    # Reshape the given arrays to repeat as needed to allow all combinations
    reshaped_arrays = pd.core.reshape.util.cartesian_product(list_of_arrays)
    
    # Place reshaped arrays into a dataframe and name the columns based on the
    # input list-of-names
    matrix = pd.DataFrame(dict(zip(list_of_names,reshaped_arrays)))
    
    return matrix


def add_columns_matrix(matrix):
    """Adds additional values to the data matrix based on initial inputs
    
    Args:
        DataFrame with the following columns names:
            "Condo Cost"
            "Downpayment"
            "Property Tax Rate"
            "PMI Rate"
            "Loan Term"
            "Interest Rate"
          
    Returns:
      DataFrame with many more column names:
          
    """ 
    maintenance_rate = 1.0 / 100
    
    matrix["Maintenance"] = matrix["Condo Cost"] * maintenance_rate / 12
    
    matrix["Loan Amount"] = matrix["Condo Cost"] - matrix["Downpayment"]
    
    matrix["Monthly Tax"] = calculate_property_tax(
                                matrix["Condo Cost"], 
                                matrix["Property Tax Rate"]
                                )
    
    matrix["Monthly Tax"] = matrix.apply(lambda row: row['Condo Cost'] * row['Property Tax Rate'] / 12, axis=1)
    
    matrix["Monthly PMI"] = matrix.apply(lambda row: 0 if (row['Downpayment'] >= (0.2 * row['Condo Cost'])) else
                                              row['Condo Cost'] * row['Pmi Rate'] / 12, axis=1)
    
    
    matrix["Mortgage"] = matrix.apply(lambda row: -1 * npf.pmt((row["Interest Rate"]/12), 
                                                          (row["Loan Term"] * 12), 
                                                           row["Loan Amount"]
                                                          ), axis=1)
    
    matrix["Total Monthly Payment"] = matrix["Mortgage"] + matrix["Monthly Tax"] + matrix["Maintenance"] + matrix["Monthly PMI"]
    
    matrix["Payment without PMI"] = matrix["Mortgage"] + matrix["Monthly Tax"] + matrix["Maintenance"]
    
    matrix["Total Mortgage Payments"] = (matrix["Mortgage"]+matrix["Monthly Tax"]+matrix["Maintenance"]) * matrix["Loan Term"] * 12
    
    matrix["Total Interest Payments"] = matrix["Total Mortgage Payments"] - matrix["Condo Cost"]
    
    matrix["Cost (k)"] = matrix["Condo Cost"]/1000
    
    return matrix