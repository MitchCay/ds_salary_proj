# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:24:55 2020

@author: caywo
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/caywo/Documents/ds_salary_proj"

df = gs.get_jobs('physics', 1500, False, path+"/chromedriver", 15)

df.to_csv(path+"/glassdoor_jobs.csv", index=False, header=True)