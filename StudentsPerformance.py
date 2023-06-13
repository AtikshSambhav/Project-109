import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
students_list = df["StudentsPerformance"].to_list()

#Mean for Students Performance
StudentsPerformance_mean = statistics.mean(StudentsPerformance_list) 

#Median for Students Performance
StudentsPerformance_median = statistics.median(StudentsPerformance_list)

#Mode for Stuents Performance
StudentsPerformance_mode = statistics.mode(StudentsPerformance_list)

#Printing Mean, Media and Mode to continue
print("Mean, Median and Mode of StudentsPerformance is {} ,{} and {} respictvely".format(StudentsPerformance_mean, StudentsPerformance_median, StudentsPerformance_mode))

#Standard Deviation for Students Performance
StudentsPerformance_std_deviation = statistics.stdev(StudentsPerformance_list)

#1, 2 and 3 Standard Deviation for Students Performance
StudentsPerformance_first_std_deviation_start, StudentsPerformance_first_std_deviation_end = StudentsPerformance_mean-StudentsPerformance_std_deviation, StudentsPerformance_mean+Students Performance_std_deviation
StudentsPerformance_second_std_deviation_start, StudentsPerformance_second_std_deviation_end = StudentsPerformance_mean-(2*height_std_deviaion), StudentsPerformance_mean+(2*StudentsPerformance_std_deviation)
StudentsPerformance_third_std_deviation_start, StudentsPerformance_third_std_deviation_end = StudentsPerformance_mean-(3*StudentsPerformance_std_deviation), StudentsPerformance_mean+(3*StudentsPerformance_std_deviation)

#Percentage of data within 1, 2 and third standard deviation
StudentsPerformance_list_of_data_within_first_std_deviation = [result for result in StudentsPerformance_list if result > StudentsPerformance_first_std_deviation_start and result < StudentsPerformance_first_standard_deviation_end]  
StudentsPerformance_list_of_data_within_2_std_deviation = [result for result in StudentsPerformance_list if result > StudentsPerformance_second_std_deviation_start and result < StudentsPerformance_second_std_deviation_end]
StudentsPerformance_list_of_data_within_3_std_deviation = [result for result in StudentsPerformance_list if result > StudentsPerformance_third_std_deviation_start and result < StudentsPerformance_third_std_deviation_end]

#Priinting Data for Students Performance (STANDARD DEVIATION)
print("{}% of data for StudentsPerformance lies within 1 standard deviation".format(len(StudentsPerformance_list_of_data_within_1_std_deviation)*100.0/len(StudentsPerformance_list)))
print("{}% of data for StudentsPerformance lies within 2 standard deviations".format(len(StudentsPerformance_list_of_data_within_2_std_deviation)*100.0/len(StudentsPerformance_list)))
print("{}% of data for StudentsPerformance lies within 3 standard deviations".format(len(StudentsPerformance_list_of_data_within_3_std_deviation)*100.0/len(StudentsPerformance_list)))




























