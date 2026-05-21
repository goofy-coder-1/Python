# =============================================================
#               M A I N   A P P L I C A T I O N
# =============================================================

from maths import calculatePercentage, get_highest_score

print("===== Testing Module Imports ========")

marks_obtained = 425
total_marks = 500

final_percentage = calculatePercentage(marks_obtained, total_marks)

print(f"Exam Result: {final_percentage}%")

top_student = get_highest_score(50, 40, 80, 70)
print(f"Highest Score: {top_student} %")