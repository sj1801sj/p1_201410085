﻿def home():

  myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
  yourhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}

  print yourhome - myhome
  print myhome - yourhome
  print myhome | yourhome
  print myhome & yourhome

  d=dict()

  for i in myhome:
    if i not in d:
      d[i]=1
    else:
      d[i]=d[i]+1
  for i in yourhome:
    if i not in d:
      d[i]=1
    else:
      d[i]=d[i]+1
  print d 

home()

raw_input()
