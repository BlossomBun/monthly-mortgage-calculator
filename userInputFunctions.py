# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:12:55 2024

@author: natur
"""

import numpy as np

dict_inputs = {
    2: 'house cost',
    3: 'downpayment',
    4: 'interest rate',
    5: 'loan term',
    6: 'property tax',
    7: 'PMI rate'}

unit_dict = {
    2: '$',
    3: '$',
    4: '%',
    5: ' years',
    6: '%',
    7: '%'}

def input_array():
    house_cost = np.arange(250_000,360_000,10_000)

    downpayment = np.arange(40_000,70_000,10_000)

    interest_rate = np.arange(.07, .08, .0025)

    loan_term_years = np.arange(20, 40, 10)

    property_tax_rate = np.arange(.010, .011, .001)

    pmi_rate = np.arange(0.005,0.02,0.005)
    
    
    print(('The default values of this calculator are as follows and may '
          'be modified as desired.'))
    print_input(2, house_cost)
    print_input(3, downpayment)
    print_input(4, interest_rate)
    print_input(5, loan_term_years)
    print_input(6, property_tax_rate)
    print_input(7, pmi_rate)
    
    
    list_options = [1,2,3,4,5,6,7,8]
    
    option = ask_first_input([1,2,3,4,5,6,7])
    continue_flag = True
    
    list_options.remove(1)
    
    while continue_flag:
        match option:
            case 1: 
                print("You have selected the default options.")
                continue_flag = False
                 
            case 2: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                house_cost = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)
                
            case 3: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                downpayment = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)

            case 4: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                interest_rate = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)

            case 5: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                loan_term_years = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)

            case 6: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                property_tax_rate = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)              

            case 7: 
                print(f"You have choosen to update the {dict_inputs[option]}.")
                min_value = update_value('minimum')
                max_value = update_value('maximum')
                inc_value = update_value('increment')
                pmi_rate = np.arange(min_value,max_value+inc_value,inc_value)
                list_options.remove(option)
                
            case 8:
                print("Thank you for your selections.")
                continue_flag = False
                
            case _:
                print("Your input isn't recognized. Program will continue with established options.")
                continue_flag = False
        
        if continue_flag:
            option = ask_added_input(list_options)
    
    print("The program will use the following inputs: ")
    print_input(2, house_cost)
    print_input(3, downpayment)
    print_input(4, interest_rate)
    print_input(5, loan_term_years)
    print_input(6, property_tax_rate)
    print_input(7, pmi_rate)
    
    
    list_of_inputs = [house_cost, downpayment, interest_rate,
                                 loan_term_years, property_tax_rate, pmi_rate]
    
    return list_of_inputs





def ask_first_input(list_options):
    initial_message = ('Please select what inputs you would like to consider using the '
   'following options:')
    
    initial_message = initial_message + create_options_list(list_options)
    
    return ask_input(initial_message)




def create_options_list(list_options_to_include):
    message = ""
    dict_options = {}
    for i in range(8):
        if i==0:
            dict_options[i+1] = f"\n   {i+1}: Default values."
        elif i==7:
            dict_options[i+1] = f"   {i+1}: Use defaults for remaining values."
        else:
            dict_options[i+1] = f"   {i+1}: Update {dict_inputs[i+1]}."

    for option in list_options_to_include:
        message += dict_options[option]
        message += "\n"

    message += 'No other options are available at this time.\n'
     
    return message




def ask_input(initial_message, 
              input_message = 'Please enter your selection now:   ',
              error_message = "Invalid input. Enter a number. Try again."):
    continue_flag = True
    
    print(initial_message)
    
    while continue_flag:
        try:
            option = float(input(input_message))
            continue_flag = False
        except ValueError:
            print(error_message)
        
    return option



def ask_added_input(list_options_to_include):
    initial_message = 'Would you like to enter any other values?\n'
    initial_message += create_options_list(list_options_to_include)
    return ask_input(initial_message)



def update_value(type_of_value):
    initial_message = f'What {type_of_value} value would you like to use?'
    return ask_input(initial_message)




def print_input(key, arange):   
   minimum = arange[0]
   maximum = arange[-1]
   if len(arange) > 1:
       increment = arange[1] - arange[0]
   else:
       increment = 0
   
   print((dict_inputs[key].upper() + ": " + add_unit(key, minimum) +
          " - " + add_unit(key, maximum) +
          ", in increments of " + add_unit(key, increment) + "."))
   
   return
        


def add_unit(key, value):
   if key == 2 or key == 3:
       return unit_dict[key] + f"{value:,}"
   elif key == 5:
       return f"{value:,.0f}" + unit_dict[key]
   else:
       return f"{value*100:.3f}" + unit_dict[key]
  