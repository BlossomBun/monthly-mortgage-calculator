# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:05:34 2024

@author: 12aan
"""

from baseFunctions import *
from plotFunctions import *
from userInputFunctions import *
import pandas as pd #remove when returning to function



# Create an input array
dict_of_arrays = input_array()

column_names = [key.replace("_"," ").title() for key in list(dict_of_arrays.keys())]

matrix = create_df_matrix(list(dict_of_arrays.values()), column_names)


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

matrix["Rent"] = 1600

matrix["Total Rent with 1% Increases"] = matrix.apply(lambda row: npf.fv(.01/12, 
                                                      row["Loan Term"] * 12,
                                                      row["Rent"], #assuming mortgage is greater than rent
                                                       0
                                                      ), axis=1)

matrix["Invested Cash at 6%"] = -1 * matrix.apply(lambda row: npf.fv(.06/12, 
                                                      row["Loan Term"] * 12,
                                                      0,
                                                      row["Downpayment"]
                                                      ), axis=1)

matrix["Condo Value at 4%"] = -1 * matrix.apply(lambda row: npf.fv(.04/12, 
                                                      row["Loan Term"] * 12,
                                                      0,
                                                       row["Condo Cost"]
                                                      ), axis=1)

matrix["Rent Cost"] = matrix["Invested Cash at 6%"] - matrix["Total Rent with 1% Increases"]
matrix["Buy Cost"] = matrix["Condo Value at 4%"] - matrix["Total Mortgage Payments"]
matrix["Buying Cost minus Renting Cost"] = matrix["Buy Cost"] - matrix["Rent Cost"]

matrix["Cost (k)"] = matrix["Condo Cost"]/1000

#facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", "Downpayment", "PMI Rate", save = True)
#facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", "Property Tax Rate", "Downpayment", save=True)
