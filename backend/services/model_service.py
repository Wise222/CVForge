# -*- coding: utf-8 -*-
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch, re

class CVForgeModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.loaded = False

    def load(self):
        if self.loaded:
            return
        print("Loading CVForge model...")
        base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.tokenizer = AutoTokenizer.from_pretrained("Wise222/cvforge-model-v2")
        base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float32)
        self.model = PeftModel.from_pretrained(base_model, "Wise222/cvforge-model-v2")
        self.model.eval()
        self.loaded = True
        print("CVForge model loaded!")

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        if not self.loaded:
            self.load()
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=400)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.7,
                do_sample=True,
                repetition_penalty=1.3
            )
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        result = result.split("### Response:")[-1].strip()
        result = re.sub(r"### Instruction:.*", "", result, flags=re.DOTALL).strip()
        lines = result.split("\n")
        seen = set()
        clean = []
        for line in lines:
            s = line.strip()
            if s and s not in seen:
                seen.add(s)
                clean.append(line)
        return " ".join(clean).strip()[:500]

    def generate_summary(self, industry: str, seniority: str, years_exp: int, skills: str) -> str:
        prompt = f"### Instruction: Write a 3-sentence professional summary for a {seniority} {industry} with {years_exp} years experience. Skills: {skills}.\n### Response:"
        return self.generate(prompt, 150)

    def generate_cover_letter_body(self, name: str, role: str, company: str, industry: str, skills: str, job_title: str, job_company: str) -> str:
        prompt = f"### Instruction: Write a professional cover letter body paragraph for {name} applying for {role} at {company}. They are a {industry}. Skills: {skills}. Most recent role: {job_title} at {job_company}.\n### Response:"
        return self.generate(prompt, 300)

    def generate_reference_body(self, name: str, role: str, job_title: str, job_company: str, duties: str, skills: str) -> str:
        prompt = f"### Instruction: Write a professional reference letter body for {name} who worked as {job_title} at {job_company}. Contributions: {duties}. Skills: {skills}.\n### Response:"
        return self.generate(prompt, 300)

    def generate_linkedin(self, name: str, industry: str, seniority: str, years_exp: int, skills: str, company: str) -> str:
        prompt = f"### Instruction: Write a LinkedIn profile summary for {name}, a {seniority} {industry} with {years_exp} years experience at {company}. Skills: {skills}.\n### Response:"
        return self.generate(prompt, 200)

# Global singleton instance
cvforge_model = CVForgeModel()
