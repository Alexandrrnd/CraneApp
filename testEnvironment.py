# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:23:41 2021

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from Check_List import CheckListEvaluator 

    # Определение значений лингвистических переменных
answers = [0,1,2,1,2,1,0,3,4,1,1,2]
    
clEvaluator = CheckListEvaluator(True)
print(clEvaluator.evaluateSafetyState(answers))