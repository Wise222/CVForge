# CVForge - Progress Tracker
**Last Updated:** 2026-04-21 21:30

Legend: [ ] Not Started | [~] In Progress | [x] Done

## PHASE 0 - Foundation
- [ ] P0-01 | Install Python 3.10+
- [ ] P0-02 | Install Git and create GitHub account
- [ ] P0-03 | Create Hugging Face account and get API token
- [ ] P0-04 | Create Google account and access Google Colab
- [ ] P0-05 | Create Kaggle account and get API token
- [ ] P0-06 | Install VS Code
- [ ] P0-07 | Install project Python dependencies
- [ ] P0-08 | Initialize Git repo and push to GitHub
- [ ] P0-09 | Connect Google Drive to Colab

## PHASE 1 - Data Collection
- [ ] P1-01 | Download Kaggle dataset snehaanbhawal/resume-dataset
- [ ] P1-02 | Download Kaggle dataset gauravduttakiit/resume-dataset
- [ ] P1-03 | Download GitHub CV datasets
- [ ] P1-04 | Write clean_data.py
- [ ] P1-05 | Write format_pairs.py
- [ ] P1-06 | Generate 500 synthetic CVs with Claude
- [ ] P1-07 | Split data 80/10/10
- [ ] P1-08 | Validate minimum 400 training pairs
- [ ] P1-09 | Upload dataset to Hugging Face Hub

## PHASE 2 - Fine-Tuning
- [ ] P2-01 | Create finetune_cvforge.ipynb
- [ ] P2-02 | Load Mistral 7B with QLoRA
- [ ] P2-03 | Configure LoRA parameters
- [ ] P2-04 | Run first epoch - confirm no errors
- [ ] P2-05 | Run full 3-epoch training
- [ ] P2-06 | Save weights to Google Drive
- [ ] P2-07 | Upload model to Hugging Face Hub

## PHASE 3 - Evaluation
- [ ] P3-01 | Write evaluate.py
- [ ] P3-02 | Define 5 scoring criteria
- [ ] P3-03 | Test on 5 industries
- [ ] P3-04 | Test on 3 experience levels
- [ ] P3-05 | Target average score 4/5
- [ ] P3-06 | Identify failure patterns
- [ ] P3-07 | Retrain if below 4/5

## PHASE 4 - App Development
- [ ] P4-01 | Write JSON templates for 10 industries
- [ ] P4-02 | Build Gradio UI
- [ ] P4-03 | Connect form to model
- [ ] P4-04 | Add PDF export
- [ ] P4-05 | Add CV style selector
- [ ] P4-06 | Add industry dropdown
- [ ] P4-07 | Test full user flow

## PHASE 5 - Deployment
- [ ] P5-01 | Deploy to Hugging Face Spaces
- [ ] P5-02 | Write public README
- [ ] P5-03 | Package with Ollama for local use
- [ ] P5-04 | Share on GitHub Reddit LinkedIn

## PHASE 6 - Iteration
- [ ] P6-01 | Collect feedback from 10 users
- [ ] P6-02 | Add training data from failures
- [ ] P6-03 | Retrain with improved dataset
- [ ] P6-04 | Add French support
- [ ] P6-05 | Add Swahili support
- [ ] P6-06 | Add cover letter generation

## SESSION LOG
| Date | What Was Done | Next Step |
|------|--------------|-----------|
| 2026-04-21 | Project created | Install Python and tools (P0-01) |
