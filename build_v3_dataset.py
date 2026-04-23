import pandas as pd, json, os

print("Loading new resume data...")
df = pd.read_csv("data/raw/resume_data.csv", on_bad_lines="skip")
df = df.fillna("")

pairs = []
for _, row in df.iterrows():
    industry = str(row.get("\ufeffjob_position_name", "Professional"))
    skills = str(row.get("skills", ""))
    objective = str(row.get("career_objective", ""))
    experience = str(row.get("responsibilities", ""))
    education = str(row.get("degree_names", ""))
    languages = str(row.get("languages", ""))
    certifications = str(row.get("certification_skills", ""))

    cv = f"""PROFESSIONAL SUMMARY
{objective}

CORE SKILLS
{skills}

WORK EXPERIENCE
{experience}

EDUCATION
{education}

LANGUAGES
{languages}

CERTIFICATIONS
{certifications}"""

    if len(cv.strip()) > 200:
        pairs.append({
            "prompt": f"Write a professional CV for a {industry} position.",
            "response": cv.strip()
        })

print(f"Generated {len(pairs)} pairs from new dataset")

existing = []
with open("data/pairs/training_pairs_v2.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        existing.append(json.loads(line))

import random
all_pairs = existing + pairs
random.shuffle(all_pairs)

with open("data/pairs/training_pairs_v3.jsonl", "w", encoding="utf-8") as f:
    for pair in all_pairs:
        f.write(json.dumps(pair) + "\n")

print(f"Previous dataset: {len(existing)}")
print(f"New examples added: {len(pairs)}")
print(f"TOTAL V3 DATASET: {len(all_pairs)} training examples")
print("Saved to data/pairs/training_pairs_v3.jsonl")
