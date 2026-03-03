# Federal AI Inventory Template

This inventory template aligns with US federal mandates (OMB M-24-10 legacy guidance) for tracking AI systems, especially rights- and safety-impacting ones. It integrates NIST AI RMF 1.0 for risk management and supports SEC disclosures by identifying potential "AI Washing" gaps. Use this to document deployments, reference assessments from [AI Impact Assessment Template](ai_impact_assessment_template.md), and link risks from [AI System Risk Register](ai_system_risk_register.md). Not an official form—practical artifact for audits/insurance.

## 1. Organization Overview
- **Entity**: **[e.g., US Federal Agency / GovCon Firm / Public Company]**
- **Inventory Date**: **[YYYY-MM-DD]**
- **Responsible Owner**: **[Name / Role, e.g., Chief AI Officer]**
- **Scope**: **[e.g., All deployed AI systems in finance operations; excludes prototypes.]**
- **Total AI Systems Inventoried**: **[Number]**

## 2. AI System Inventory

| System ID | System Name | Description | Deployment Status (Active/Planned/Decommissioned) | Impact Classification (OMB: Rights/Safety) | Key Vulnerabilities (OWASP LLM Top 10) | RMF Mapping Summary | Linked Assessment/Risk Register | Notes (e.g., SEC Disclosure Implications) |
|-----------|-------------|-------------|-------------------------------------------|--------------------------------------------|----------------------------------------|---------------------|--------------------------------|-------------------------------------------|
| SYS-001 | **[e.g., Customer RAG Chatbot]** | **[e.g., RAG-based LLM for query responses.]** | **[Active]** | **[Rights: Yes (Privacy); Safety: Yes (Financial decisions).]** | **[e.g., LLM01 Prompt Injection, LLM02 Data Poisoning.]** | **[Govern: Policies defined; Map: Risks identified; Measure: Metrics in place; Manage: Monitoring active. (Refs: Govern 1.1, Map 2.1).]** | **[Link to ai_impact_assessment.md or RISK-001.]** | **[e.g., High risk requires 10-K disclosure if material.]** |
| SYS-002 | **[e.g., Predictive Analytics Tool]** | **[e.g., ML model for fraud detection.]** | **[Planned]** | **[Rights: Yes (Equity); Safety: No.]** | **[e.g., LLM03 Model Denial of Service.]** | **[Govern: Accountability set; Map: Stakeholders mapped; Measure: Bias tests; Manage: Response plans. (Refs: Measure 3.3).]** | **[Link to risk register entry.]** | **[e.g., Inventory gap could affect insurability.]** |

*Add rows for each AI system. Classify per OMB: Rights-impacting if affects civil rights/privacy; Safety-impacting if influences harm.*

## 3. Summary Metrics
- **Rights-Impacting Systems**: **[Count / Percentage]**
- **Safety-Impacting Systems**: **[Count / Percentage]**
- **High-Risk Systems**: **[Count – e.g., Those with unmitigated OWASP vulns.]**
- **Compliance Gaps**: **[e.g., Systems without full RMF mapping: List IDs.]**

## 4. Governance & Approval
- **Inventory Process**: **[e.g., Annual scan using automated tools; cross-referenced with CMMC controls.]**
- **Mitigation Roadmap**: **[e.g., Prioritize rights-impacting systems for Q2 audits.]**
- **Approver**: **[Name / Role]**
- **Date**: **[YYYY-MM-DD]**
- **Review Cadence**: **[Annual / Bi-Annual]**

This template reduces liability by enabling proactive federal reporting and SEC-ready risk quantification.
