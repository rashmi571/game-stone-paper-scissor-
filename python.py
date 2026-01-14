s=input("enter string: ")

special_count=0
letter_count=0
space_count=0

for char in s:
    if char == " ":
        space_count += 1
    elif char.isalpha():
        letter_count += 1
    else:
        special_count += 1         


print(f"{special_count} -> special symboles in string\n {letter_count} -> letters in string\n {space_count} -> space in string")