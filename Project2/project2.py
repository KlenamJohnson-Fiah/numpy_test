import random
import numpy as np
import matplotlib.pyplot as plt
import functions


dataset = np.genfromtxt(
    "US_births_1994_2014_monthly.csv",
    dtype=[("year", np.int_), ("month", np.int_), ("births", np.int_)],
    skip_header=1,
    delimiter=",",
)
print("\nThe mean of births : {:31.2f}".format(np.mean(dataset["births"])))
print("The highest number of births : {:21}".format(np.amax(dataset["births"])))
print("The least number of births : {:23}".format(np.amin(dataset["births"])))
print("The standard deviation for births : {:16.2f}".format(np.std(dataset["births"])))
print("The median of births : {:29.2f}".format(np.median(dataset["births"])))


uniqueYears = functions.uniqueYears(dataset, "year")


# # store categorized data (yearly) in separate numpy array
# # this done by dynamically creating the variables using the key
# # feeding the values to numpy
allYears_categorized = functions.categorize_by_Yearly(uniqueYears, dataset)
for k, v in allYears_categorized.items():
    globals()[f"np_year_{k}"] = np.array(allYears_categorized[k])


# First graph for categorizing data into years
# Line plot
plt.figure(figsize=(10, 6))
for k, v in allYears_categorized.items():
    plt.plot(
        globals()[f"np_year_{k}"]["month"],
        globals()[f"np_year_{k}"]["births"],
        label=str(k),
    )
    plt.legend(title="Years", loc="upper left", numpoints=1, ncol=4, fontsize=5)

plt.title("Number of births in the US from 1994 to 2014 categorized monthly ")
plt.xlabel("months January(1) to December(12)")
plt.ylabel("number of births")
plt.show()

# Second graph for categorizing data into years
# Scatter plot
plt.figure(figsize=(10, 6))
for k, v in allYears_categorized.items():

    plt.scatter(
        globals()[f"np_year_{k}"]["month"],
        globals()[f"np_year_{k}"]["births"],
        label=str(k),
    )
    plt.legend(title="Years", loc="upper left", scatterpoints=1, ncol=4, fontsize=5)
plt.title("Number of births in the US from 1994 to 2014 categorized monthly")
plt.xlabel("months January(1) to December(12)")
plt.ylabel("number of births")

plt.show()

# store categorized data (now current year and 10years i.e 1994 to 2004 as a single collection) in separate numpy array
# this done by dynamically creating the variables using the key
# feeding the values to numpy
overTenYears = functions.categorize_every_TENyears(uniqueYears, dataset)
for k, v in overTenYears.items():
    globals()[f"np_tenYears_{k}_{k+10}"] = np.array(overTenYears[k])


# First graph for categorizing data into groups of ten years
# Box plot
labels_Can = []
np_arrays_Can = []
plt.figure(figsize=(10, 6))
for k, v in overTenYears.items():
    np_arrays_Can.append(globals()[f"np_tenYears_{k}_{k+10}"]["births"])
    labels_Can.append(f"{k} to {k+10}")
plt.boxplot(
    np_arrays_Can,
    patch_artist=True,
    labels=labels_Can,
)
plt.title(
    "Boxplot of number of births in the US from 1994 to 2014 grouped into two groups of 10year periods"
)
plt.xlabel("Ten year groups. NB: data ends at 2014")
plt.ylabel("births")
plt.show()

# Second graph for categorizing data into groups of ten years
# Bar plot
x = []
y = []
color = ["red", "blue"]
plt.figure(figsize=(10, 6))
for k, v in overTenYears.items():
    x.append(f"{k} to {k+10}")
    y.append(np.mean(globals()[f"np_tenYears_{k}_{k+10}"]["births"]))
    plt.bar(x, y, label=x, color=color)

plt.title(
    "Bar graph of mean values of US births from 1994 to 2014 monthly grouped into two groups of 10year periods"
)
plt.xlabel("Ten year groups. NB: data ends at 2014")
plt.ylabel("Number of births")
plt.show()


# store categorized data (monthly) in separate numpy array
# this done by dynamically creating the variables using the key
# feeding the values to numpy
categorizedMonthly = functions.categorise_by_months(dataset)
for k, v in categorizedMonthly.items():
    globals()[f"np_month_{k}"] = np.array(categorizedMonthly[k])

# First graph for categorizing data into months
# bar plot
month = []
mean = []
col2 = []
plt.figure(figsize=(10, 6))
for k, v in categorizedMonthly.items():
    r = random.random()
    b = random.random()
    g = random.random()
    col = (r, g, b)
    col2.append(col)
    month.append(k)
    mean.append(np.mean(globals()[f"np_month_{k}"]["births"]))
    plt.bar(
        month,
        mean,
        label=month,
        color=col2,
    )
plt.title("Bar graph showing the monthly mean value for US births from 1994 to 2014 ")
plt.xlabel("months January(1) to December(12)")
plt.ylabel("births")
plt.show()


# Second graph for categorizing data into months
# Box plot
np_arrays_CatMonthly = []
catMonthly_labels = []
colors = []
count = 0

# Generate 12 RGB values for graph
while count <= 12:
    r = random.random()
    b = random.random()
    g = random.random()
    col = (r, g, b)
    colors.append(col)
    count += 1

plt.figure(figsize=(10, 6))
for k, v in categorizedMonthly.items():
    colors.append(col)
    np_arrays_CatMonthly.append(globals()[f"np_month_{k}"]["births"])
    catMonthly_labels.append(k)
    box = plt.boxplot(np_arrays_CatMonthly, labels=catMonthly_labels, patch_artist=True)

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

plt.title(
    "Boxplot of the number of births for each month January(1) to December (12) from the years 1994-2014"
)
plt.xlabel("months January(1) to December(12)")
plt.ylabel("births count")

plt.show()


# Q5d.
# Violin plo
np_arrays_CatMonthly2 = []
catMonthly_labels2 = []

plt.figure(figsize=(17, 6))
for k, v in categorizedMonthly.items():
    colors.append(col)
    np_arrays_CatMonthly2.append(globals()[f"np_month_{k}"]["births"])
    catMonthly_labels2.append(k)
    box = plt.violinplot(np_arrays_CatMonthly2, showmeans=True, showmedians=True)

    # for patch, color in zip(box["boxes"], colors):
    #     patch.set_facecolor(color)

plt.title(
    "Q5d. Violin plot of the number of births for each month January(1) to December (12) from the years 1994-2014 showing mean and median"
)
plt.xlabel("months January(1) to December(12)")
plt.ylabel("births count")

plt.show()
