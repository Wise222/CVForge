import json, random, pandas as pd

industries = ["Software Developer","HR Manager","Accountant","Teacher","Civil Engineer","Sales Manager","Marketing Manager","Nurse","Finance Analyst","Graphic Designer","Banking Officer","Agricultural Officer","Mining Engineer","Telecoms Engineer","NGO Worker","Project Manager","Lawyer","Architect","Journalist","Electrician","Mechanic","Pharmacist","Data Scientist","Business Analyst","Supply Chain Manager","Logistics Officer","Public Relations Officer","Social Worker","Security Officer","Chef"]

companies = ["ABC Technologies","XYZ Corporation","Global Solutions Ltd","Africa Tech Industries","Sunrise Mining","Pioneer Group","Excel Financial Services","Summit Healthcare","Horizon Telecoms","Pinnacle Consulting","Zambia National Bank","Kenya Power","Nigeria LNG","Ghana Cocoa Board","MTN Africa","Airtel Networks","Standard Chartered","Deloitte Africa","PwC East Africa","UNICEF","WHO Africa","World Bank Group","African Development Bank"]

first_names = ["James","Grace","Peter","Mary","John","Sarah","David","Ruth","Moses","Alice","Emmanuel","Fatima","Michael","Amara","Chioma","Kwame","Aisha","Ibrahim","Blessing","Chidi","Nkechi","Seun","Tunde","Yemi","Kofi","Abena","Kweku","Ama","Kojo","Efua","Tendai","Rudo","Tatenda","Farai","Simba","Thabo","Lerato","Mpho","Kagiso","Palesa"]

last_names = ["Mwale","Banda","Phiri","Tembo","Mulenga","Zulu","Lungu","Mutale","Chanda","Sichone","Osei","Diallo","Onyeka","Mensah","Nwosu","Asante","Owusu","Darko","Boateng","Acheampong","Moyo","Dube","Ncube","Ndlovu","Sibanda","Nkosi","Dlamini","Mthembu","Khumalo","Zwane"]

skills_pool = {
    "Software Developer": "Python, Java, JavaScript, React, Node.js, SQL, Git, Agile",
    "HR Manager": "Recruitment, Payroll, Employee Relations, HRIS, Training, Performance Management",
    "Accountant": "Financial Reporting, Tax Compliance, Budgeting, QuickBooks, Excel, Auditing",
    "Teacher": "Curriculum Development, Classroom Management, Assessment, Microsoft Office, Communication",
    "Civil Engineer": "AutoCAD, Project Management, Structural Analysis, Site Supervision, Surveying",
    "Sales Manager": "Sales Strategy, CRM, Negotiation, Team Leadership, Market Analysis, Forecasting",
    "Marketing Manager": "Digital Marketing, SEO, Social Media, Brand Management, Google Analytics, Campaigns",
    "Nurse": "Patient Care, Clinical Assessment, IV Administration, Electronic Health Records, Triage",
    "Finance Analyst": "Financial Modeling, Excel, Bloomberg, Risk Analysis, Investment Analysis, Reporting",
    "Graphic Designer": "Adobe Photoshop, Illustrator, InDesign, CorelDraw, UI/UX, Branding",
    "Banking Officer": "Credit Analysis, Loan Processing, Customer Service, KYC, Anti-Money Laundering",
    "Data Scientist": "Python, R, Machine Learning, TensorFlow, SQL, Tableau, Statistics",
    "Business Analyst": "Requirements Gathering, Process Mapping, SQL, Stakeholder Management, Agile",
    "Project Manager": "PMP, Agile, Risk Management, Budgeting, MS Project, Team Leadership",
    "Lawyer": "Legal Research, Contract Drafting, Litigation, Corporate Law, Compliance",
    "Architect": "AutoCAD, Revit, SketchUp, Project Management, Urban Planning, 3D Modeling",
    "Pharmacist": "Drug Dispensing, Clinical Pharmacy, Patient Counseling, Inventory Management",
    "Journalist": "Investigative Reporting, Content Writing, Video Production, Social Media, Editing",
    "Chef": "Menu Planning, Food Safety, Kitchen Management, Catering, International Cuisine",
    "NGO Worker": "Project Management, Fundraising, Community Development, Report Writing, M&E"
}

pairs = []

# 1. GENERATE DETAILED CVs
print("Generating detailed CVs...")
for i in range(3000):
    industry = random.choice(industries)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    name = f"{fname} {lname}"
    years = random.randint(1, 20)
    skills = skills_pool.get(industry, "Communication, Leadership, Teamwork, Microsoft Office")
    company1 = random.choice(companies)
    company2 = random.choice(companies)
    
    cv = f"""{name}
Email: {fname.lower()}.{lname.lower()}@email.com | Phone: +{random.randint(1,9)}{random.randint(10,99)} {random.randint(100,999)} {random.randint(1000,9999)}

PROFESSIONAL SUMMARY
Dedicated and results-driven {industry} with {years} years of progressive experience delivering exceptional results. Proven track record of exceeding targets and driving organizational growth through innovative solutions and strong leadership.

CORE SKILLS
{skills}

WORK EXPERIENCE

{industry} | {company1} | {random.randint(2015,2022)} - Present
- Led cross-functional teams to deliver projects on time and within budget
- Improved operational efficiency by {random.randint(15,45)}% through process optimization
- Developed and implemented strategies that increased revenue by {random.randint(10,30)}%
- Mentored junior staff and conducted performance evaluations
- Collaborated with stakeholders to align departmental goals with organizational objectives

Junior {industry} | {company2} | {random.randint(2010,2015)} - {random.randint(2015,2020)}
- Supported senior team members in daily operations and project delivery
- Maintained accurate records and prepared detailed reports for management
- Participated in client meetings and contributed to business development activities
- Achieved {random.randint(90,100)}% customer satisfaction rating

EDUCATION
Bachelor of Science in {industry.split()[0]} | University of {random.choice(['Zambia','Nairobi','Ghana','Lagos','Cape Town','Johannesburg','Dar es Salaam','Accra','Abuja','Cairo'])} | {random.randint(2005,2018)}

CERTIFICATIONS
- Professional Certificate in {industry} | {random.randint(2018,2024)}
- {random.choice(['PMP','ACCA','CFA','CIMA','CISSP','AWS','Google Analytics','HubSpot','Salesforce'])} Certified

LANGUAGES
English (Fluent), {random.choice(['French','Swahili','Arabic','Portuguese','Hausa','Yoruba','Zulu','Amharic'])} ({random.choice(['Basic','Intermediate','Fluent'])})"""

    pairs.append({
        "prompt": f"Write a professional CV for a {industry} with {years} years of experience.",
        "response": cv
    })

# 2. GENERATE COVER LETTERS
print("Generating cover letters...")
for i in range(2000):
    industry = random.choice(industries)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    name = f"{fname} {lname}"
    company = random.choice(companies)
    years = random.randint(1, 15)
    skills = skills_pool.get(industry, "Communication, Leadership, Problem-solving")

    cover_letter = f"""Dear Hiring Manager,

I am writing to express my enthusiastic interest in the {industry} position at {company}. Having spent {years} years building expertise in {industry.lower()}, I am excited about the opportunity to bring my skills and dedication to your esteemed organization.

Throughout my career, I have developed strong competencies in {skills}. My professional journey has equipped me with the ability to deliver results consistently while working effectively in diverse team environments. I am particularly drawn to {company} because of its commitment to excellence, innovation, and positive impact.

In my previous roles, I have successfully led initiatives that improved efficiency and drove measurable outcomes. I am known for my analytical thinking, attention to detail, and ability to communicate complex ideas clearly to both technical and non-technical stakeholders.

I am confident that my background in {industry.lower()}, combined with my passion for continuous learning, makes me a strong fit for this role. I would welcome the opportunity to discuss how my experience aligns with {company}'s goals and vision.

Thank you for your time and consideration. I look forward to the possibility of contributing to your team.

Yours sincerely,
{name}
{fname.lower()}.{lname.lower()}@email.com
+{random.randint(1,9)}{random.randint(10,99)} {random.randint(100,999)} {random.randint(1000,9999)}"""

    pairs.append({
        "prompt": f"Write a professional cover letter for a {industry} position at {company}.",
        "response": cover_letter
    })

# 3. GENERATE BUSINESS LETTERHEADS
print("Generating business letters...")
subjects = [
    "Business Proposal and Partnership Opportunity",
    "Request for Quotation",
    "Employment Confirmation Letter",
    "Reference Letter",
    "Salary Increment Request",
    "Project Completion Report",
    "Service Agreement Renewal",
    "Official Complaint Letter",
    "Job Offer Letter",
    "Recommendation Letter"
]

for i in range(1000):
    company_name = random.choice(companies)
    sender = f"{random.choice(first_names)} {random.choice(last_names)}"
    recipient = f"{random.choice(first_names)} {random.choice(last_names)}"
    subject = random.choice(subjects)
    industry = random.choice(industries)

    letter = f"""{company_name}
123 Business Avenue, City Centre
Tel: +{random.randint(1,9)}{random.randint(10,99)} {random.randint(100,999)} {random.randint(1000,9999)} | Email: info@company.com
Website: www.company.com

{random.randint(1,28)} {random.choice(['January','February','March','April','May','June','July','August','September','October','November','December'])} 2026

{recipient}
{random.choice(industries)}
{random.choice(companies)}

Dear {recipient.split()[0]},

RE: {subject}

I hope this letter finds you in good health and high spirits. I am writing on behalf of {company_name} regarding the above-mentioned subject matter.

{company_name} has been a leading provider of professional services for over {random.randint(5,25)} years. We have built a strong reputation for delivering quality, reliability, and innovation across all our operations. We believe that a collaborative relationship between our organizations would be mutually beneficial and yield significant positive outcomes.

We would like to formally propose that we explore opportunities for cooperation in areas of mutual interest. Our team is fully committed to ensuring that any partnership or agreement entered into is fair, transparent, and aligned with the highest professional standards.

We would appreciate the opportunity to meet at your earliest convenience to discuss this matter further. Please do not hesitate to contact us should you require any additional information.

We look forward to your positive response and the possibility of building a long-lasting professional relationship.

Yours faithfully,

{sender}
{random.choice(industries)}
{company_name}
{fname.lower()}.{lname.lower()}@company.com"""

    pairs.append({
        "prompt": f"Write a professional business letter with letterhead for {company_name} regarding {subject}.",
        "response": letter
    })

# 4. GENERATE LINKEDIN SUMMARIES
print("Generating LinkedIn summaries...")
for i in range(500):
    industry = random.choice(industries)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    years = random.randint(2, 20)
    skills = skills_pool.get(industry, "Leadership, Communication, Strategy")

    linkedin = f"""Results-driven {industry} with {years}+ years of experience delivering exceptional outcomes across diverse industries and markets. Passionate about leveraging {skills.split(',')[0].strip()} and innovation to solve complex challenges and create lasting value.

Throughout my career I have consistently exceeded targets, built high-performing teams, and driven organizational transformation. I thrive in dynamic environments where strategic thinking and hands-on execution go hand in hand.

Core competencies: {skills}

Currently open to new opportunities and collaborations. Let's connect and explore how we can create impact together.

#{industry.replace(' ','')} #ProfessionalDevelopment #Leadership #Africa #OpenToWork"""

    pairs.append({
        "prompt": f"Write a professional LinkedIn summary for a {industry} with {years} years of experience.",
        "response": linkedin
    })

# COMBINE WITH EXISTING CV DATA
print("Loading existing CV data...")
existing = []
with open("data/pairs/training_pairs.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        existing.append(json.loads(line))

all_pairs = existing + pairs
random.shuffle(all_pairs)

with open("data/pairs/training_pairs_v2.jsonl", "w", encoding="utf-8") as f:
    for pair in all_pairs:
        f.write(json.dumps(pair) + "\n")

print(f"Original CV data: {len(existing)}")
print(f"New synthetic data: {len(pairs)}")
print(f"TOTAL COMBINED: {len(all_pairs)} training examples")
print("Saved to data/pairs/training_pairs_v2.jsonl")
