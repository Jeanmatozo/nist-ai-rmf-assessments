# NIST AI RMF Mappings & Assessments

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This repository demonstrates practical mappings of AI vulnerabilities (e.g., OWASP LLM Top 10) to the NIST AI Risk Management Framework (RMF) 1.0. It focuses on US federal mandates (OMB M-24-10 legacy guidance for rights- and safety-impacting AI systems) and helps reduce liability under SEC AI disclosure rules. As an AI security professional, I use these artifacts to translate technical risks in RAG/LLM systems into governance tools that support audits, insurance requirements, and compliance in GovCon/finance sectors.

Key Value: Hiring managers—scan this in <2 minutes to see how I can inventory AI systems, perform impact assessments, and automate RMF checks to mitigate "AI Washing" risks.

## Contents
### `templates/`
Reusable Markdown templates for:

- **AI Impact Assessments**  
  OMB-aligned templates for evaluating rights- and safety-impacting AI systems.
- **AI System Risk Registers**  
  Risk registers with explicit NIST AI RMF mappings and OWASP LLM Top 10 integration.
- **Federal AI Inventories**  
  Inventory formats suitable for OMB-compliant tracking and SEC-aligned disclosures.

---

### `examples/`
Practical, real-world examples for **LLM and RAG systems**, including:

- Vulnerability mappings (OWASP LLM Top 10 → NIST AI RMF: Govern / Map / Measure / Manage)
- Filled-out AI Impact Assessments and Risk Registers
- Example Federal AI Inventory entries
- Threat modeling artifacts for risks such as prompt injection and context poisoning

---

### `automation/`
Lightweight Python scripts to support **basic RMF alignment checks**.

- No external dependencies required
- Intended to demonstrate repeatability and governance automation concepts

---

## Quick Demo

```bash
git clone https://github.com/Jeanmatozo/nist-ai-rmf-assessments.git
```

Run automation: 
`cd automation
python rmf_alignment_checks.py --input ../examples/rag_llm_rmf_mapping.md
`
Alternatively, browse the examples directly on GitHub to quickly review RMF mappings and compliance artifacts.

## Why This Matters for US Compliance
- **NIST AI RMF**:   
Provides structured AI risk management across the Govern, Map, Measure, and Manage functions.
- **OMB M-24-10 Legacy**:   
Reinforces the need for inventories and impact assessments for rights- and safety-impacting AI systems, especially for federal agencies and contractors.
- **SEC Scrutiny**:  
Requires accurate mapping of technical AI vulnerabilities to material financial and reputational risks to avoid enforcement actions and misleading disclosures.


Built by [LinkedIn](https://www.linkedin.com/in/jean-akingeneye-00500213/). Contributions welcome for US-centric expansions.
