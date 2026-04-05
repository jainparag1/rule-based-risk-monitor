def risk_agent(data):
    issues = []

    if data['amount'].std() > 7000:
        issues.append("High transaction volatility")

    if data['amount'].max() > 18000:
        issues.append("Potential high-value fraud transaction")

    return issues