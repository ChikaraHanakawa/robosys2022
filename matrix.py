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
    JohnWick = np.identity(a)
    return JohnWick
  except:
    print("") 

Keanu = np.array([0,1,2, [4,5,6]])
Reeves = np.array([7,8,9, [10,11,12]])
KeanuReeves = Keanu + Reeves

print(KeanuReeves)

for n in sys.stdin:
  speed = Wachowski
print(speed)
