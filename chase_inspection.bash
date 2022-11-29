#!/bin/bash -xv

chase=./chase.py

#Test
if [ $? = 0 ]; then
  echo "chaseは正常終了"
else
  echo "chaseは異常終了"
fi
if [ -f blue.png ]; then
  echo "png"
fi
