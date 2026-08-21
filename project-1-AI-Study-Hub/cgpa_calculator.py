print("===== CGPA CALCULATOR =====")

total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

percentage = (obtained_marks / total_marks) * 100

cgpa = (percentage / 100) * 4

print("\nPercentage =", percentage)
print("CGPA =", round(cgpa, 2))
