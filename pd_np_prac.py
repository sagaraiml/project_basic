# -*- coding: utf-8 -*-
"""
Created on Wed Jan 9 20:20:13 2019

@author: sagar_paithankar
"""
import pandas as pd
import numpy as np

a = np.random.randint(5, 50, 12).reshape((3,4))
b = np.random.randint(-50, -5, 12).reshape((3,4))

a = pd.DataFrame(a)
b = pd.DataFrame(b)

x = a.copy()
y = b.copy()

data = {
        'emp_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],
        'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']
        }
df_1 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
data = {
        'emp_id': ['4', '5', '6', '7'],
        'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],
        'last_name': ['Alexander', 'Suma', 'Mike', 'G']
        }
df_2 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])

x_app_y = x.append(y, ignore_index=True)
#x_app_y = x.append(y); x_app_y.reset_index(inplace=True); x_app_y.drop(columns='index', inplace=True)
z = pd.DataFrame()
z = z.append(x_app_y)
del x_app_y, z