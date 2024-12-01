# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:38:44 2024

@author: natur
"""
import seaborn as sns

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
