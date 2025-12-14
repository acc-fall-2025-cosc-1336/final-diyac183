from question_b import get_stock_list, display_stock_list

def main():
    stock_list = get_stock_list()
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_stock_list(stock_list)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def display_stock_list(stock_list):
    print("Stock Report")
    print("Company Symbol")
    for stock in stock_list:
        print(f"{stock.get_company_name()} {stock.get_symbol()}")


if __name__ == "__main__":
    main()
