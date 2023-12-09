import pandas as pd

# Create a DataFrame
data = {'Question': ['How many corners does a triangle have?', 'What is the variable type of a? a = "yes"', 'How many oceans are in the world?'],
        'Choice1': ['Two', 'Integer', 'Two'],
        'Choice2': ['Three', 'Float', 'Three'],
        'Choice3': ['Four', 'String', 'Four'],
        'Choice4': ['Five', 'Character', 'Five'],
        'Answer': [2, 3, 4]}

df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
csv_file_path = 'Mcqs.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved to {csv_file_path}")
