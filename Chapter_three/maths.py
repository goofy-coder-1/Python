# =============================
# MATH FORMULAS
# =============================

def calculatePercentage(part, total):
    if total == 0:
        return 0
    return (part/total)*100

def get_highest_score(*scores):
    if not scores:
        return 0
    return max(scores)