# Prompt Injection RMF Analysis Example

This example provides a detailed analysis of OWASP LLM01 (Prompt Injection) vulnerability in a RAG/LLM system, mapped to NIST AI RMF 1.0. It uses elements from the [AI System Risk Register Template](../templates/ai_system_risk_register.md) and [AI Impact Assessment Template](../templates/ai_impact_assessment_template.md) to show how to mitigate rights-impacting risks, supporting US federal mandates (OMB M-24-10) and SEC risk disclosures.

## Vulnerability Overview
- **Description**: Adversaries inject malicious prompts to hijack LLM behavior, potentially extracting sensitive data or generating harmful outputs in RAG setups.
- **Impact Classification** (OMB-Aligned): Rights-Impacting (High – privacy breaches); Safety-Impacting (Medium – could lead to unsafe recommendations).
- **Threat Model** (STRIDE-Inspired): Spoofing/Tampering via user inputs; Elevation of privilege if overrides controls.
- **Why Analyze This?**: Common in LLMs; mapping to RMF helps reduce regulatory exposure (e.g., SEC fines for undisclosed AI risks).

## Risk Register Excerpt

| Risk ID | Description | Likelihood | Impact | RMF Mapping | Mitigation | Residual Risk |
|---------|-------------|------------|--------|-------------|------------|---------------|
| RISK-001 | Prompt injection via user queries in RAG, leading to data exfiltration or biased responses. | High | High (Rights-impacting: Privacy/equity violations; potential SEC liability). | Govern 1.2 (Policies), Map 2.1 (Surfaces), Measure 3.1 (Tests), Manage 4.3 (Guards). | Input sanitization, prompt hardening, least-privilege design. | Low |

## Detailed RMF Function Alignment
- **GOVERN**
  - Establish organizational policies for prompt engineering and validation thresholds (e.g., no unfiltered user inputs).  
    *(Ref: Govern 1.2 – Accountability structures; ties to OMB rights protections).*

- **MAP**
  - Identify contextual risks, such as RAG retrieval amplifying injections, and affected stakeholders (e.g., end-users, regulators).  
    *(Ref: Map 2.1 – Risks and benefits; Map 2.3 – TEVV planning).*

- **MEASURE**
  - Define metrics like injection success rate (<1%) and use adversarial testing (e.g., red teaming prompts). Evaluate with tools like OWASP benchmarks.  
    *(Ref: Measure 3.1 – Trustworthiness metrics; supports insurance audits).*

- **MANAGE**
  - Implement continuous monitoring (e.g., anomaly detection in outputs) and incident response plans for detected injections.  
    *(Ref: Manage 4.3 – Monitoring and reporting; reduces financial risks for SEC filings).*

## Mitigation Implementation Notes
- **Technical Controls**: Use libraries like NeMo Guardrails for runtime checks.
- **Compliance Value**: This analysis can feed into federal AI inventories, proving proactive risk management to avoid "AI Washing" scrutiny.
- **Testing Demo**: Run adversarial prompts in a sandbox; measure pre/post-mitigation effectiveness.

For broader mappings, see [RAG/LLM System RMF Mapping](../examples/rag_llm_rmf_mapping.md).
