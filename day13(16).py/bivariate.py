import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
print(plt.colormaps())

sns.set(style = 'whitegrid')

data = {
    "age":[25,30,35,40,28,32,45,50,23,36,29,41],
    "salary":[30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,42000,70000],
    "experience":[1,3,7,10,2,5,15,20,1,8,4,12],
    "department":["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']}

df = pd.DataFrame(data)
print(df)

plt.figure()
sns.scatterplot(x = "age", y = "salary",data=df)
plt.title("age vs salary")
plt.show()


plt.figure()
sns.scatterplot(x = "gender", y = "salary",data=df)
plt.title("experience vs salary")
plt.show()


plt.figure()
sns.boxplot(x = "gender", y = "salary",data=df)
plt.title("salary by gender")
plt.show()


plt.figure()
sns.scatterplot(x = "department", y = "salary",data=df)
plt.title("salary by department")
plt.show()

corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix,annot=True,cmap="berlin_r")
plt.title("Correlation Heatmap")
plt.show()


plt.figure()
sns.boxplot(x=df["age"])
plt.title("age outliers")
plt.show()

#FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.


print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")
