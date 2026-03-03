# RAG/LLM Risk Register Example

This is a filled-out version of the [AI System Risk Register Template](../templates/ai_system_risk_register.md) for a hypothetical Retrieval-Augmented Generation (RAG) LLM system in a US federal contractor (GovCon) setting. It maps OWASP LLM vulnerabilities to NIST AI RMF, supporting OMB inventories and SEC risk management.

## 1. System Overview
- **System Name**: Enterprise RAG Chatbot
- **Description**: LLM with RAG for internal document queries, handling sensitive data.
- **Deployment Context**: US federal contractor (subject to CMMC and OMB mandates)
- **Impact Classification** (OMB-Aligned):
  - **Rights-Impacting**: Yes – Justification: Processes personal data, potential for privacy/equity biases.
  - **Safety-Impacting**: Yes – Justification: Influences decision-support in operations.

## 2. Risk Register

| Risk ID | Risk Category | Description | Likelihood (High/Med/Low) | Impact (High/Med/Low) | OMB Impact (Rights/Safety) | RMF Mapping (Functions/Refs) | Mitigation Strategies | Residual Risk (High/Med/Low) |
|---------|---------------|-------------|----------------------------|------------------------|-----------------------------|------------------------------|-----------------------|------------------------------|
| RISK-001 | Data Security | Prompt Injection allowing unauthorized access in RAG queries. | High | High – Data leaks, regulatory fines. | Rights – Privacy violations. | Govern 1.2 (Policies), Map 2.1 (Threats), Measure 3.1 (Tests), Manage 4.3 (Monitoring). | Input filters, guardrails (e.g., NeMo), logging. | Low |
| RISK-002 | Model Integrity | Data Poisoning corrupting RAG sources, leading to inaccurate outputs. | Med | High – Biased decisions, audit failures. | Rights – Equity; Safety – Operational harm. | Govern 1.1 (Accountability), Map 2.4 (Supply chain), Measure 3.3 (Bias metrics), Manage 4.1 (Response). | Source allowlisting, checksums, periodic audits. | Med |
| RISK-003 | Output Reliability | Sensitive Information Disclosure via LLM outputs. | Med | Med – Reputational damage. | Rights – Civil liberties. | Govern 1.4 (Thresholds), Map 2.2 (Stakeholders), Measure 3.2 (PII detection), Manage 4.2 (Remediation). | Output sanitization, redaction tools. | Low |

## 3. Mitigation & Monitoring Summary
- **Overall Risk Tolerance**: No high-residual risks; align with CMMC Level 2.
- **Monitoring Approach**: Automated scans quarterly, integrated with SIEM.
- **SEC Tie-In**: High-impact risks (e.g., leaks) quantified as potential $X million losses for disclosures.

## 4. Approval & Review
- **Assessor**: Jean Matozo / AI Security Engineer
- **Date**: 2026-03-03
- **Review Cadence**: Quarterly
- **Next Review Date**: 2026-06-03
