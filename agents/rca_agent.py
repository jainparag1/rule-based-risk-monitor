def rca_agent(dq_issues, risk_issues):
    if dq_issues:
        return "Data pipeline or ingestion issue"

    if risk_issues:
        return "Abnormal transaction behavior detected"

    return "No issue detected"