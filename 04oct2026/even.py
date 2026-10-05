# Input: Enter the student's roll number
roll_number = int(input("Enter the student's roll number: "))

# Check if the roll number is divisible by 2
if roll_number % 2 == 0:
    print(f"Roll number {roll_number} is Even.")
else:
    print(f"Roll number {roll_number} is Odd.")
