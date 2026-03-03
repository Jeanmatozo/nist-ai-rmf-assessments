# RAG/LLM Federal AI Inventory Example

This is a filled-out version of the [Federal AI Inventory Template](../templates/federal_ai_inventory_template.md) for a hypothetical US federal contractor (GovCon) deploying AI systems, including RAG/LLM tools. It demonstrates OMB-compliant tracking with NIST RMF mappings and OWASP considerations, aiding audits and SEC disclosures.

## 1. Organization Overview
- **Entity**: Fictional GovCon Firm (e.g., supporting DoD)
- **Inventory Date**: 2026-03-03
- **Responsible Owner**: AI Governance Lead
- **Scope**: All active AI systems in operations
- **Total AI Systems Inventoried**: 3

## 2. AI System Inventory

| System ID | System Name | Description | Deployment Status (Active/Planned/Decommissioned) | Impact Classification (OMB: Rights/Safety) | Key Vulnerabilities (OWASP LLM Top 10) | RMF Mapping Summary | Linked Assessment/Risk Register | Notes (e.g., SEC Disclosure Implications) |
|-----------|-------------|-------------|-------------------------------------------|--------------------------------------------|----------------------------------------|---------------------|--------------------------------|-------------------------------------------|
| SYS-001 | Enterprise RAG Chatbot | RAG-based LLM for internal document queries. | Active | Rights: Yes (Privacy in data retrieval); Safety: Yes (Decision-support). | LLM01 Prompt Injection, LLM02 Data Poisoning. | Govern: Policies enforced; Map: Threats identified; Measure: Injection tests; Manage: Guards implemented. (Refs: Govern 1.2, Measure 3.1). | [rag_llm_impact_assessment.md](../examples/rag_llm_impact_assessment.md), [rag_llm_risk_register.md RISK-001](../examples/rag_llm_risk_register.md). | High privacy risk; disclose in SEC filings if material to operations. |
| SYS-002 | Fraud Detection ML Model | Supervised ML for transaction anomaly detection. | Active | Rights: Yes (Equity in scoring); Safety: No. | N/A (Non-LLM). | Govern: Accountability defined; Map: Bias risks mapped; Measure: Fairness metrics; Manage: Annual reviews. (Refs: Measure 3.3). | [ai_impact_assessment_template.md filled for this system]. | Bias could lead to regulatory exposure; monitor for insurability. |
| SYS-003 | Predictive Maintenance AI | IoT-based predictive model for equipment. | Planned | Rights: No; Safety: Yes (Physical safety). | LLM06 Sensitive Disclosure (if integrated). | Govern: Thresholds set; Map: Stakeholders; Measure: Accuracy tests; Manage: Rollback plans. (Refs: Manage 4.2). | [prompt_injection_rmf_analysis.md for related vulns](../examples/prompt_injection_rmf_analysis.md). | Safety-impacting; ensure OMB assessment before deployment. |

## 3. Summary Metrics
- **Rights-Impacting Systems**: 2 / 67%
- **Safety-Impacting Systems**: 2 / 67%
- **High-Risk Systems**: 1 (SYS-001 due to active vulns)
- **Compliance Gaps**: SYS-003 lacks full assessment—prioritize.

## 4. Governance & Approval
- **Inventory Process**: Quarterly automated scan integrated with CMMC tools.
- **Mitigation Roadmap**: Address SYS-001 vulns by Q2; use stride-gpt for threat models.
- **Approver**: Jean Matozo / AI Security Engineer
- **Date**: 2026-03-03
- **Review Cadence**: Quarterly

This example reduces audit risks by providing a clear, RMF-aligned inventory for federal reporting.
