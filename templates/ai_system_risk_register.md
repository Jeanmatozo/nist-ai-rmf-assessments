# AI System Risk Register Template

This risk register is derived from NIST AI Risk Management Framework (AI RMF 1.0), the NIST AI RMF Playbook, and US federal guidance for rights- and safety-impacting AI systems (e.g., OMB M-24-10 legacy guidance). It helps document and mitigate AI risks, supporting federal inventories, audits, insurance requirements, and SEC AI risk disclosures. Use this to map technical vulnerabilities (e.g., OWASP LLM Top 10) to RMF functions and quantify impacts for regulatory compliance.

## 1. System Overview
- **System Name**: **[e.g., RAG-Based Customer Chatbot]**
- **Description**: **[Brief overview, e.g., LLM with RAG for query responses in a US bank.]**
- **Deployment Context**: **[US federal agency / GovCon / Public company]**
- **Impact Classification** (OMB-Aligned):
  - **Rights-Impacting**: **[Yes/No – Justification: Affects privacy/equity?]**
  - **Safety-Impacting**: **[Yes/No – Justification: Influences safety decisions?]**

## 2. Risk Register

| Risk ID | Risk Category | Description | Likelihood (High/Med/Low) | Impact (High/Med/Low) | OMB Impact (Rights/Safety) | RMF Mapping (Functions/Refs) | Mitigation Strategies | Residual Risk (High/Med/Low) |
|---------|---------------|-------------|----------------------------|------------------------|-----------------------------|------------------------------|-----------------------|------------------------------|
| RISK-001 | **[e.g., Data Security]** | **[e.g., Prompt Injection leading to data exfiltration in RAG system.]** | **[High]** | **[High – Privacy breaches, SEC fines.]** | **[Rights – Affects civil liberties.]** | **[Govern 1.2 (Policies), Map 2.1 (Threats), Measure 3.1 (Tests), Manage 4.3 (Monitoring).]** | **[Input sanitization, prompt hardening, runtime guards.]** | **[Low]** |
| RISK-002 | **[e.g., Model Integrity]** | **[e.g., Data Poisoning in RAG knowledge base causing biased outputs.]** | **[Med]** | **[High – Discriminatory outcomes, regulatory exposure.]** | **[Rights – Equity issues; Safety – Harmful decisions.]** | **[Govern 1.1 (Accountability), Map 2.4 (Supply chain), Measure 3.3 (Bias metrics), Manage 4.1 (Response).]** | **[Source verification, integrity checks, diverse data audits.]** | **[Med]** |
| RISK-003 | **[e.g., Output Reliability]** | **[e.g., Hallucinations leading to misleading information.]** | **[Med]** | **[Med – Loss of trust, operational errors.]** | **[Safety – Psychological/financial harm.]** | **[Govern 1.4 (Thresholds), Map 2.2 (Stakeholders), Measure 3.2 (Accuracy), Manage 4.2 (Remediation).]** | **[Confidence scoring, human-in-loop review.]** | **[Low]** |

*Add rows as needed for additional risks. Reference OWASP LLM Top 10 for vulnerability inspiration.*

## 3. Mitigation & Monitoring Summary
- **Overall Risk Tolerance**: **[e.g., No high-residual risks for rights-impacting systems per OMB.]**
- **Monitoring Approach**: **[e.g., Quarterly reviews, automated alerts for Measure metrics.]**
- **SEC Tie-In**: **[Quantify financial implications, e.g., High-impact risks could lead to material disclosures in 10-K filings.]**

## 4. Approval & Review
- **Assessor**: **[Name / Role]**
- **Date**: **[YYYY-MM-DD]**
- **Review Cadence**: **[Quarterly / Event-Driven]**
- **Next Review Date**: **[YYYY-MM-DD]**

This template can be used standalone or integrated with the [AI Impact Assessment Template](ai_impact_assessment_template.md) for comprehensive governance.
