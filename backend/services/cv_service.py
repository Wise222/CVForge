# -*- coding: utf-8 -*-
from services.model_service import cvforge_model

def build_cv(data: dict) -> str:
    name = data.get("full_name", "")
    email = data.get("email", "")
    phone = data.get("phone", "")
    location = data.get("location", "")
    nationality = data.get("nationality", "")
    linkedin = data.get("linkedin", "")
    industry = data.get("industry", "")
    seniority = data.get("seniority", "")
    years_exp = data.get("years_exp", 0)
    skills = data.get("skills", "")
    languages = data.get("languages", "")
    job1_title = data.get("job1_title", "")
    job1_company = data.get("job1_company", "")
    job1_dates = data.get("job1_dates", "")
    job1_duties = data.get("job1_duties", "")
    job2_title = data.get("job2_title", "")
    job2_company = data.get("job2_company", "")
    job2_dates = data.get("job2_dates", "")
    job2_duties = data.get("job2_duties", "")
    job3_title = data.get("job3_title", "")
    job3_company = data.get("job3_company", "")
    job3_dates = data.get("job3_dates", "")
    job3_duties = data.get("job3_duties", "")
    degree = data.get("degree", "")
    university = data.get("university", "")
    grad_year = data.get("grad_year", "")
    grade = data.get("grade", "")
    cert1 = data.get("cert1", "")
    cert2 = data.get("cert2", "")
    cert3 = data.get("cert3", "")
    target_role = data.get("target_role", "")
    target_company = data.get("target_company", "")
    hobbies = data.get("hobbies", "")
    summary_input = data.get("summary_input", "")

    # Generate summary
    if summary_input.strip():
        summary = summary_input.strip()
    else:
        summary = cvforge_model.generate_summary(industry, seniority, years_exp, skills)

    lines = []

    # HEADER
    lines.append("=" * 60)
    lines.append(name.upper())
    lines.append(f"{industry}  |  {seniority}")
    lines.append("=" * 60)
    lines.append("")

    # CONTACT
    lines.append("CONTACT INFORMATION")
    lines.append("-" * 40)
    if email: lines.append(f"Email      : {email}")
    if phone: lines.append(f"Phone      : {phone}")
    if location: lines.append(f"Location   : {location}")
    if nationality: lines.append(f"Nationality: {nationality}")
    if linkedin: lines.append(f"LinkedIn   : {linkedin}")
    lines.append("")

    # SUMMARY
    lines.append("PROFESSIONAL SUMMARY")
    lines.append("-" * 40)
    lines.append(summary)
    lines.append("")

    # SKILLS
    if skills:
        lines.append("CORE COMPETENCIES")
        lines.append("-" * 40)
        skill_list = [s.strip() for s in skills.split(",") if s.strip()]
        for i in range(0, len(skill_list), 2):
            left = f"\u2022 {skill_list[i]:<28}" if i < len(skill_list) else ""
            right = f"\u2022 {skill_list[i+1]}" if i+1 < len(skill_list) else ""
            lines.append(f"{left}{right}")
        lines.append("")

    # EXPERIENCE
    lines.append("PROFESSIONAL EXPERIENCE")
    lines.append("-" * 40)
    for title, company, dates, duties in [
        (job1_title, job1_company, job1_dates, job1_duties),
        (job2_title, job2_company, job2_dates, job2_duties),
        (job3_title, job3_company, job3_dates, job3_duties)
    ]:
        if title and company:
            lines.append(f"{title.upper()}")
            lines.append(f"{company}  |  {dates}")
            for duty in [d.strip() for d in duties.split(",") if d.strip()]:
                lines.append(f"  \u2022 {duty}")
            lines.append("")

    # EDUCATION
    lines.append("EDUCATION")
    lines.append("-" * 40)
    if degree:
        lines.append(degree)
    if university:
        lines.append(f"{university}  |  {grad_year}  |  {grade}")
    lines.append("")

    # CERTIFICATIONS
    certs = [c for c in [cert1, cert2, cert3] if c.strip()]
    if certs:
        lines.append("CERTIFICATIONS & MEMBERSHIPS")
        lines.append("-" * 40)
        for cert in certs:
            lines.append(f"  \u2022 {cert}")
        lines.append("")

    # LANGUAGES
    if languages:
        lines.append("LANGUAGES")
        lines.append("-" * 40)
        for lang in [l.strip() for l in languages.split(",") if l.strip()]:
            lines.append(f"  \u2022 {lang}")
        lines.append("")

    # INTERESTS
    if hobbies:
        lines.append("INTERESTS & COMMUNITY INVOLVEMENT")
        lines.append("-" * 40)
        lines.append(hobbies)
        lines.append("")

    return "\n".join(lines)

def build_cover_letter(data: dict) -> str:
    name = data.get("full_name", "")
    email = data.get("email", "")
    phone = data.get("phone", "")
    location = data.get("location", "")
    industry = data.get("industry", "")
    skills = data.get("skills", "")
    years_exp = data.get("years_exp", 0)
    job1_title = data.get("job1_title", "")
    job1_company = data.get("job1_company", "")
    job1_duties = data.get("job1_duties", "")
    target_role = data.get("target_role", "")
    target_company = data.get("target_company", "")

    body = cvforge_model.generate_cover_letter_body(name, target_role, target_company, industry, skills, job1_title, job1_company)

    lines = []
    lines.append(name)
    lines.append(location)
    lines.append(phone)
    lines.append(email)
    lines.append("")
    lines.append("Dear Hiring Manager,")
    lines.append("")
    lines.append(f"RE: APPLICATION FOR {target_role.upper()} - {target_company.upper()}")
    lines.append("")
    lines.append(body)
    lines.append("")
    lines.append(f"I am confident that my {years_exp} years of experience in {industry}, combined with my expertise in {skills}, make me an excellent candidate for this role.")
    lines.append("")
    lines.append(f"I would welcome the opportunity to discuss how my background aligns with the needs of {target_company}. Please find my CV attached for your review.")
    lines.append("")
    lines.append("Thank you for your time and consideration.")
    lines.append("")
    lines.append("Yours sincerely,")
    lines.append("")
    lines.append(name)
    lines.append(phone)
    lines.append(email)
    return "\n".join(lines)

def build_linkedin(data: dict) -> str:
    name = data.get("full_name", "")
    email = data.get("email", "")
    industry = data.get("industry", "")
    seniority = data.get("seniority", "")
    years_exp = data.get("years_exp", 0)
    skills = data.get("skills", "")
    job1_company = data.get("job1_company", "")
    target_role = data.get("target_role", "")

    summary = cvforge_model.generate_linkedin(name, industry, seniority, years_exp, skills, job1_company)

    skill_tags = "  ".join([f"\u2022 {s.strip()}" for s in skills.split(",")[:6] if s.strip()])
    lines = []
    lines.append("LINKEDIN PROFILE SUMMARY")
    lines.append("=" * 50)
    lines.append("")
    lines.append(summary)
    lines.append("")
    lines.append("WHAT I BRING:")
    lines.append(skill_tags)
    lines.append("")
    lines.append(f"OPEN TO: {target_role} opportunities")
    lines.append(f"CONNECT: {email}")
    return "\n".join(lines)

def build_reference(data: dict) -> str:
    name = data.get("full_name", "")
    email = data.get("email", "")
    job1_title = data.get("job1_title", "")
    job1_company = data.get("job1_company", "")
    job1_duties = data.get("job1_duties", "")
    skills = data.get("skills", "")
    target_role = data.get("target_role", "")

    body = cvforge_model.generate_reference_body(name, target_role, job1_title, job1_company, job1_duties, skills)

    lines = []
    lines.append("[COMPANY LETTERHEAD]")
    lines.append("")
    lines.append("TO WHOM IT MAY CONCERN")
    lines.append("")
    lines.append(f"RE: REFERENCE FOR {name.upper()}")
    lines.append("")
    lines.append(f"I am pleased to provide this reference for {name}, who served as {job1_title} at {job1_company}.")
    lines.append("")
    lines.append(body)
    lines.append("")
    lines.append(f"I have no hesitation in recommending {name.split()[0]} for the position of {target_role}.")
    lines.append("")
    lines.append("Yours faithfully,")
    lines.append("")
    lines.append("_______________________")
    lines.append("[Referee Name & Title]")
    lines.append("[Company & Contact Details]")
    return "\n".join(lines)
