import pandas as pd, json, os

df = pd.read_csv("data/cleaned/cleaned_resumes.csv")
pairs = []
for _, row in df.iterrows():
    pair = {
        "prompt": f"Write a professional CV for a {row['Category']} position.",
        "response": str(row["Resume"])
    }
    pairs.append(pair)

os.makedirs("data/pairs", exist_ok=True)
with open("data/pairs/training_pairs.jsonl", "w", encoding="utf-8") as f:
    for pair in pairs:
        f.write(json.dumps(pair) + "\n")

print(f"Created {len(pairs)} training pairs")
print("Saved to data/pairs/training_pairs.jsonl")
