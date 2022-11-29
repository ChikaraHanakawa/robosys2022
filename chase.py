#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2022 Chikara Hanakawa 
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause

import cv2
import numpy as np

#動画取得
cap = cv2.VideoCapture(0)

#1フレームを保存する際の最低画素値
oneframe = np.array([0, 0, 0, [0, 0, 0,[0, 0, 0]]])

#色の設定
def detect(frame):

  #BGR色空間をHSV色空間に変更
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  #blue
  color_min = np.array([110,50,50])
  color_max = np.array([130,255,255])

  #画素を指定してそれ以外を0とする
  mask = cv2.inRange(hsv, color_min, color_max)
  return mask

#撮影開始
while(cap.isOpened()):

  #動画の読み取り
  ret, frame = cap.read()
  
  #グレースケールの取得
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  mask = detect(frame)

  #強調表示する
  res = cv2.bitwise_and(gray, mask) 
  ans = cv2.applyColorMap(res, cv2.COLORMAP_JET)

  #動画の表示（結果の表示）
  cv2.imshow('Video',frame)
  cv2.imshow('Mask',mask)
  cv2.imshow('Result',ans)

  #青色を認識するとその1フレームで画像を保存
  if mask != oneframe:
    cv2.imwrite('blue.png', frame)

  #キーが打たれると終了
  key = cv2.waitKey(1)

  if key != -1:
    break

#撮影終了
cap.release()

#ウィンドウを全て閉じる
cv2.destroyAllWindows()
