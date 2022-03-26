import csv
import pandas as pd

df = pd.read_csv("final_data.csv")

df_computed = pd.DataFrame(columns = ["Star_Name", "Distance", "Mass", "Radius","Gravity"])

G = 6.674e-11

for index, row in df.iterrows():
    try:
        m = float(row["Mass"])*1.989e+30
        r = float(row["Radius"])* 6.957e+8
        g = (G * m /(r * r))

        df_computed = df_computed.append({'Star_Name' : row["Star_name"], 'Distance' : row["Distance"], 'Mass' : m, 'Radius' : r, 'Gravity' : g}, ignore_index = True)
    except ValueError:
        print(f"Could not convert {row['Mass']} or {row['Radius']} to float.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

# print(df_computed)
df_computed.to_csv("star_with_gravity.csv")