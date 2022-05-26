import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import statistics as st
import random
import math
import pandas as pd
import csv
df = pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()

dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=st.mean(dataset)
std_deviation=st.stdev(dataset)
print("mean of sample",mean)
print("std_deviation of sample",std_deviation)
#go to find mean of 100 data points 1000 times and plot it
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean
#function to plot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=st.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
# pass the number of times ypu want the mean of data points as parameter in range
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=st.mean(mean_list)
    print("mean of sampling distribution",mean)
setup()
#Code to find mean of raw data
population_mean=st.mean(data)
print("population mean",population_mean)
#Code to find the standard deviation of sample data
def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=st.stdev(mean_list)
    print("Standard Deviation of sampling distribution",std_deviation)
standard_deviation()
