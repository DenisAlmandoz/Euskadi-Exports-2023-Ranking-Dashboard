#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:51:18 2023

@author: Denis
"""

import pandas as pd

df= pd.read_csv("exportaciones euskadi.csv", sep=";")

df = df.drop(columns=['Unnamed: 0'])
df = df.loc[1:,:]
df_upd= df.to_csv
df.to_csv('exportaciones_mod.csv', index=False)
