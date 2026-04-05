def dq_agent(data):
    issues = []

    if data.isnull().sum().sum() > 0:
        issues.append("Null values detected")

    if data['amount'].mean() > 15000:
        issues.append("Unusually high average transaction value")

    if len(data) == 0:
        issues.append("Empty batch received")

    return issues