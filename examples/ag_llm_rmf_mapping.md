# RAG/LLM System RMF Mapping Example

This example maps common OWASP LLM Top 10 vulnerabilities for a Retrieval-Augmented Generation (RAG) LLM system (e.g., an enterprise search tool) to NIST AI RMF 1.0 functions. It demonstrates how to translate technical risks into governance artifacts, reducing US regulatory liability under OMB M-24-10 (rights/safety-impacting AI) and SEC disclosure requirements. For a full impact assessment, see the [AI Impact Assessment Template](../templates/ai_impact_assessment_template.md).

## System Context
- **Description**: RAG-enhanced LLM for querying internal documents, deployed in a US federal contractor environment.
- **Impact Classification** (OMB-Aligned): Rights-Impacting (Yes – potential privacy/equity issues); Safety-Impacting (Yes – could influence operational decisions).
- **Why This Matters**: Maps vulnerabilities to RMF to support federal inventories, audits, and insurance proofs of AI safety.

## Vulnerability Mappings to NIST AI RMF

| OWASP Vulnerability | Description | RMF Govern | RMF Map | RMF Measure | RMF Manage |
|---------------------|-------------|------------|---------|-------------|------------|
| LLM01: Prompt Injection | Attacker manipulates inputs to override behavior or extract data. | Establish input validation policies (Govern 1.2). | Identify prompt-based attack surfaces (Map 2.1). | Test injection success rates; metrics: <1% failure (Measure 3.1). | Runtime guards and logging for incidents (Manage 4.3). |
| LLM02: Insecure Output Handling | Outputs expose sensitive info or enable attacks. | Define output sanitization standards (Govern 1.4). | Map data flows in RAG retrieval (Map 2.4). | Audit outputs for PII leaks; fairness scores (Measure 3.2). | Automated filters and escalation protocols (Manage 4.1). |
| LLM03: Training Data Poisoning | Corrupted RAG sources lead to biased/harmful outputs. | Data governance policies for sources (Govern 1.1). | Assess supply chain risks (Map 2.3). | Integrity checks; bias detection metrics (Measure 3.3). | Source verification and rollback plans (Manage 4.2). |
| LLM06: Sensitive Information Disclosure | LLM reveals confidential data from RAG. | Privacy thresholds in policies (Govern 1.3). | Stakeholder impact analysis (Map 2.2). | Redaction efficacy tests (Measure 3.1). | Monitoring for disclosures; response procedures (Manage 4.1). |

## Key Insights for US Compliance
- **OMB Tie-In**: For rights-impacting systems, these mappings ensure proactive assessments to avoid civil rights violations.
- **SEC Relevance**: Quantifies risks (e.g., poisoning → financial harm from bad decisions) for 10-K disclosures.
- **Residual Risk Reduction**: Implementing these lowers audit exposure; e.g., Measure metrics can prove "insurability" for cyber policies.

This artifact can be automated—see ../automation/rmf_alignment_checks.py for coverage verification.
