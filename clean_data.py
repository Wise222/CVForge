import pandas as pd, re, os

print("Loading datasets...")
df1 = pd.read_csv("data/raw/Resume/Resume.csv")[["Resume_str","Category"]].rename(columns={"Resume_str":"Resume"})
df2 = pd.read_csv("data/raw/final_merged_dataset2.csv")[["Resume","Category"]]
df3 = pd.read_csv("data/raw/UpdatedResumeDataSet.csv")[["Resume","Category"]]

df = pd.concat([df1,df2,df3], ignore_index=True)
print(f"Total before cleaning: {len(df)}")

df.dropna(inplace=True)
df["Resume"] = df["Resume"].apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip())
df = df[df["Resume"].str.len() > 200]
df.drop_duplicates(subset="Resume", inplace=True)
df.reset_index(drop=True, inplace=True)

os.makedirs("data/cleaned", exist_ok=True)
df.to_csv("data/cleaned/cleaned_resumes.csv", index=False)
print(f"Total after cleaning: {len(df)}")
print(f"Categories: {df['Category'].nunique()}")
print(df["Category"].value_counts())
print("Saved to data/cleaned/cleaned_resumes.csv")
