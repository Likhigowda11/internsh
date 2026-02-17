import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = { 
    "Customer_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], 
    "Gender": ["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female"], 
    "Age": [25,32,28,45,36,23,40,29,31,27], 
    "City_Tier": [1,2,1,3,2,1,3,2,1,2], 
    "Avg_Session_Time": [15,10,18,8,12,20,7,16,14,19], 
    "Pages_Visited": [5,3,6,2,4,8,2,5,6,7], 
    "Products_Viewed": [3,2,4,1,2,5,1,3,4,4], 
    "Previous_Purchases": [2,1,3,0,1,4,0,2,3,3], 
    "Discount_Used": [1,0,1,0,1,1,0,1,1,1], 
    "Total_Spend": [1200,600,1800,300,900,2500,250,1500,2000,1700] 
} 

df = pd.DataFrame(data)

# Task 1 - Univariate Analysis
plt.figure(figsize=(6,4))
sns.histplot(df['Total_Spend'], bins=5, kde=True, color='skyblue')
plt.title('Distribution of Total Spend')
plt.xlabel('Total Spend')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(y=df['Avg_Session_Time'], color='lightgreen')
plt.title('Boxplot of Avg Session Time')
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='City_Tier', data=df, hue='City_Tier', palette='pastel', legend=False)
plt.title('Customer Count by City Tier')
plt.show()

# Task 2 - Bivariate Analysis
plt.figure(figsize=(6,4))
sns.scatterplot(x='Avg_Session_Time', y='Total_Spend', data=df, hue='Gender', s=100)
plt.title('Avg Session Time vs Total Spend')
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Pages_Visited', y='Total_Spend', data=df, hue='Gender', s=100)
plt.title('Pages Visited vs Total Spend')
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Previous_Purchases', y='Total_Spend', data=df, hue='Gender', s=100)
plt.title('Previous Purchases vs Total Spend')
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Discount_Used', y='Total_Spend', data=df, palette='Set2')
plt.title('Discount Used vs Total Spend')
plt.show()

# Task 3 - Multivariate Analysis
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Task 4 - Subplot Dashboard
fig, axs = plt.subplots(2, 2, figsize=(12,10))

sns.scatterplot(x='Avg_Session_Time', y='Total_Spend', data=df, ax=axs[0,0], color='blue')
axs[0,0].set_title('Session Time vs Total Spend')

sns.scatterplot(x='Previous_Purchases', y='Total_Spend', data=df, ax=axs[0,1], color='green')
axs[0,1].set_title('Previous Purchases vs Total Spend')

sns.boxplot(x='Discount_Used', y='Total_Spend', data=df, ax=axs[1,0], palette='Set1')
axs[1,0].set_title('Discount Used vs Total Spend')

sns.histplot(df['Total_Spend'], bins=5, kde=True, color='purple', ax=axs[1,1])
axs[1,1].set_title('Total Spend Distribution')

plt.tight_layout()
plt.show()