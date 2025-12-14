import sys
sys.path.append('../..')
from question_b import Stock
def get_stock_list():
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    return stocks


def display_stock_list(stock_list):
    print("\n--- Stock List ---")
    print(f"{'Symbol':<10} {'Company Name':<20}")
    print("-" * 30)
    for stock in stock_list:
        print(f"{stock.get_symbol():<10} {stock.get_company_name():<20}")
    print()


def main():
    stock_list = get_stock_list()
    
    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            display_stock_list(stock_list)
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()