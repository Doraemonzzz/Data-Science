# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:03:24 2018

@author: Administrator
"""

import pandas as pd
import numpy as np

dates=pd.date_range('20170520',periods=7)
print(dates)

datesdf=pd.DataFrame(np.random.randn(7,3),index=dates,columns=list('ABC'))

print(datesdf)