#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2022 Chikara Hanakawa
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause

import cv2
import sys
import numpy as np

def Wachowski(a):
  try:
    KeanuReeves = np.identity(a)
    return KeanuReeves
  except:
    print("") 

#Keanu = np.array([0,1,2, [4,5,6]])
#Reeves = np.array([7,8,9, [10,11,12]])

answer = 0
for line in sys.stdin:
  answer = Wachowski(line)
  print(answer)
