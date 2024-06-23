import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the JSON data from the root directory
file_path = os.path.join(os.path.dirname(__file__), '../updated_members.json')
with open(file_path, encoding='utf-8') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Filter out rows without vote information
df_votes = df[df['vote'].notna()]

# Plot the votes
plt.figure(figsize=(10, 6))
vote_counts = df_votes['vote'].value_counts()
vote_counts.plot(kind='bar', color='skyblue')
plt.title('Votes of Members')
plt.xlabel('Vote')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Ensure the output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '../mnt/data')
os.makedirs(output_dir, exist_ok=True)

# Save the plot
output_path = os.path.join(output_dir, 'member_votes.png')
plt.savefig(output_path)

# Show the plot
plt.show()