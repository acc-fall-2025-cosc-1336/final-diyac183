#add import
from question_a import create_multiplication_table, display_multiplication_table

while True:
    table = create_multiplication_table()
    display_multiplication_table(table)
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break