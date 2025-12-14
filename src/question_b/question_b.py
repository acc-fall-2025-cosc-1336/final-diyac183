class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

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
    print("Stock Report")
    print("Company Symbol")
    for stock in stock_list:
        print(f"{stock.get_company_name()} {stock.get_symbol()}")
