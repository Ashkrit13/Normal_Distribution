import csv
import statistics
import pandas as pd

df = pd.read_csv("student_data.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

mean_height = statistics.mean(height_list)
mean_weight = statistics.mean(weight_list)

median_height = statistics.median(height_list)
median_weight = statistics.median(weight_list)

mode_height = statistics.mode(height_list)
mode_weight = statistics.mode(weight_list)

print("Mean, Median, and Mode of Height is: {}, {}, {} respectivly".format(mean_height, median_height, mode_height))
print("Mean, Median, and Mode of Weight is: {}, {}, {} respectivly".format(mean_weight, median_weight, mode_weight))

sd_height = statistics.stdev(height_list)
sd_weight = statistics.stdev(weight_list)

print("Standard Deviation for Height is:", sd_height)
print("Standard Deviation for Weight is:", sd_weight)

firstsd_height_start, firstsd_height_end = mean_height - sd_height, mean_height + sd_height
secondsd_height_start, secondsd_height_end = mean_height - (2 * sd_height), mean_height + (2 * sd_height)
thirdsd_height_start, thirdsd_height_end = mean_height - (3 * sd_height), mean_height + (3 * sd_height)

firstsd_weight_start, firstsd_weight_end = mean_weight - sd_weight, mean_weight + sd_weight
secondsd_weight_start, secondsd_weight_end = mean_weight - (2 * sd_weight), mean_weight + (2 * sd_weight)
thirdsd_weight_start, thirdsd_weight_end = mean_weight - (3 * sd_weight), mean_weight + (3 * sd_weight)

height_list_firstsd = [result for result in height_list if result > firstsd_height_start and result < firstsd_height_end]
height_list_secondsd = [result for result in height_list if result > secondsd_height_start and result < secondsd_height_end]
height_list_thirdsd = [result for result in height_list if result > thirdsd_height_start and result < thirdsd_height_end]
print("{} % of data for height lies within first standard deviation".format(len(height_list_firstsd) * 100.0/len(height_list)))
print("{} % of data for height lies within second standard deviation".format(len(height_list_secondsd) * 100.0/len(height_list)))
print("{} % of data for height lies within third standard deviation".format(len(height_list_thirdsd) * 100.0/len(height_list)))

weight_list_firstsd = [result for result in weight_list if result > firstsd_weight_start and result < firstsd_weight_end]
weight_list_secondsd = [result for result in weight_list if result > secondsd_weight_start and result < secondsd_weight_end]
weight_list_thirdsd = [result for result in weight_list if result > thirdsd_weight_start and result < thirdsd_weight_end]
print("{} % of data for weight lies within first standard deviation".format(len(weight_list_firstsd) * 100.0/len(weight_list)))
print("{} % of data for weight lies within second standard deviation".format(len(weight_list_secondsd) * 100.0/len(weight_list)))
print("{} % of data for weight lies within third standard deviation".format(len(weight_list_thirdsd) * 100.0/len(weight_list)))
