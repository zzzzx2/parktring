def best_price(prices):
    """Devuelve el precio más bajo de la lista."""
    cheapest = prices[0]
    for price in prices:
        if price < cheapest:
            cheapest = price
    return cheapest

def run():
    text = input("Enter prices separated by commas: ")
    prices = [float(p) for p in text.split(",")]
    print("The best price is:", best_price(prices), "€")

if __name__ == "__main__":
    run()
