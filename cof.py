import numpy as np 
import plotly.express as px
import csv 
 
def getDataSource(data_path):
    ice_creame_sales=[]
    cold_drink_sales=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            ice_creame_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))
    return{"x":ice_creame_sales,"y":cold_drink_sales}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation bettwen temprature and ice-creame sales: -\n--->",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
