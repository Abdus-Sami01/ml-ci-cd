import sys
import pandas as pd

if len(sys.argv) != 3:
    raise ValueError("Usage: preprocess.py <input_path> <output_path>")

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)
df = df.dropna()
df.to_csv(output_path, index=False)

print(f"Processed data saved to {output_path}")
