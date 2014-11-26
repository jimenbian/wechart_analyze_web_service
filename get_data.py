# -*- coding: utf-8 -*-
import re
def Get_data(filename):
  f1=open('static/Uploads/%s.txt'%(filename))
  f2=open('static/manage_upload/%s.txt'%(filename),'a')
  
  j=0#行数记录
  for line in f1.readlines():
     if j>=2:
     	 if '-' in line[:6] and '-' in line[6:9]:
     	  #  print re.sub(' +',' ',line.strip())
          f2.write('\n'+re.sub(' +',' ',line.strip()))
     	 else:
          f2.write(' '+line.strip())
     	
     else:
     	j+=1
     	continue

 