# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:05:34 2024

@author: 12aan
"""

from mortgage import *
import numpy_financial as npf
import numpy as np

house_cost = np.arange(250_000,360_000,10_000)

downpayment = np.arange(40_000,70_000,10_000)

interest_rate = np.arange(700, 800, 25) / (10_000)

loan_term_years = np.arange(30, 40, 10)

property_tax_rate = np.arange(.010, .011, .001)

pmi_rate = np.arange(0.005,0.02,0.005)


matrix = create_df_matrix_6(house_cost, downpayment, interest_rate,
                             loan_term_years, property_tax_rate, pmi_rate,
                            "Condo Cost","Downpayment","Interest Rate",
                             "Term","Prop Tax Rate","PMI Rate")


maintenance_rate = 1.0 / 100
matrix["Maintenance"] = matrix["Condo Cost"] * maintenance_rate / 12
matrix["Loan Amount"] = matrix["Condo Cost"] - matrix["Downpayment"]
matrix["Monthly Tax"] = calculate_property_tax(
                            matrix["Condo Cost"], 
                            matrix["Prop Tax Rate"]
                            )

matrix["Monthly Tax"] = matrix.apply(lambda row: row['Condo Cost'] * row['Prop Tax Rate'] / 12, axis=1)

matrix["Monthly PMI"] = matrix.apply(lambda row: 0 if (row['Downpayment'] >= (0.2 * row['Condo Cost'])) else
                                          row['Condo Cost'] * row['PMI Rate'] / 12, axis=1)


matrix["Mortgage"] = matrix.apply(lambda row: -1 * npf.pmt((row["Interest Rate"]/12), 
                                                      (row["Term"] * 12), 
                                                       row["Loan Amount"]
                                                      ), axis=1)

matrix["Total Monthly Payment"] = matrix["Mortgage"] + matrix["Monthly Tax"] + matrix["Maintenance"] + matrix["Monthly PMI"]

matrix["Payment without PMI"] = matrix["Mortgage"] + matrix["Monthly Tax"] + matrix["Maintenance"]

matrix["Total Mortgage Payments"] = (matrix["Mortgage"]+matrix["Monthly Tax"]+matrix["Maintenance"]) * matrix["Term"] * 12

matrix["Total Interest Payments"] = matrix["Total Mortgage Payments"] - matrix["Condo Cost"]

matrix["Rent"] = 1600

matrix["Total Rent with 1% Increases"] = matrix.apply(lambda row: npf.fv(.01/12, 
                                                      row["Term"] * 12,
                                                      row["Rent"], #assuming mortgage is greater than rent
                                                       0
                                                      ), axis=1)

matrix["Invested Cash at 6%"] = -1 * matrix.apply(lambda row: npf.fv(.06/12, 
                                                      row["Term"] * 12,
                                                      0,
                                                      row["Downpayment"]
                                                      ), axis=1)

matrix["Condo Value at 4%"] = -1 * matrix.apply(lambda row: npf.fv(.04/12, 
                                                      row["Term"] * 12,
                                                      0,
                                                       row["Condo Cost"]
                                                      ), axis=1)

matrix["Rent Cost"] = matrix["Invested Cash at 6%"] - matrix["Total Rent with 1% Increases"]
matrix["Buy Cost"] = matrix["Condo Value at 4%"] - matrix["Total Mortgage Payments"]
matrix["Buying Cost minus Renting Cost"] = matrix["Buy Cost"] - matrix["Rent Cost"]
import seaborn as sns

matrix["Cost (k)"] = matrix["Condo Cost"]/1000
def facetGridPlot(df, sortingVariableCol, 
                  xVariable, yVariable, colorVariable, sortingVariableRow,
                  sharex = False, sharey = True, legend_out = True,
                  aspect = 1, col_wrap = 2, height = 3, palette = "viridis",
                  save = False
                  ):
    sns.set_style("ticks",{'axes.grid' : True})
    g = sns.FacetGrid(df, 
                      col = sortingVariableCol,
                      row = sortingVariableRow,
                      hue = colorVariable,
                      palette = palette,
                      aspect = aspect,
                      height = height,
                      sharex = sharex,
                      sharey = sharey,
                      legend_out = legend_out,
                      #alpha = alpha
                      )
    #sns.color_palette(palette='viridis')
    g.map(sns.scatterplot, xVariable, yVariable)
    g.set_axis_labels(xVariable, yVariable)
    g.set_xticklabels(rotation = 45)
    g.add_legend()
    g.refline(y=1600)
    g.refline(y=2300)

    if save == True:
        
        g.savefig("facetgridplot_by_" + sortingVariableCol + "-" + sortingVariableRow 
                    + "_showing_" + colorVariable
                    + "_xy_" + xVariable + "_" + yVariable,bbox_inches='tight')
    return


facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", "Downpayment", "PMI Rate", save = True)
facetGridPlot(matrix, "Interest Rate", "Cost (k)", "Total Monthly Payment", "Prop Tax Rate", "Downpayment", save=True)
