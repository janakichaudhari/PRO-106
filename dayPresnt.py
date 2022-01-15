import plotly.express as px
import csv
import numpy as n

def getdata():
    tem=[]
    sales=[]
    with open ("days present.csv") as i:
        df=csv.DictReader(i)
        for d in df:
            tem.append(float(d["Marks In Percentage"]))
            sales.append(float(d["Days Present"]))
    return {"x":tem,"y":sales}
def correlation(getd):
    co=n.corrcoef(getd["x"],getd["y"])

    print(co[0,1])
def main():
    getd=getdata()
    correlation(getd)
main()

