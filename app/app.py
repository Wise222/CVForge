# -*- coding: utf-8 -*-
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch, re
from fpdf import FPDF
import tempfile, os

print("Loading CVForge model...")
base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained("Wise222/cvforge-model-v2")
base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float32)
model = PeftModel.from_pretrained(base_model, "Wise222/cvforge-model-v2")
model.eval()
print("CVForge ready!")

def clean_output(text):
    text = text.split("### Response:")[-1].strip()
    text = re.sub(r'### Instruction:.*', '', text, flags=re.DOTALL)
    lines = text.split("\n")
    seen = set()
    clean = []
    for line in lines:
        stripped = line.strip()
        if stripped and stripped not in seen:
            seen.add(stripped)
            clean.append(line)
    return "\n".join(clean[:80]).strip()

def generate_document(doc_type, full_name, email, phone, location, nationality,
                      industry, seniority, years_exp, skills, languages,
                      job1_title, job1_company, job1_dates, job1_duties,
                      job2_title, job2_company, job2_dates, job2_duties,
                      degree, university, grad_year, extra_cert,
                      target_role, target_company, hobbies, template):

    if not full_name:
        return "Please enter your full name to get started.", None

    if doc_type == "Professional CV":
        prompt = f"""### Instruction: Write a highly professional ATS-optimized CV.
Name: {full_name} | Email: {email} | Phone: {phone} | Location: {location} | Nationality: {nationality}
Target Role: {target_role} at {target_company}
Industry: {industry} | Level: {seniority} | Experience: {years_exp} years
Skills: {skills}
Languages: {languages}
Experience 1: {job1_title} at {job1_company} ({job1_dates}) - {job1_duties}
Experience 2: {job2_title} at {job2_company} ({job2_dates}) - {job2_duties}
Education: {degree}, {university}, {grad_year}
Certifications: {extra_cert}
Interests: {hobbies}
### Response:"""

    elif doc_type == "Cover Letter":
        prompt = f"""### Instruction: Write a compelling cover letter for {full_name} applying for {target_role} at {target_company}. Industry: {industry}. Skills: {skills}. Most recent role: {job1_title} at {job1_company}.
### Response:"""

    elif doc_type == "LinkedIn Summary":
        prompt = f"""### Instruction: Write a powerful LinkedIn profile summary for {full_name}, a {seniority} {industry} with {years_exp} years experience. Skills: {skills}. Current company: {job1_company}.
### Response:"""

    elif doc_type == "Reference Letter":
        prompt = f"""### Instruction: Write a professional reference letter for {full_name} who worked as {job1_title} at {job1_company}. Duties: {job1_duties}. Skills: {skills}.
### Response:"""

    else:
        prompt = f"""### Instruction: Write a professional resignation letter for {full_name} resigning from {job1_title} at {job1_company} to pursue {target_role} at {target_company}.
### Response:"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=600)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=600, temperature=0.7,
                                  do_sample=True, repetition_penalty=1.3)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    text = clean_output(result)

    pdf_path = create_pdf(text, full_name, template, doc_type)
    return text, pdf_path

def create_pdf(text, name, template, doc_type):
    pdf = FPDF()
    pdf.add_page()

    if template == "Classic Professional":
        pdf.set_fill_color(255, 255, 255)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 12, name, ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_draw_color(0, 0, 0)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    elif template == "Modern Blue":
        pdf.set_fill_color(30, 58, 138)
        pdf.rect(0, 0, 210, 40, "F")
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "B", 22)
        pdf.set_y(12)
        pdf.cell(0, 10, name, ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 6, doc_type, ln=True, align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_y(48)

    elif template == "Executive Gold":
        pdf.set_fill_color(20, 20, 20)
        pdf.rect(0, 0, 210, 45, "F")
        pdf.set_fill_color(218, 165, 32)
        pdf.rect(0, 42, 210, 3, "F")
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Helvetica", "B", 24)
        pdf.set_y(12)
        pdf.cell(0, 10, name, ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(200, 200, 200)
        pdf.cell(0, 6, doc_type, ln=True, align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_y(52)

    elif template == "African Heritage":
        pdf.set_fill_color(139, 0, 0)
        pdf.rect(0, 0, 210, 8, "F")
        pdf.set_fill_color(0, 100, 0)
        pdf.rect(0, 8, 210, 8, "F")
        pdf.set_fill_color(255, 165, 0)
        pdf.rect(0, 16, 210, 8, "F")
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(0, 24, 210, 8, "F")
        pdf.set_text_color(0, 0, 0)
        pdf.set_y(38)
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 10, name, ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_draw_color(139, 0, 0)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    elif template == "Minimalist":
        pdf.set_text_color(50, 50, 50)
        pdf.set_font("Helvetica", "B", 18)
        pdf.set_y(15)
        pdf.cell(0, 10, name, ln=True)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(0, 5, doc_type, ln=True)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y()+2, 200, pdf.get_y()+2)
        pdf.ln(8)
        pdf.set_text_color(50, 50, 50)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            pdf.ln(3)
        elif line.isupper() or (len(line) < 40 and line.endswith(":")):
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(30, 30, 120) if template == "Modern Blue" else pdf.set_text_color(0,0,0)
            pdf.ln(2)
            pdf.cell(0, 7, line, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 30)
        else:
            pdf.multi_cell(0, 6, line)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", prefix=f"CVForge_{name.replace(' ','_')}_")
    pdf.output(tmp.name)
    return tmp.name

css = """
* { box-sizing: border-box; }
.gradio-container {
    background: #0f0f1a !important;
    font-family: 'Segoe UI', system-ui, sans-serif !important;
    max-width: 100% !important;
    padding: 0 !important;
}
.main-header {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a3e 100%);
    padding: 32px 20px 20px 20px;
    text-align: center;
    border-bottom: 1px solid #2d2d5e;
}
.section-card {
    background: #13131f;
    border: 1px solid #2d2d5e;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}
.section-title {
    color: #fbbf24;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #2d2d5e;
}
label { color: #d1d5db !important; font-size: 13px !important; font-weight: 500 !important; }
input, textarea, select {
    background: #1e1e35 !important;
    color: #f9fafb !important;
    border: 1px solid #374151 !important;
    border-radius: 8px !important;
    font-size: 13px !important;
}
input:focus, textarea:focus {
    border-color: #6366f1 !important;
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(99,102,241,0.2) !important;
}
.generate-btn {
    background: linear-gradient(90deg, #f59e0b, #ef4444) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    border-radius: 12px !important;
    padding: 16px !important;
    border: none !important;
    width: 100% !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}
.generate-btn:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(239,68,68,0.4) !important;
}
.output-area textarea {
    background: #0a0a14 !important;
    color: #e2e8f0 !important;
    border: 1px solid #374151 !important;
    font-family: 'Courier New', monospace !important;
    font-size: 13px !important;
    line-height: 1.7 !important;
    border-radius: 12px !important;
}
.tag {
    display: inline-block;
    background: rgba(99,102,241,0.15);
    color: #818cf8;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    margin: 2px;
    border: 1px solid rgba(99,102,241,0.3);
}
"""

with gr.Blocks(title="CVForge Pro", css=css) as app:

    gr.HTML("""
    <div class='main-header'>
        <div style='font-size:48px; font-weight:900; background:linear-gradient(90deg,#f59e0b,#ef4444,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent; line-height:1.1;'>
            CVForge Pro
        </div>
        <div style='color:#9ca3af; font-size:15px; margin-top:8px; font-weight:400;'>
            Africa's Most Advanced AI Career Document Builder
        </div>
        <div style='margin-top:14px;'>
            <span class='tag'>Professional CVs</span>
            <span class='tag'>Cover Letters</span>
            <span class='tag'>LinkedIn Profiles</span>
            <span class='tag'>Reference Letters</span>
            <span class='tag'>PDF Export</span>
            <span class='tag'>5 Premium Templates</span>
        </div>
        <div style='color:#6b7280; font-size:12px; margin-top:12px;'>
            Trusted by job seekers across Zambia, Kenya, Nigeria, Ghana, South Africa and beyond
        </div>
    </div>
    """)

    with gr.Row(equal_height=False):

        with gr.Column(scale=1, min_width=400):

            with gr.Group():
                gr.HTML("<div class='section-title'>Document Type & Template</div>")
                doc_type = gr.Radio(
                    ["Professional CV", "Cover Letter", "LinkedIn Summary", "Reference Letter", "Resignation Letter"],
                    value="Professional CV", label="What would you like to create?"
                )
                template = gr.Radio(
                    ["Classic Professional", "Modern Blue", "Executive Gold", "African Heritage", "Minimalist"],
                    value="Modern Blue", label="Choose PDF Template"
                )

            with gr.Group():
                gr.HTML("<div class='section-title'>Personal Information</div>")
                full_name = gr.Textbox(label="Full Name *", placeholder="e.g. Grace Tembo")
                with gr.Row():
                    email = gr.Textbox(label="Email Address", placeholder="grace@email.com")
                    phone = gr.Textbox(label="Phone Number", placeholder="+260 97 000 0000")
                with gr.Row():
                    location = gr.Textbox(label="City & Country", placeholder="Lusaka, Zambia")
                    nationality = gr.Textbox(label="Nationality", placeholder="Zambian")

            with gr.Group():
                gr.HTML("<div class='section-title'>Career Profile</div>")
                industry = gr.Dropdown([
                    "Software Developer", "Data Scientist", "Cybersecurity Analyst", "IT Support Officer",
                    "HR Manager", "Recruitment Specialist", "Training Officer",
                    "Accountant", "Finance Analyst", "Auditor", "Banking Officer", "Investment Analyst",
                    "Marketing Manager", "Brand Manager", "Digital Marketing Specialist",
                    "Sales Manager", "Business Development Officer", "Account Manager",
                    "Civil Engineer", "Electrical Engineer", "Mechanical Engineer", "Mining Engineer",
                    "Nurse", "Doctor", "Pharmacist", "Public Health Officer", "Lab Technician",
                    "Teacher", "University Lecturer", "Education Officer", "School Administrator",
                    "Lawyer", "Legal Officer", "Compliance Officer", "Paralegal",
                    "Project Manager", "Operations Manager", "Supply Chain Manager", "Logistics Officer",
                    "Graphic Designer", "UI/UX Designer", "Architect", "Interior Designer",
                    "Journalist", "Communications Officer", "Public Relations Officer", "Content Creator",
                    "NGO Program Officer", "Community Development Officer", "Social Worker", "Field Officer",
                    "Agricultural Officer", "Environmental Officer", "Food Security Specialist",
                    "Chef", "Hospitality Manager", "Tourism Officer", "Events Coordinator",
                    "Telecoms Engineer", "Network Administrator", "Systems Administrator"
                ], label="Industry / Profession *")
                with gr.Row():
                    seniority = gr.Dropdown([
                        "Internship / Attachment",
                        "Entry Level (0-2 years)",
                        "Junior Professional (2-4 years)",
                        "Mid-Level Professional (4-7 years)",
                        "Senior Professional (7-12 years)",
                        "Manager / Team Lead",
                        "Senior Manager / Director",
                        "C-Suite / Executive"
                    ], label="Career Level *")
                    years_exp = gr.Slider(0, 35, value=3, step=1, label="Years of Experience")
                skills = gr.Textbox(
                    label="Key Skills (separate with commas)",
                    placeholder="e.g. Financial Reporting, Excel, SAP, Team Leadership, Budgeting, Communication",
                    lines=2
                )
                languages = gr.Textbox(
                    label="Languages",
                    placeholder="e.g. English (Fluent), French (Intermediate), Nyanja (Native)"
                )

            with gr.Group():
                gr.HTML("<div class='section-title'>Work Experience</div>")
                gr.HTML("<div style='color:#9ca3af; font-size:12px; margin-bottom:10px;'>Most Recent Position</div>")
                with gr.Row():
                    job1_title = gr.Textbox(label="Job Title", placeholder="e.g. Senior Finance Officer")
                    job1_company = gr.Textbox(label="Company / Organization", placeholder="e.g. Zambia Revenue Authority")
                job1_dates = gr.Textbox(label="Period", placeholder="e.g. March 2021 - Present")
                job1_duties = gr.Textbox(
                    label="Key Achievements & Responsibilities",
                    placeholder="e.g. Managed ZMW 50M annual budget, reduced expenditure by 18%, supervised team of 8 staff, prepared monthly financial statements for board review...",
                    lines=3
                )
                gr.HTML("<div style='color:#9ca3af; font-size:12px; margin:10px 0;'>Previous Position</div>")
                with gr.Row():
                    job2_title = gr.Textbox(label="Job Title", placeholder="e.g. Finance Officer")
                    job2_company = gr.Textbox(label="Company / Organization", placeholder="e.g. Deloitte Zambia")
                job2_dates = gr.Textbox(label="Period", placeholder="e.g. June 2018 - February 2021")
                job2_duties = gr.Textbox(
                    label="Key Responsibilities",
                    placeholder="e.g. Prepared tax returns, assisted with annual audits, maintained ledgers...",
                    lines=2
                )

            with gr.Group():
                gr.HTML("<div class='section-title'>Education & Qualifications</div>")
                with gr.Row():
                    degree = gr.Textbox(label="Highest Qualification", placeholder="e.g. Bachelor of Accountancy (Honours)")
                    university = gr.Textbox(label="Institution", placeholder="e.g. University of Zambia")
                with gr.Row():
                    grad_year = gr.Textbox(label="Year Graduated", placeholder="e.g. 2018")
                    extra_cert = gr.Textbox(label="Certifications / Memberships", placeholder="e.g. ACCA Part III, ZICA Member, CFA Level 1")

            with gr.Group():
                gr.HTML("<div class='section-title'>Target Application</div>")
                with gr.Row():
                    target_role = gr.Textbox(label="Position Applying For", placeholder="e.g. Finance Manager")
                    target_company = gr.Textbox(label="Company Applying To", placeholder="e.g. MTN Zambia")
                hobbies = gr.Textbox(
                    label="Interests & Community Involvement (optional)",
                    placeholder="e.g. Youth mentoring, financial literacy workshops, reading, marathon running"
                )

            btn = gr.Button("Generate My Document", variant="primary", elem_classes=["generate-btn"])

        with gr.Column(scale=1, min_width=400):
            gr.HTML("""
            <div style='background:#13131f; border:1px solid #2d2d5e; border-radius:12px; padding:16px; margin-bottom:12px;'>
                <div style='color:#fbbf24; font-size:11px; font-weight:800; letter-spacing:2px; margin-bottom:10px;'>YOUR GENERATED DOCUMENT</div>
                <div style='color:#6b7280; font-size:12px;'>Fill in your details on the left and click Generate. Your professional document will appear here instantly.</div>
            </div>
            """)
            output = gr.Textbox(
                label="",
                lines=40,
                placeholder="Your document will appear here...",
                elem_classes=["output-area"]
            )
            pdf_output = gr.File(label="Download as PDF", visible=True)

            gr.HTML("""
            <div style='background:#13131f; border:1px solid #2d2d5e; border-radius:12px; padding:16px; margin-top:12px;'>
                <div style='color:#fbbf24; font-size:11px; font-weight:800; letter-spacing:2px; margin-bottom:12px;'>PRO TIPS FOR A WINNING CV</div>
                <div style='color:#9ca3af; font-size:12px; line-height:2;'>
                    Use numbers — "Increased sales by 35%" beats "Improved sales"<br>
                    Tailor skills to match the job description keywords<br>
                    Keep achievements specific — what did YOU do and what was the result?<br>
                    List certifications relevant to the role you are applying for<br>
                    Download the PDF and review before sending to employers
                </div>
            </div>
            <div style='margin-top:16px; background:#13131f; border:1px solid #2d2d5e; border-radius:12px; padding:16px;'>
                <div style='color:#fbbf24; font-size:11px; font-weight:800; letter-spacing:2px; margin-bottom:12px;'>PDF TEMPLATES</div>
                <div style='display:grid; grid-template-columns:1fr 1fr; gap:8px;'>
                    <div style='background:#1e1e35; padding:10px; border-radius:8px; border-left:3px solid #6366f1;'>
                        <div style='color:#e2e8f0; font-size:12px; font-weight:700;'>Classic Professional</div>
                        <div style='color:#6b7280; font-size:11px;'>Clean black & white</div>
                    </div>
                    <div style='background:#1e1e35; padding:10px; border-radius:8px; border-left:3px solid #3b82f6;'>
                        <div style='color:#e2e8f0; font-size:12px; font-weight:700;'>Modern Blue</div>
                        <div style='color:#6b7280; font-size:11px;'>Corporate & bold</div>
                    </div>
                    <div style='background:#1e1e35; padding:10px; border-radius:8px; border-left:3px solid #f59e0b;'>
                        <div style='color:#e2e8f0; font-size:12px; font-weight:700;'>Executive Gold</div>
                        <div style='color:#6b7280; font-size:11px;'>Premium dark theme</div>
                    </div>
                    <div style='background:#1e1e35; padding:10px; border-radius:8px; border-left:3px solid #16a34a;'>
                        <div style='color:#e2e8f0; font-size:12px; font-weight:700;'>African Heritage</div>
                        <div style='color:#6b7280; font-size:11px;'>Pan-African colors</div>
                    </div>
                    <div style='background:#1e1e35; padding:10px; border-radius:8px; border-left:3px solid #9ca3af;'>
                        <div style='color:#e2e8f0; font-size:12px; font-weight:700;'>Minimalist</div>
                        <div style='color:#6b7280; font-size:11px;'>Clean & simple</div>
                    </div>
                </div>
            </div>
            <div style='text-align:center; color:#374151; font-size:11px; margin-top:16px; padding-bottom:20px;'>
                CVForge Pro v2.0 — Free Forever — Built for Africa
            </div>
            """)

    btn.click(
        generate_document,
        inputs=[doc_type, full_name, email, phone, location, nationality,
                industry, seniority, years_exp, skills, languages,
                job1_title, job1_company, job1_dates, job1_duties,
                job2_title, job2_company, job2_dates, job2_duties,
                degree, university, grad_year, extra_cert,
                target_role, target_company, hobbies, template],
        outputs=[output, pdf_output]
    )

app.launch(share=True)
