import plotly.express as px
import csv
import numpy as n

def getdata():
    tem=[]
    sales=[]
    with open ("cofe.csv") as i:
        df=csv.DictReader(i)
        for d in df:
            tem.append(float(d["Coffee in ml"]))
            sales.append(float(d["sleep in hours"]))
    return {"x":tem,"y":sales}
def correlation(getd):
    co=n.corrcoef(getd["x"],getd["y"])

    print(co[0,1])
def main():
    getd=getdata()
    correlation(getd)
main()

