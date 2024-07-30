chk_grade=(lambda grade: "A grade" if grade>70 else("B grade" if grade<40 else "C grade" if grade<40 else "pass"))
print(chk_grade(80)) #A grade
print(chk_grade(50)) # B grade
print(chk_grade(37)) # Pass
print(chk_grade(45)) # C Grade
