
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