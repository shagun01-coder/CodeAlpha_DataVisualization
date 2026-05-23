import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    'Students': ['Aman', 'Riya', 'Shagun', 'Rahul', 'Priya'],
    'Marks': [78, 85, 92, 67, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create bar chart
plt.bar(df['Students'], df['Marks'])

# Labels
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks Visualization')

# Show graph
plt.show()