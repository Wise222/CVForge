# CVForge Pro - Master Project Context & Bible
**Last Updated:** April 23, 2026
**Version:** 3.0
**Status:** ACTIVE DEVELOPMENT
**Primary Tool:** PowerShell on Windows - ALL scripts must be paste-safe using string arrays $lines = @() | Set-Content - NEVER use here-strings @" "@ as they break when pasted directly into PowerShell

---

## CRITICAL INSTRUCTIONS FOR ANY AI READING THIS

1. ALL code must be paste-safe for PowerShell - use $lines = @(...) | Set-Content pattern only
2. Always specify exactly WHERE to paste - PowerShell, Kaggle notebook, or browser
3. Do NOT produce generic AI output - think like a senior commercial product developer
4. Every design decision must be intentional, unique, and commercial-grade
5. The AI model output is NOT trusted for structure - always use template-driven CV building
6. AI is only used to generate the professional summary section - all other CV sections are built from user inputs
7. Never waste the users time - be direct, specific, and efficient
8. This is a commercial product targeting millions of job seekers worldwide - treat it as such
9. Do not suggest Gradio for the final product - we are moving to FastAPI + React
10. Always commit to GitHub after major changes

---

## WHY THIS PROJECT EXISTS

Millions of people across Africa and the developing world cannot afford professional CV writers.
A bad CV means a missed job opportunity. CVForge Pro is a free, open-source, AI-powered platform
that writes professional, industry-specific CVs, cover letters, LinkedIn summaries, reference letters
and business letters from simple user input. This is NOT a side project. This is a commercial-grade
product with real human impact targeting millions of job seekers worldwide.

---

## PROJECT IDENTITY

- Name: CVForge Pro
- Tagline: Africa Most Advanced AI Career Document Builder
- License: MIT open source free forever at base level
- Target Markets: Zambia, Kenya, Nigeria, Ghana, South Africa, Tanzania, Uganda, Zimbabwe, India, Philippines, Middle East, Global
- Languages Planned: English done, French, Swahili, Portuguese, Arabic
- Monetization: Freemium - basic free, premium PDF templates paid, B2B licensing to universities and recruitment agencies
- GitHub: https://github.com/Wise222/CVForge
- Hugging Face: https://huggingface.co/Wise222

---

## WHAT HAS BEEN DONE - COMPLETED WORK

### Environment Setup - DONE
- Python 3.14.3 installed on Windows
- Git 2.53.0 installed
- All Python libraries installed: transformers, peft, trl, accelerate, gradio, fpdf2, python-docx, kaggle, huggingface_hub, ollama, datasets, torch, pandas
- PATH configured for all tools
- GitHub repo created and connected: https://github.com/Wise222/CVForge
- Kaggle account created: goodcontentacademy
- Hugging Face account created: Wise222
- Kaggle API token configured at C:\Users\katam\.kaggle\kaggle.json

### Data Collection - DONE
- Downloaded 4 Kaggle CV datasets totaling 21,240 raw CVs
- snehaanbhawal/resume-dataset: 2,484 CVs
- avishekmajhi/resume-dataset: 8,234 CVs
- jillanisofttech/updated-resume-dataset: 962 CVs
- saugataroyarghya/resume-dataset: 9,544 CVs with detailed fields
- All raw files in: C:\Users\katam\Projects\CVForge\data\raw\

### Data Processing - DONE
- clean_data.py: combines and cleans all raw CSVs into cleaned_resumes.csv (10,794 clean CVs)
- format_pairs.py: converts to JSONL training format - training_pairs.jsonl (10,794 pairs)
- generate_synthetic.py: generates cover letters, letterheads, LinkedIn summaries (6,500 synthetic examples)
- build_v3_dataset.py: combines everything into training_pairs_v3.jsonl (26,836 total examples)

### Training Datasets Created
- training_pairs.jsonl: 10,794 CV pairs (v1)
- training_pairs_v2.jsonl: 17,294 pairs - CVs plus cover letters plus letterheads plus LinkedIn
- training_pairs_v3.jsonl: 26,836 pairs - all above plus 9,542 detailed CVs
- All datasets uploaded to Kaggle: goodcontentacademy/cvforge-training-data-v3

### Model Training - DONE
- Base model: TinyLlama 1.1B Chat v1.0
- Training method: PEFT LoRA fine-tuning
- LoRA config: r=16, lora_alpha=32, lora_dropout=0.05, target_modules q_proj v_proj k_proj o_proj
- GPU: Kaggle P100 16GB
- cvforge-model v1: 500 CVs, 3 epochs, loss 2.1 - saved at Wise222/cvforge-model
- cvforge-model v2: 10,794 CVs, 3 epochs, loss 1.8 - saved at Wise222/cvforge-model-v2
- cvforge-model v3: 26,836 examples, 3 epochs continuing from v2 - IN PROGRESS on Kaggle

### Application - CURRENT VERSION
- Framework: Gradio (TEMPORARY - moving to FastAPI + React)
- File: C:\Users\katam\Projects\CVForge\app\app.py
- Run command in PowerShell: python C:\Users\katam\Projects\CVForge\app\app.py
- Access at: http://127.0.0.1:7860
- Current features: CV generation, Cover Letter, LinkedIn Summary, Reference Letter, 5 PDF templates, PDF download
- Key improvement made: template-driven CV building - AI only writes professional summary, all other sections built from user inputs - this fixes the random paragraph problem

---

## CURRENT PROBLEMS TO FIX

1. Gradio is a demo tool not a commercial product - replacing with FastAPI + React
2. PDF templates need professional two-column layouts like real CV templates
3. Model output still has some repetition - v3 training will improve this
4. No user accounts or CV saving yet
5. No mobile responsive design yet
6. Share link blocked by Windows firewall - only local access currently

---

## WHAT WE ARE BUILDING NEXT - THE REAL PRODUCT

### Tech Stack Decision - FINAL

Frontend: React with TailwindCSS
- Complete design freedom and pixel perfect control
- Fully responsive on mobile tablet desktop
- Component based architecture
- Professional commercial look

Backend: FastAPI with Python
- Same language as AI training code
- Fast modern production ready
- Full control over AI model integration
- Automatic API documentation
- Easy deployment

PDF Generation: WeasyPrint
- Professional quality PDFs with HTML and CSS
- Real two-column layouts
- Custom fonts and colors
- Far superior to fpdf2

Database: SQLite for local, PostgreSQL for production
- Save user CVs
- User accounts
- Usage analytics

Deployment: Railway or Render (both free tier available)
- Free hosting for the app
- Hugging Face Spaces for the model

### Architecture

User Browser React
    connects to
FastAPI Backend Python
    connects to
TinyLlama AI Model - for professional summary generation only
    and
WeasyPrint PDF Generator - for all document exports
    and
SQLite Database - for saving CVs and user data

### Build Order
Step 1: Set up FastAPI backend and connect AI model
Step 2: Build React frontend with all CV form sections
Step 3: Connect frontend to backend API
Step 4: Build WeasyPrint PDF templates - 5 designs
Step 5: Add CV saving and user accounts
Step 6: Mobile responsive testing and fixes
Step 7: Deploy to Railway or Render free hosting
Step 8: Deploy model to Hugging Face Spaces
Step 9: Share publicly and collect feedback
Step 10: Iterate based on feedback

---

## CV DOCUMENT STRUCTURE - NON NEGOTIABLE

Every CV produced by CVForge Pro must have these sections in this order:
1. Header - Full name, contact details, LinkedIn, location
2. Professional Summary - 3 to 4 sentences, AI generated or user written
3. Core Competencies - Skills in a clean grid format
4. Professional Experience - Each job with title, company, dates, bullet point achievements
5. Education - Degree, institution, year, grade
6. Certifications and Professional Memberships
7. Languages
8. Interests and Community Involvement

RULE: The AI model never writes the full CV. It only writes the professional summary.
RULE: All other sections are built from user inputs in a strict template.
RULE: Every achievement must be a bullet point.
RULE: Dates must always be clearly visible.
RULE: The CV must be ATS friendly - no tables, no images, clean text.

---

## PDF TEMPLATE DESIGNS PLANNED

1. Classic Professional - White background, black text, simple header line, timeless
2. Modern Blue - Dark navy header with white name, blue accent lines, corporate
3. Executive Gold - Black header with gold name and accents, premium feel
4. African Heritage - Pan-African color stripe header, bold and culturally proud
5. Minimalist - Clean gray tones, maximum white space, modern and simple
6. Two Column - Left sidebar with contact and skills, right main content - most popular globally
7. Creative - For designers, marketers, creatives - colored sidebar with icon accents

---

## DATA STRATEGY - WHAT WE NEED MORE OF

Current: 26,836 training examples
Target: 100,000+ examples for loss below 1.2

Priority data needed:
1. More real CV data - search Kaggle for resume cv curriculum vitae datasets
2. African specific CVs - local companies, local qualifications like ZICA ACCA CFA CIMA
3. Cover letter dataset - need 10,000 real examples, currently only 2,000 synthetic
4. Job description dataset - to train ATS keyword optimization
5. French CVs for West Africa
6. Swahili CVs for East Africa

Trusted data sources:
- Kaggle datasets: resume-dataset, cv-dataset, curriculum-vitae
- GitHub: search resume dataset cv dataset
- User submitted CVs anonymized from the app
- Synthetic generation using Claude API

---

## MODEL UPGRADE PATH

Current: TinyLlama 1.1B - decent, loss 1.8, good for summaries
Next: Mistral 7B - requires Colab Pro 10/month or Vast.ai 2 to 3 dollars per run
Target loss: below 1.0 for world class output

When to upgrade to Mistral 7B:
- When v3 training completes and loss is confirmed
- When we have 50,000+ training examples
- When the React app is built and working

---

## FOLDER STRUCTURE

C:\Users\katam\Projects\CVForge\
  app\
    app.py                     Current Gradio app - temporary
    templates\                 PDF template assets
    static\                    CSS and images
  data\
    raw\                       4 downloaded Kaggle CSV files
    cleaned\
      cleaned_resumes.csv      10,794 cleaned CVs
    pairs\
      training_pairs.jsonl     10,794 pairs v1
      training_pairs_v2.jsonl  17,294 pairs v2
      training_pairs_v3.jsonl  26,836 pairs v3 - MAIN TRAINING FILE
    synthetic\                 Generated training examples
  model\
    final\                     Local model storage
  training\
    checkpoints\               Training checkpoints
  notebooks\
    CVForge_Finetune.ipynb     Training notebook
  clean_data.py                Data cleaning script
  format_pairs.py              JSONL formatter
  generate_synthetic.py        Synthetic data generator
  build_v3_dataset.py          V3 dataset builder
  CONTEXT.md                   THIS FILE
  PROGRESS.md                  Task tracker
  README.md                    Public description
  .gitignore                   Protects large files

---

## HOW TO RESUME THIS PROJECT WITH ANY AI

1. Open C:\Users\katam\Projects\CVForge\CONTEXT.md
2. Copy the entire file
3. Paste into Claude or any AI assistant
4. Say: I want to continue building CVForge Pro - read the context and tell me what to do next
5. The AI will know everything and pick up exactly where we left off

The AI must:
- Use PowerShell paste-safe scripts only
- Build toward FastAPI + React not Gradio
- Think commercially not academically
- Produce unique designs not generic AI output
- Always test before suggesting

---

## IMMEDIATE NEXT STEPS IN ORDER

1. Wait for v3 Kaggle training to complete - check progress
2. Push v3 model to Hugging Face as Wise222/cvforge-model-v3
3. Install Node.js and create-react-app for frontend
4. Install FastAPI uvicorn for backend
5. Build FastAPI backend with model endpoint
6. Build React frontend CV form
7. Connect frontend to backend
8. Build WeasyPrint PDF templates
9. Test full flow end to end
10. Deploy to Railway free hosting

---

## COMMERCIAL ROADMAP

Month 1: Launch MVP with FastAPI and React - free for all users
Month 2: Collect feedback from 100 real users across Africa
Month 3: Add user accounts and CV saving
Month 4: Add premium PDF templates at 2 dollars per download
Month 5: Retrain on Mistral 7B with 50,000 examples
Month 6: Launch B2B product for universities and recruitment agencies
Month 12: Target 10,000 monthly active users
Month 18: Target 50,000 monthly active users across Africa

Revenue targets:
1,000 users paying 2 dollars per month = 2,000 dollars per month
10 universities paying 200 dollars per month = 2,000 dollars per month
50,000 users with 5 percent conversion = 5,000 dollars per month

---

## ACCOUNTS AND CREDENTIALS SUMMARY

GitHub: Wise222 - https://github.com/Wise222/CVForge
Hugging Face: Wise222 - https://huggingface.co/Wise222
Kaggle: goodcontentacademy - https://www.kaggle.com/goodcontentacademy
HF Token: stored in logs folder - do not share publicly
Kaggle token: C:\Users\katam\.kaggle\kaggle.json
PC username: katam
Project root: C:\Users\katam\Projects\CVForge
