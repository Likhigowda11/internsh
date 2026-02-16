import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
sns.histplot(df["age"], kde=True)
plt.title("age Distribution")
plt.show()


plt.figure()
sns.histplot(df["salary"], kde=True)
plt.title("salary Distribution")
plt.show()

plt.figure()
sns.histplot(x=df["salary"])
plt.title("salary boxplot")
plt.show()

plt.figure()
sns.countplot(x="department",data=df)
plt.title("department Distribution")
plt.show()




