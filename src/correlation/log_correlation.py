from collections import Counter
import re

def correlate_logs(chunks):
    error_patterns = []

    for chunk in chunks:
        matches = re.findall(r"(error|failed|timeout|exception)", chunk.lower())
        error_patterns.extend(matches)

    counter = Counter(error_patterns)

    return {
        "total_errors": sum(counter.values()),
        "top_patterns": counter.most_common(3)
    }