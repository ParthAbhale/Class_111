from pandas import read_csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = read_csv('data1.csv')
data = df['Math_score']

mean = statistics.mean(data)
# median = statistics.median(data)
# mode = statistics.mode(data)
stdev = statistics.stdev(data)

print(mean,stdev)

s1,e1 = mean - stdev, mean + stdev
s2,e2 = mean + (2* stdev), mean + (2 * stdev)
s3,e3 = mean + (3* stdev), mean + (3* stdev)

fig = ff.create_distplot([data],["Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode = "lines",name = "Mean-1"))
fig.add_trace(go.Scatter(x=[s1,s1],y=[0,0.17],mode = "lines",name = "Std-1"))
fig.add_trace(go.Scatter(x=[s2,s2],y=[0,0.17],mode = "lines",name = "Std-2"))
fig.add_trace(go.Scatter(x=[s3,s3],y=[0,0.17],mode = "lines",name = "Std-3"))
fig.add_trace(go.Scatter(x=[e1,e1],y=[0,0.17],mode = "lines",name = "Std-1"))
fig.add_trace(go.Scatter(x=[e2,e2],y=[0,0.17],mode = "lines",name = "Std-2"))
fig.add_trace(go.Scatter(x=[e3,e3],y=[0,0.17],mode = "lines",name = "Std-3"))

fig.show()