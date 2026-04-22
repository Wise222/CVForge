import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
import torch

print("Loading CVForge model...")
base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained("Wise222/cvforge-model")
base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float32)
model = PeftModel.from_pretrained(base_model, "Wise222/cvforge-model")
model.eval()
print("CVForge ready!")

def generate_cv(name, email, phone, location, industry, years_exp, skills, experience, education):
    prompt = f"### Instruction: Write a professional CV for a {industry} position for {name} with {years_exp} years experience. Skills: {skills}. Experience: {experience}. Education: {education}. Contact: {email}, {phone}, {location}.\n### Response:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=400, temperature=0.7, do_sample=True)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result.split("### Response:")[-1].strip()

with gr.Blocks(title="CVForge") as app:
    gr.Markdown("# CVForge\n### Professional CVs for Everyone - Free, AI-Powered")
    with gr.Row():
        with gr.Column():
            name = gr.Textbox(label="Full Name", placeholder="John Banda")
            email = gr.Textbox(label="Email", placeholder="john@email.com")
            phone = gr.Textbox(label="Phone", placeholder="+260 97 123 4567")
            location = gr.Textbox(label="Location", placeholder="Lusaka, Zambia")
            industry = gr.Dropdown(["Software Developer","HR","Accountant","Teacher","Engineer","Sales","Marketing","Healthcare","Finance","Designer","Banking","Agriculture","Mining","Telecoms","Government","NGO Worker"], label="Industry")
            years_exp = gr.Slider(0, 30, value=2, step=1, label="Years of Experience")
            skills = gr.Textbox(label="Skills", placeholder="Python, Excel, Communication...", lines=2)
            experience = gr.Textbox(label="Work Experience", lines=3, placeholder="Company, role, achievements...")
            education = gr.Textbox(label="Education", placeholder="Degree, University, Year")
            btn = gr.Button("Generate My CV", variant="primary")
        with gr.Column():
            output = gr.Textbox(label="Your Professional CV", lines=30)
    btn.click(generate_cv, inputs=[name,email,phone,location,industry,years_exp,skills,experience,education], outputs=output)
    gr.Markdown("*CVForge - Built for Africa, Free Forever*")

app.launch(share=True)
