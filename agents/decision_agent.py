def decision_agent(dq_issues, risk_issues):
    if dq_issues or risk_issues:
        return "ALERT"
    return "IGNORE"