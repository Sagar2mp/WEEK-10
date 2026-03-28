import pandas as pd
try:
    df = pd.read_csv('smarks.csv')
    print("File loaded successfully")
except:
    data = {'name': ['Jagan', 'Saif', 'Punith', 'Mohith', 'Venky'], 
            'marks': [85, 92, 78, 95, 88], 
            'grade': ['A', 'A+', 'B+', 'A+', 'A']}
    df = pd.DataFrame(data)
    df.to_csv('smarks.csv', index=False)
    print("Sample CSV created correctly!")
print("Original Student Data:")
print(df)
print("\n" + "="*40)
print("1. Sort by Marks (Highest first):")
print(df.sort_values('marks', ascending=False))
print("\n2. Sort by Grade:")
print(df.sort_values('grade'))
print("\n" + "="*40)
print("3. Top 3 students:")
print(df.sort_values('marks', ascending=False).iloc[:3])
print("\n4. A+ students:")
aplus = df[df['grade'] == 'A+']
print(aplus if len(aplus) > 0 else "No A+ students")
print("\n5. Marks > 85:")
high = df[df['marks'] > 85]
print(high if len(high) > 0 else "No students >85")