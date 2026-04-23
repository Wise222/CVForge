# -*- coding: utf-8 -*-
import json, random, os

first_names = ["James","Grace","Peter","Mary","John","Sarah","David","Ruth","Moses","Alice","Emmanuel","Fatima","Michael","Amara","Chioma","Kwame","Aisha","Ibrahim","Blessing","Chidi","Nkechi","Seun","Tunde","Yemi","Kofi","Abena","Tendai","Rudo","Thabo","Lerato","Ahmed","Fatou","Moussa","Aminata","Daniel","Jennifer","Robert","Linda","Priya","Rahul"]
last_names = ["Mwale","Banda","Phiri","Tembo","Mulenga","Zulu","Lungu","Mutale","Chanda","Sichone","Osei","Diallo","Onyeka","Mensah","Nwosu","Asante","Owusu","Moyo","Dube","Ncube","Ndlovu","Sibanda","Nkosi","Dlamini","Hassan","Ibrahim","Toure","Camara","Smith","Johnson","Williams","Brown","Sharma","Patel","Kumar","Singh","Wang","Li","Zhang","Liu"]
cities = ["Lusaka, Zambia","Nairobi, Kenya","Lagos, Nigeria","Accra, Ghana","Johannesburg, South Africa","Dar es Salaam, Tanzania","Kampala, Uganda","Harare, Zimbabwe","Kigali, Rwanda","Addis Ababa, Ethiopia","Abidjan, Ivory Coast","Dakar, Senegal","Douala, Cameroon","Maputo, Mozambique","Gaborone, Botswana"]
industries = ["Finance","Technology","Healthcare","Engineering","Marketing","NGO","Government","Mining","Education","Telecoms"]

companies = {"Finance":["Zambia National Commercial Bank","Standard Chartered Zambia","First National Bank","Barclays Africa","Old Mutual","Ecobank","African Development Bank","Deloitte Africa","PricewaterhouseCoopers","Ernst and Young Africa"],"Technology":["MTN Group","Airtel Africa","Safaricom","Andela","Flutterwave","Paystack","Interswitch","Microsoft Africa","IBM Africa","Google Africa"],"Healthcare":["Zambia Ministry of Health","Kenya National Hospital","Lagos University Teaching Hospital","Aga Khan Hospital","AMREF Health Africa","MSF Africa","WHO Regional Office","CDC Africa","Pfizer Africa","GlaxoSmithKline Africa"],"Engineering":["Zambia Electricity Supply Corporation","Kenya Power","Eskom","Dangote Group","Lafarge Africa","Julius Berger","Murray and Roberts","Aurecon Africa","AECOM Africa","Group Five"],"Marketing":["Ogilvy Africa","JWT Africa","TBWA Africa","Publicis Africa","Unilever Africa","Procter and Gamble Africa","Nestle Africa","Coca Cola Africa","SABMiller","Diageo Africa"],"NGO":["UNICEF Zambia","UNDP Africa","World Food Programme","Oxfam Africa","Save the Children","Care International","ActionAid","Plan International","World Vision","Catholic Relief Services"],"Government":["Zambia Revenue Authority","Kenya Revenue Authority","Ghana Revenue Authority","Ministry of Finance","Ministry of Health","Ministry of Education","Ministry of Agriculture","Public Service Commission","Electoral Commission","National Planning Commission"],"Mining":["Zambia Consolidated Copper Mines","First Quantum Minerals","Glencore Zambia","Barrick Gold Africa","Anglo American Africa","De Beers","Sibanye-Stillwater","Gold Fields","Harmony Gold","Impala Platinum"],"Education":["University of Zambia","University of Nairobi","University of Ghana","University of Lagos","Makerere University","University of Cape Town","African Leadership University","Strathmore University","Ashesi University","USIU Africa"],"Telecoms":["Zamtel","Vodacom","Cell C","Telkom Africa","Orange Africa","Tigo","Glo Mobile","Liquid Telecom","SEACOM","Econet"]}

strong_verbs = ["Led","Managed","Directed","Supervised","Spearheaded","Developed","Designed","Built","Implemented","Delivered","Achieved","Exceeded","Secured","Generated","Optimized","Streamlined","Transformed","Trained","Mentored","Analyzed","Negotiated","Increased","Reduced","Improved","Enhanced"]
seniority_levels = [("Entry Level",1,2),("Junior Professional",2,4),("Mid-Level Professional",4,8),("Senior Professional",8,15),("Manager",10,20),("Director",15,30)]
qualifications = {"Finance":["Bachelor of Accountancy","Bachelor of Commerce in Finance","Master of Business Administration","ACCA","CIMA","CFA Level III","ZICA Full Member","CA(SA)"],"Technology":["Bachelor of Science in Computer Science","Bachelor of Information Technology","Master of Science in Data Science","AWS Certified Solutions Architect","Google Cloud Professional","Microsoft Azure Administrator","Cisco CCNA"],"Healthcare":["Bachelor of Medicine and Surgery","Bachelor of Nursing Science","Master of Public Health","Bachelor of Pharmacy","Registered Nurse","ACLS Certified","WHO Emergency Response Training"],"Engineering":["Bachelor of Science in Civil Engineering","Bachelor of Science in Electrical Engineering","Bachelor of Science in Mechanical Engineering","Master of Science in Structural Engineering","Professional Engineer Registration"],"Marketing":["Bachelor of Commerce in Marketing","Master of Business Administration","CIM Professional Diploma","Google Analytics Certified","HubSpot Marketing Certified"],"NGO":["Bachelor of Social Work","Master of Development Studies","Bachelor of International Relations","Project Management Professional","Monitoring and Evaluation Certificate"],"Government":["Bachelor of Public Administration","Master of Public Policy","Bachelor of Laws","Bachelor of Economics","Senior Management Programme"],"Mining":["Bachelor of Science in Mining Engineering","Bachelor of Science in Geology","Master of Science in Mineral Processing","Mine Manager Certificate of Competency","SAIMM Member"],"Education":["Bachelor of Education","Master of Education","PhD in Educational Psychology","Postgraduate Certificate in Education","Cambridge International Teaching Certificate"],"Telecoms":["Bachelor of Engineering in Telecommunications","Master of Science in Network Engineering","Cisco CCNP","Nokia Deepfield Certified","Ericsson Certified Engineer"]}

def rname(): return f"{random.choice(first_names)} {random.choice(last_names)}"
def rcompany(ind): return random.choice(companies.get(ind, companies["Finance"]))
def rqual(ind): return random.choice(qualifications.get(ind, qualifications["Finance"]))
def rverb(): return random.choice(strong_verbs)
def rpct(): return random.randint(12,48)
def rnum(): return random.randint(3,50)
def rrev(): return random.randint(1,20)

pairs = []

# CV GENERATION - 40000 examples
print("Generating 40000 professional CVs...")
for i in range(40000):
    ind = random.choice(industries)
    sen, mne, mxe = random.choice(seniority_levels)
    yrs = random.randint(mne, mxe)
    name = rname()
    city = random.choice(cities)
    c1 = rcompany(ind)
    c2 = rcompany(ind)
    c3 = rcompany(ind)
    qual = rqual(ind)
    uni = random.choice(["Zambia","Nairobi","Ghana","Lagos","Cape Town","Makerere","Dar es Salaam","Kigali"])
    gyr = random.randint(2000,2020)
    v1,v2,v3,v4 = random.sample(strong_verbs,4)
    p1,p2,p3 = rpct(),rpct(),rpct()
    n1,n2,n3 = rnum(),rnum(),rnum()
    r1,r2 = rrev(),rrev()
    grade = random.choice(["First Class Honours","Upper Second Class Honours","Lower Second Class Honours","Pass with Distinction","Merit"])
    skills = random.sample(["Strategic Planning","Financial Analysis","Team Leadership","Project Management","Stakeholder Engagement","Process Improvement","Data Analysis","Risk Management","Budget Management","Change Management","Performance Management","Business Development","Client Relations","Operations Management","Quality Assurance","Communication","Negotiation","Problem Solving","Research","Reporting"],8)
    cv = f"""{name.upper()}
{city} | {name.lower().replace(chr(32),chr(46))}{random.randint(1,99)}@gmail.com

PROFESSIONAL SUMMARY
{"="*55}
{sen} {ind} professional with {yrs} years of progressive experience. Proven track record of delivering measurable results through strategic thinking and effective stakeholder management.

CORE COMPETENCIES
{"="*55}
{" | ".join(skills)}

PROFESSIONAL EXPERIENCE
{"="*55}
{ind.upper()} SPECIALIST  |  {c1}  |  {gyr+yrs} - Present
  {chr(8226)} {v1} departmental performance by {p1}%, exceeding organizational targets for {n1} consecutive quarters
  {chr(8226)} {v2} team of {n2} professionals delivering {n3} concurrent projects valued at USD {r1}M
  {chr(8226)} {v3} operational processes resulting in {p2}% reduction in turnaround time
  {chr(8226)} {v4} USD {r2}M budget with {p3}% variance against approved estimates

{ind.upper()} OFFICER  |  {c2}  |  {gyr+2} - {gyr+yrs}
  {chr(8226)} {random.choice(strong_verbs)} {n1} key initiatives contributing to {p1}% growth in departmental output
  {chr(8226)} {random.choice(strong_verbs)} relationships with {n2} strategic partners across {random.randint(2,8)} markets
  {chr(8226)} {random.choice(strong_verbs)} compliance framework adopted across {random.randint(2,6)} regional offices

JUNIOR {ind.upper()} OFFICER  |  {c3}  |  {gyr+1} - {gyr+2}
  {chr(8226)} Supported delivery of {n3} projects within agreed timelines and budget parameters
  {chr(8226)} Prepared {random.randint(10,50)} management reports for executive review
  {chr(8226)} Maintained accurate records ensuring {p3}% compliance with organizational standards

EDUCATION
{"="*55}
{qual}
University of {uni}  |  {gyr}  |  {grade}

LANGUAGES
{"="*55}
{random.choice(["English (Fluent)","English (Fluent) | French (Intermediate)","English (Fluent) | Swahili (Native)","English (Fluent) | Arabic (Intermediate)","English (Fluent) | Portuguese (Basic)"])}"""
    pairs.append({"prompt":f"Write a professional CV for a {sen} {ind} professional with {yrs} years experience in {city}.","response":cv.strip()})
    if (i+1) % 5000 == 0: print(f"  CVs: {i+1}/40000")

# COVER LETTERS - 20000 examples
print("Generating 20000 cover letters...")
openings = ["I am writing to express my strong interest in the {role} position at {company}.","Your advertisement for {role} at {company} immediately captured my attention.","The opportunity to join {company} as {role} aligns perfectly with my professional trajectory.","Having followed {company} growth with great admiration I was compelled to apply for the {role} role.","I am excited to submit my application for the {role} position at {company}."]
closings = ["I would welcome the opportunity to discuss how my experience aligns with your requirements.","I am confident that my background makes me a compelling candidate for this role.","I look forward to the possibility of contributing to your continued success.","I would be grateful for the opportunity to elaborate on my qualifications in an interview.","Please find my CV attached and I remain available at your convenience."]
impact_phrases = ["exceeded quarterly targets by {p}% for {n} consecutive periods","delivered {n} high-impact projects valued at USD {r}M within approved budgets","reduced operational costs by {p}% through process redesign and automation","grew team capability by training and developing {n} junior professionals","secured USD {r}M in new business through strategic client engagement"]

for i in range(20000):
    ind = random.choice(industries)
    sen, mne, mxe = random.choice(seniority_levels)
    yrs = random.randint(mne, mxe)
    name = rname()
    c1 = rcompany(ind)
    c2 = rcompany(ind)
    role = f"{random.choice([sen,chr(83)+chr(101)+chr(110)+chr(105)+chr(111)+chr(114)])} {ind} {random.choice([chr(79)+chr(102)+chr(102)+chr(105)+chr(99)+chr(101)+chr(114),chr(77)+chr(97)+chr(110)+chr(97)+chr(103)+chr(101)+chr(114),chr(83)+chr(112)+chr(101)+chr(99)+chr(105)+chr(97)+chr(108)+chr(105)+chr(115)+chr(116)])}"
    opening = random.choice(openings).format(role=role,company=c1)
    closing = random.choice(closings)
    impact = random.choice(impact_phrases).format(p=rpct(),n=rnum(),r=rrev())
    v1 = rverb()
    letter = f"""{name}
{random.choice(cities)}

Dear Hiring Manager,

RE: APPLICATION FOR {role.upper()} - {c1.upper()}

{opening}

With {yrs} years of progressive experience in {ind.lower()}, I have built a comprehensive skill set that I believe would add immediate value to {c1}. In my current role at {c2}, I have {impact}.

What particularly draws me to {c1} is its reputation for excellence and commitment to impact. I am confident that my background in {ind.lower()} combined with my demonstrated ability to deliver results would make me a strong addition to your team.

I bring a proven track record of {random.choice(["exceeding targets","delivering complex projects","building high-performing teams","driving organizational transformation","developing strategic partnerships"])} and I am eager to bring this commitment to {c1}.

{closing}

Yours sincerely,
{name}"""
    pairs.append({"prompt":f"Write a professional cover letter for {name} applying for {role} at {c1}.","response":letter.strip()})
    if (i+1) % 5000 == 0: print(f"  Cover Letters: {i+1}/20000")

# COVER LETTERS - 20000 examples
print("Generating 20000 cover letters...")
openings = ["I am writing to express my strong interest in the {r} position at {c}.","Your advertisement for a {r} at {c} immediately captured my attention.","The opportunity to join {c} as {r} aligns perfectly with my professional trajectory.","Having followed {c} growth with great admiration I was compelled to apply for the {r} role.","I am excited to submit my application for the {r} position at {c}."]
closings = ["I would welcome the opportunity to discuss how my experience aligns with your requirements.","I am confident that my background makes me a compelling candidate for this role.","I look forward to the possibility of contributing to your continued success.","I would be grateful for the opportunity to elaborate on my qualifications in an interview.","Please find my CV attached and I remain available at your convenience."]
for i in range(20000):
    ind = random.choice(industries)
    sen, mne, mxe = random.choice(seniority_levels)
    yrs = random.randint(mne, mxe)
    name = rname()
    c1 = rcompany(ind)
    c2 = rcompany(ind)
    role = f"{random.choice(["Senior","Lead","Principal","Head of"])} {ind} Manager"
    v1 = rverb()
    v2 = rverb()
    p1 = rpct()
    n1 = rnum()
    r1 = rrev()
    opening = random.choice(openings).format(r=role,c=c1)
    closing = random.choice(closings)
    letter = f"""Dear Hiring Manager,

RE: APPLICATION FOR {role.upper()} - {c1.upper()}

{opening}

With {yrs} years of progressive experience in {ind.lower()}, I have built a comprehensive skill set that would add immediate value to {c1}. In my current role at {c2}, I {v1.lower()}ed departmental performance by {p1}% and {v2.lower()}ed a team of {n1} professionals to deliver USD {r1}M in results.

What draws me to {c1} is its reputation for excellence and commitment to impact. I bring a proven track record of exceeding targets, building high-performing teams, and driving organizational transformation. I am confident this experience translates directly to the requirements of this role.

{closing}

Yours sincerely,
{name}"""
    pairs.append({"prompt":f"Write a professional cover letter for {name} applying for {role} at {c1}.","response":letter.strip()})
    if (i+1) % 5000 == 0: print(f"  Cover letters: {i+1}/20000")

# LINKEDIN SUMMARIES - 10000 examples
print("Generating 10000 LinkedIn summaries...")
for i in range(10000):
    ind = random.choice(industries)
    sen, mne, mxe = random.choice(seniority_levels)
    yrs = random.randint(mne, mxe)
    name = rname()
    c1 = rcompany(ind)
    v1 = rverb()
    p1 = rpct()
    n1 = rnum()
    impact = random.choice(["sub-Saharan Africa","East Africa","West Africa","Southern Africa","the African continent","global markets"])
    strength = random.choice(["translating complex challenges into actionable solutions","building high-performance teams that deliver results","bringing commercial rigour to every initiative","bridging the gap between strategy and execution"])
    passion = random.choice(["developing the next generation of African professionals","driving sustainable economic growth across the continent","leveraging technology to solve real problems","building institutions that outlast individuals"])
    open_to = random.choice(["senior leadership roles","executive management positions","board advisory opportunities","strategic consulting engagements"])
    summary = f"""{sen} {ind} professional with {yrs} years of experience driving results across {impact}. At {c1}, I {v1.lower()}ed performance by {p1}% and built a team of {n1} high-performing professionals.

My expertise spans strategic planning, operational excellence, and stakeholder management. I am known for {strength}.

Passionate about {passion}.

Open to: {open_to} | Connect: {name.lower().replace(chr(32),chr(46))}@gmail.com"""
    pairs.append({"prompt":f"Write a professional LinkedIn summary for a {sen} {ind} professional with {yrs} years of experience.","response":summary.strip()})
    if (i+1) % 2500 == 0: print(f"  LinkedIn: {i+1}/10000")

# TRANSFORMATION PAIRS - 20000 examples
print("Generating 20000 transformation pairs...")
weak_to_strong = [
    ("responsible for managing the accounts department", "Directed accounts department of {n} staff overseeing monthly financial close and ensuring full IFRS compliance"),
    ("helped with project delivery", "Contributed to delivery of {n} projects valued at USD {r}M ensuring all milestones were achieved within agreed timelines"),
    ("assisted in preparing reports", "Produced {n} comprehensive management reports monthly synthesizing data from multiple departments for executive decision-making"),
    ("worked on the website", "Developed company website serving {n}K monthly users improving load time by {p}% and increasing conversion rate by {p}%"),
    ("did customer service duties", "Managed customer experience for {n}K clients achieving {p}% satisfaction rating and reducing complaint resolution time by {p}%"),
    ("was in charge of the team", "Led team of {n} professionals delivering {p}% improvement in productivity and {p}% reduction in project delivery time"),
    ("handled complaints from clients", "Resolved {n} client escalations monthly achieving {p}% first-contact resolution and reducing churn by {p}%"),
    ("did data entry tasks", "Managed data integrity for {n}K records implementing validation protocols that reduced error rate by {p}%"),
    ("helped train new staff", "Designed induction programme for {n} new hires reducing onboarding time by {p}% and improving 90-day retention"),
    ("worked on improving processes", "Eliminated {n} process inefficiencies reducing cycle time by {p}% and saving USD {r}K annually"),
    ("responsible for sales targets", "Exceeded quarterly targets by {p}% for {n} consecutive quarters generating USD {r}M in new revenue"),
    ("assisted with financial reporting", "Prepared financial statements for {n} entities ensuring timely submission with {p}% first-submission accuracy"),
    ("helped with recruitment", "Managed recruitment for {n} positions reducing time-to-hire by {p}% and achieving {p}% offer acceptance rate"),
    ("did administrative duties", "Coordinated operations for {n}-person office implementing systems improving workflow efficiency by {p}%"),
    ("worked in the IT department", "Provided technical support for {n} users maintaining {p}% uptime and resolving {p}% of tickets within SLA"),
    ("responsible for health and safety", "Implemented HSE system across {n} sites achieving {p}% reduction in incidents and zero fatality record"),
    ("helped coordinate events", "Coordinated {n} corporate events for {n} delegates managing USD {r}K budgets achieving {p}% satisfaction"),
    ("assisted in budget preparation", "Supported USD {r}M budget preparation identifying {n} cost reduction opportunities saving USD {r}K"),
    ("worked with suppliers", "Managed {n} vendor relationships negotiating contracts delivering {p}% cost reduction with maintained quality"),
    ("responsible for quality control", "Implemented quality system reducing defect rate by {p}% and improving first-pass yield by {p}%")
]
for i in range(20000):
    weak, strong_t = random.choice(weak_to_strong)
    strong = strong_t.format(n=rnum(),r=rrev(),p=rpct())
    ind = random.choice(industries)
    pairs.append({"prompt":f"Rewrite this CV bullet point professionally for a {ind} role: {weak}","response":strong})
    if (i+1) % 5000 == 0: print(f"  Transformations: {i+1}/20000")

# REFERENCE LETTERS - 10000 examples
print("Generating 10000 reference letters...")
titles = ["Chief Executive Officer","Chief Financial Officer","Director General","General Manager","Head of Department","Senior Manager"]
for i in range(10000):
    ind = random.choice(industries)
    sen, mne, mxe = random.choice(seniority_levels)
    yrs = random.randint(mne, mxe)
    name = rname()
    referee = rname()
    c1 = rcompany(ind)
    role = f"{ind} Officer"
    target = f"Senior {ind} Manager"
    v1,v2 = rverb(),rverb()
    p1,p2 = rpct(),rpct()
    n1,r1 = rnum(),rrev()
    start_yr = random.randint(2015,2020)
    end_yr = random.randint(2021,2024)
    letter = f"""TO WHOM IT MAY CONCERN

RE: PROFESSIONAL REFERENCE - {name.upper()}

I am pleased to provide this reference for {name}, who served as {role} at {c1} from {start_yr} to {end_yr}.

During their tenure they consistently demonstrated the highest professional standards. They {v1.lower()}ed departmental performance by {p1}% and {v2.lower()}ed a team of {n1} professionals to deliver USD {r1}M in results.

I recommend {name.split()[0]} without reservation for the position of {target}. They possess the skills, character and drive to excel in any demanding environment.

Yours faithfully,
{referee}
{random.choice(titles)}
{c1}"""
    pairs.append({"prompt":f"Write a professional reference letter for {name} who worked as {role} at {c1}.","response":letter.strip()})
    if (i+1) % 2500 == 0: print(f"  References: {i+1}/10000")

# SAVE ALL
print(f"\nTotal examples generated: {len(pairs)}")
random.shuffle(pairs)
os.makedirs("data/pairs", exist_ok=True)
with open("data/pairs/training_pairs_v4.jsonl","w",encoding="utf-8") as f:
    for p in pairs:
        f.write(json.dumps(p,ensure_ascii=False)+"\n")
print("Saved to data/pairs/training_pairs_v4.jsonl")
print(f"DONE! {len(pairs)} premium training examples ready!")

