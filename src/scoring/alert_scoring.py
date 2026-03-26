def calculate_alert_score(correlation_result):
    score = 0

    total_errors = correlation_result["total_errors"]

    if total_errors > 20:
        score += 50
    elif total_errors > 10:
        score += 30
    elif total_errors > 5:
        score += 20
    else:
        score += 10

    return min(score, 100)


def get_severity(score):
    if score >= 70:
        return "🔴 Critical"
    elif score >= 40:
        return "🟠 High"
    elif score >= 20:
        return "🟡 Medium"
    else:
        return "🟢 Low"