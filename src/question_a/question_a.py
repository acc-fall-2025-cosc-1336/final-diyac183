#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table():
    table = []
    for row in range(1, 6):  # 1 to 5
        row_list = []
        for col in range(1, 11):  # 1 to 10
            row_list.append(row * col)
        table.append(row_list)
    return table

def display_multiplication_table(table):
    for row in table:
        print(' '.join(map(str, row)))