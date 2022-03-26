import pandas as pd
import matplotlib.pyplot as plt
import csv

df = []
with open('star_with_gravity.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:
    if i != []:
      df.append(i)

headers = df[0]
headers[0] = 'Index'
data = df[1:]

Stars_filtered_with_distance = []
try:
  for i in data:
    if float(i[2]) <= 100:
      Stars_filtered_with_distance.append(i)
    else:
      pass
except:
  Stars_filtered_with_distance.append('Invalid')
Stars_filtered_with_Gravity = []
try:
  for i in Stars_filtered_with_distance:
    if float(i[5].split(' ')[0]) > 150 and float(i[5].split(' ')[0]) < 350:
      Stars_filtered_with_Gravity.append(i)
    else:
      pass
except:
  Stars_filtered_with_Gravity.append('Invalid')

print('Number of stars with distance less than 100 lightyears: ',len(Stars_filtered_with_distance))
print('Number of stars with Gravity within 150-350 m/s2 : ',len(Stars_filtered_with_Gravity)-1)

with open('filtered_stars.csv','w') as f:
  csvWriter = csv.writer(f)
  csvWriter.writerow(headers)
  csvWriter.writerows(Stars_filtered_with_Gravity)