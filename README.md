# Enterprise IT Asset & Change Management Audit Pipeline

An enterprise-grade technology risk and compliance analytics pipeline designed to automate internal IT auditing. This system parses production change logs, executes custom risk-scoring algorithms, and flags critical compliance violations against global frameworks such as **COBIT**, **ISO 27001**, and **NCA (National Cybersecurity Authority)** controls.

## Strategic Audit Capabilities
The automated pipeline monitors and evaluates corporate governance through programmatic rules:
1. **Segregation of Duties (SoD) Verification:** Automatically detects unauthorized change logs where system developers bypass corporate controls by approving their own production deployments.
2. **Critical Control Failure Detection:** Flags highly critical systems deployed under emergency windows without passing User Acceptance Testing (UAT) or receiving proper IT management authorization.
3. **High-Density Risk Profiling:** Scores production risk based on infrastructure tier criticality combined with compounding compliance failure penalties, mapped down to individual change events.

## Project Structure
- `it_audit_logs.csv`: Expanded corporate dataset simulating 50 production system change events.
- `audit_pipeline.py`: Core analytical engine executing the compliance auditing rules.
- `advanced_it_audit_risk_profile.png`: Advanced high-density risk distribution chart layering boxplots and individual change events.
- `README.md`: Professional technical documentation.

## Technical Frameworks Used
- **Python 3.12**
- **Pandas** (Corporate data governance & feature extraction)
- **Matplotlib & Seaborn** (Publication-quality statistical visualization) 