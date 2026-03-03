# RAG/LLM Impact Assessment Example

This is a filled-out version of the [AI Impact Assessment Template](../templates/ai_impact_assessment_template.md) for a hypothetical Retrieval-Augmented Generation (RAG) LLM system in a US bank (finance sector, subject to SEC disclosures).

## 1. System Overview
- **System Name**: Customer Service Chatbot
- **System Description**: RAG-based LLM for handling customer queries on account balances and transactions.
- **Deployment Context**: US public company (bank)
- **Operational Role**: Customer-facing
- **Safety-Impacting AI**: Yes – influences financial decisions

## 2. Impact Classification (OMB-Aligned)
- **Rights-Impacting AI**: Yes
  - **Justification**: Affects privacy (access to personal data) and equity (potential bias in responses).
- **Safety-Impacting AI**: Yes
  - **Justification**: Influences financial safety (e.g., advice on loans could lead to economic harm).

## 3. Risk Identification & Potential Impacts
### 3.1 Identified Risk Scenarios

| Risk Category | Description | Potential Impact |
|---------------|-------------|------------------|
| **Rights Impact** | Biased responses based on training data | Discriminatory service denial, SEC scrutiny |
| **Safety Impact** | Hallucinated transaction info | Financial loss, loss of trust |
| **Data Risk** | Prompt injection leading to data exfiltration | Privacy breaches, regulatory fines |

## 4. Risk Mapping to NIST AI RMF
### 4.1 RMF Function Alignment
- **GOVERN**
  - Defined accountability: AI ethics board oversees deployment.
  - Documented thresholds: Bias <5% variance.  
    *(Ref: GOVERN 1.1, 1.2)*

- **MAP**
  - Stakeholders: Customers, regulators.
  - Classification: Rights- and safety-impacting.  
    *(Ref: MAP 2.2, 2.3)*

- **MEASURE**
  - Metrics: F1-score for accuracy, fairness audits.
  - Vulnerabilities: OWASP LLM01 (Prompt Injection).  
    *(Ref: MEASURE 3.1, 3.3)*

- **MANAGE**
  - Monitoring: Real-time logging.
  - Remediation: Auto-flags for human review.  
    *(Ref: MANAGE 4.1, 4.2)*

## 5. System Inventory & Technical Scope
- **Data Sources**: Internal transaction DB, public FAQs.
- **Models Used**: GPT-4o, hosted on Azure.
- **Known Vulnerabilities Considered**: OWASP LLM Top 10: Prompt Injection, Data Poisoning.

## 6. Mitigation & Control Summary

| Risk | Control Implemented | Residual Risk |
|------|----------------------|---------------|
| Prompt Injection | Sanitization filters | Low |
| Data Poisoning | Verified sources only | Low |
| Bias | Diverse training data | Medium |

## 7. Approval & Accountability
- **Assessor**: Jean Matozo / AI Security Engineer
- **Date**: 2026-03-03
- **Review Cadence**: Quarterly
