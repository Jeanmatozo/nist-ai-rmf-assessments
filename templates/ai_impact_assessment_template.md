# AI Impact Assessment Template

> This assessment is derived from NIST AI Risk Management Framework (AI RMF 1.0), the NIST AI RMF Playbook, and US federal guidance emphasizing rights- and safety-impacting AI systems (e.g., OMB M-24-10 legacy guidance). It is intended as a practical governance artifact, not an official NIST form.

## 1. System Overview
[Example: Customer Service Chatbot]

**System Description:**  
[Brief description of functionality, e.g., Retrieval-Augmented Generation (RAG)
LLM providing automated responses to customer inquiries.]

**Deployment Context:**  
[US federal agency / Federal contractor / US public company]

**Operational Role:**  
[Decision-support / Customer-facing / Internal efficiency / Mixed-use][Yes/No – e.g., influences physical safety decisions]

---

## 2. Impact Classification (OMB-Aligned)

**Rights-Impacting AI:**  
[Yes / No]  
*Justification:*  
[Explain whether the system affects privacy, equity, access to services,
civil rights, or due process.]

**Safety-Impacting AI:**  
[Yes / No]  
*Justification:*  
[Explain whether the system influences decisions that could affect physical,
financial, or psychological safety.]

---

## 3. Risk Identification & Potential Impacts

### 3.1 Identified Risk Scenarios

| Risk Category | Description | Potential Impact |
|--------------|-------------|------------------|
| Rights Impact | Biased or hallucinated responses | Discriminatory outcomes, regulatory exposure |
| Safety Impact | Incorrect or misleading information | Harmful decisions, loss of trust |
| Data Risk | RAG data poisoning or leakage | Privacy violations, reputational damage |

---

## 4. Risk Mapping to NIST AI RMF
### 4.1 RMF Function Alignment
- **GOVERN**
  - Defined accountability for AI system ownership and oversight
  - Documented acceptable-use and risk tolerance thresholds  
    *(Ref: GOVERN 1.1, 1.2)*

- **MAP**
  - Identified affected stakeholders and contextual risks
  - Classified system as rights- and/or safety-impacting  
    *(Ref: MAP 2.2, 2.3)*

- **MEASURE**
  - Identified metrics for model performance, bias, and failure detection
  - Evaluated known LLM/RAG vulnerabilities  
    *(Ref: MEASURE 3.1, 3.3)*

- **MANAGE**
  - Defined monitoring, incident response, and escalation processes
  - Established remediation and rollback procedures  
    *(Ref: MANAGE 4.1, 4.2)*
---

## 5. System Inventory & Technical Scope
- **Data Sources**: **[Training data sources, RAG knowledge bases, external APIs]**
- **Models Used**: **[Model name/version, hosted vs. self-managed]**
- **Known Vulnerabilities Considered**: **[OWASP LLM Top 10 categories relevant to this system, e.g., Prompt Injection, Data Poisoning, Tool Abuse]**

---

## 6. Mitigation & Control Summary

| Risk | Control Implemented | Residual Risk |
|-----|-------------------|---------------|
| Prompt Injection | Input validation, system prompt hardening | Low |
| RAG Poisoning | Source allowlisting, document review | Medium |
| Hallucinations | Confidence thresholds, human review | Medium |

---

# 7. Approval & Accountability

- **Assessor**: **[Name / Role]**
- **Date**: **[YYYY-MM-DD]**
- **Review Cadence**: **[Quarterly / Semi-Annual / Event-Driven]**
