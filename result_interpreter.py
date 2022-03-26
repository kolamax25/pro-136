import csv
import pandas as pd
import plotly.express as px

rows = []

with open("star_with_gravity.csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]

header[0] = "Index"

name = []
distance = []
mass = []
radius = []
gravity = []

for planet_data in planetData:
    name.append(planet_data[1])
    distance.append(planet_data[2])
    mass.append(planet_data[3])
    radius.append(planet_data[4])
    gravity.append(planet_data[5])


fig = px.bar(x=name, y=mass, title = 'Mass Graph')
fig.show()
fig1 = px.bar(x=name, y=radius, title = 'Radius Graph')
fig1.show()
fig2 = px.bar(x=name, y=distance, title = 'Distance Graph')
fig2.show()
fig3 = px.bar(x=name, y=gravity, title = 'Gravity Graph')
fig3.show()