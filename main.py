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

matrix = add_columns_matrix(matrix)



facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", \
              "Downpayment", "Pmi Rate", save = True)
facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", \
              "Property Tax Rate", "Downpayment", save=True)
