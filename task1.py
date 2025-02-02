import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample Data
ages = np.random.normal(loc=30, scale=10, size=1000)  # Normally distributed ages
genders = np.random.choice(['Male', 'Female', 'Other'], size=1000, p=[0.48, 0.48, 0.04])

# Plotting the Histogram for Age Distribution
plt.figure(figsize=(10, 5))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Plotting the Bar Chart for Gender Distribution
plt.figure(figsize=(8, 5))
gender_counts = {gender: list(genders).count(gender) for gender in set(genders)}
sns.barplot(x=list(gender_counts.keys()), y=list(gender_counts.values()), palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
