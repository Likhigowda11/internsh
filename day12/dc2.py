import pandas as pd
import numpy as np
import time
df = pd.read_csv("students.csv")

#TASK 1: Data Cleaning Intelligence

#Detect Missing Values
missing_summary_before = df.isnull().sum()
print("Missing Values Before Cleaning:\n", missing_summary_before)

#Replace Missing Scores with Subject-wise Mean (Vectorized)
score_columns = ["Math_Score", "Science_Score", "English_Score"]

for col in score_columns:
    df[col] = df[col].fillna(df[col].mean())


    df["Attendance_Percentage"] = df["Attendance_Percentage"].fillna(
    df["Attendance_Percentage"].mean()
)
    
# Standardize Student Names (String Operations)
    df["Name"] = df["Name"].str.strip().str.title()

# Remove Duplicate Records
    df = df.drop_duplicates()

# Missing Summary After Cleaning
missing_summary_after = df.isnull().sum()

print("Missing Values After Cleaning:\n", missing_summary_after)

# TASK 2: Risk Score Formula (Vectorized + Lambda)

#1. Create Average Score

df["Average_Score"] = df[score_columns].mean(axis=1)

#2. Boolean Masking (Vectorized Conditions)
df["Low_Marks"] = (df["Average_Score"] < 50).astype(int)
df["Low_Attendance"] = (df["Attendance_Percentage"] < 75).astype(int)
df["Low_Study"] = (df["Study_Hours_per_Week"] < 10).astype(int)
df["Low_Parent_Edu"] = (
    df["Parent_Education_Level"] == "Below High School"
).astype(int)

#3. Risk Score Calculation (Vectorized)

df["Risk_Score"] = (
    df["Low_Marks"] * 40 +
    df["Low_Attendance"] * 30 +
    df["Low_Study"] * 20 +
    df["Low_Parent_Edu"] * 10
)
#4. Risk Level Classification (Lambda Function)

df["Risk_Level"] = df["Risk_Score"].apply(
    lambda x: "Low Risk" if x <= 30
    else "Medium Risk" if x <= 60
    else "High Risk"
)

# TASK 3: Advanced Logical Insights

# 1. Which Subject Contributes Most to Failures?

failed_students = df[df["Final_Result"] == "Fail"]

subject_failure_avg = failed_students[score_columns].mean()
print(subject_failure_avg.sort_values())

#2. Are Students with Low Attendance Always Failing?

low_attendance = df[df["Attendance_Percentage"] < 75]

low_attendance["Final_Result"].value_counts()    #If some students passed → Answer is NO.

# 3. Any High Risk Student Who Still Passed?

df[(df["Risk_Level"] == "High Risk") & (df["Final_Result"] == "Pass")]

#4. Average Study Hours of High Risk Students

df[df["Risk_Level"] == "High Risk"]["Study_Hours_per_Week"].mean()

#5. Correlation Matrix

corr_matrix = df[
    ["Math_Score", "Science_Score", "English_Score",
     "Attendance_Percentage", "Study_Hours_per_Week",
     "Risk_Score"]
].corr()

print(corr_matrix)

#TASK 4: Performance Challenge

#Vectorized Version Timing
start = time.time()

df["Risk_Vectorized"] = (
    ((df["Average_Score"] < 50).astype(int) * 40) +
    ((df["Attendance_Percentage"] < 75).astype(int) * 30) +
    ((df["Study_Hours_per_Week"] < 10).astype(int) * 20) +
    ((df["Parent_Education_Level"] == "Below High School").astype(int) * 10)
)

end = time.time()
print("Vectorized Time:", end - start)

# Loop Version (For Comparison Only)

start = time.time()

risk_scores = []

for _, row in df.iterrows():
    score = 0
    if row["Average_Score"] < 50:
        score += 40
    if row["Attendance_Percentage"] < 75:
        score += 30
    if row["Study_Hours_per_Week"] < 10:
        score += 20
    if row["Parent_Education_Level"] == "Below High School":
        score += 10
    risk_scores.append(score)

df["Risk_Loop"] = risk_scores

end = time.time()
print("Loop Time:", end - start)