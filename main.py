from pandas import read_csv
import plotly.figure_factory as ff
import statistics
import random

df = read_csv('data.csv')
data = df['Math_score'].to_list()


data_mean = statistics.mean(data)
# data_mode = statistics.mode(data)
# data_median = statistics.median(data)
# data_stdev = statistics.stdev(data)


print(f"{data_mean}")


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std_dev = statistics.stdev(mean_list)
print("Mean of sampling distribution :-", mean)
print("Standard Deviation of sampling distribution :-", std_dev)

# fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
# fig.show()

# fig = ff.create_distplot([data],['Maths Score'], show_hist=False)
# fig.show()
