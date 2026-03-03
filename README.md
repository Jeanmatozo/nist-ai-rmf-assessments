# NIST AI RMF Mappings & Assessments

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This repository demonstrates practical mappings of AI vulnerabilities (e.g., OWASP LLM Top 10) to the NIST AI Risk Management Framework (RMF) 1.0. It focuses on US federal mandates (OMB M-24-10 legacy guidance for rights- and safety-impacting AI systems) and helps reduce liability under SEC AI disclosure rules. As an AI security professional, I use these artifacts to translate technical risks in RAG/LLM systems into governance tools that support audits, insurance requirements, and compliance in GovCon/finance sectors.

Key Value: Hiring managers—scan this in <2 minutes to see how I can inventory AI systems, perform impact assessments, and automate RMF checks to mitigate "AI Washing" risks.

## Contents
- **templates/**: Reusable Markdown templates for AI Impact Assessments and Risk Registers (aligned with OMB rights/safety-impacting systems).
- **examples/**: Applied mappings for RAG/LLM systems, e.g., threat modeling prompt injection to RMF functions (Govern/Map/Measure/Manage). Examples now include filled-out assessments for RAG systems
- **automation/**: Python scripts for basic RMF alignment checks (no dependencies; run with `python rmf_alignment_checks.py`).

## Quick Demo
1. Clone: `git clone https://github.com/Jeanmatozo/nist-ai-rmf-assessments.git`
2. Run automation: `cd automation && python rmf_alignment_checks.py --input ../examples/rag_llm_rmf_mapping.md`
3. View examples in browser for RMF mappings.

## Why This Matters for US Compliance
- **NIST AI RMF**: Core framework for managing AI risks.
- **OMB M-24-10 Legacy**: Requires assessments for rights/safety-impacting AI.
- **SEC Scrutiny**: Maps vulnerabilities to financial risk disclosures.

Built by [Your Name/LinkedIn]. Contributions welcome for US-centric expansions.
