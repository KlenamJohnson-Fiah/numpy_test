from collections.abc import Iterable
import numpy as np

# Find the unique years from the data
def uniqueYears(numpy_array: Iterable, columnName: str) -> list:
    finding_uniqueYears_in_column = np.unique(numpy_array[columnName])
    return finding_uniqueYears_in_column


# using the unique years categorize the data by the years
# append data into a list
def categorize_by_Yearly(uniqueYears: list, dataset: Iterable) -> dict[int, list]:
    categorizedDic = {}
    for i in range(len(uniqueYears)):
        categorizedDic[uniqueYears[i]] = []
        for data in range(len(dataset)):
            if uniqueYears[i] == dataset["year"][data]:
                categorizedDic[uniqueYears[i]].append(dataset[data])
    return categorizedDic


def categorize_every_TENyears(uniqueYears: list, dataset: Iterable) -> dict[int, list]:
    categorizedDic = {}
    ten_years_tracker = []
    for i in range(len(uniqueYears)):
        addToYear = 0
        if uniqueYears[i] not in ten_years_tracker:
            categorizedDic[uniqueYears[i]] = []
            while addToYear <= 10:
                for data in range(len(dataset)):
                    if uniqueYears[i] + addToYear == dataset["year"][data]:
                        ten_years_tracker.append((uniqueYears[i] + addToYear))
                        categorizedDic[uniqueYears[i]].append(dataset[data])
                addToYear += 1

    ten_years_tracker = set(ten_years_tracker)

    return categorizedDic


# categorizing the data by months
def categorise_by_months(dataset: Iterable) -> dict[str, list]:
    finding_uniqueMonth_in_column = np.unique(dataset["month"])
    categorizedDic = {}

    for i in range(len(finding_uniqueMonth_in_column)):
        categorizedDic[finding_uniqueMonth_in_column[i]] = []

        for data in range(len(dataset)):
            if finding_uniqueMonth_in_column[i] == dataset["month"][data]:
                categorizedDic[finding_uniqueMonth_in_column[i]].append(dataset[data])
    return categorizedDic
