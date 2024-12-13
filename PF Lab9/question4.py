items = {
    "apple": 3,
    "banana": 1,
    "orange": 2,
    "grape": 4,
    "mango": 5
}
stock = set(items.keys())
sold_items_prices = []

def purchase_item(item):
    if item in stock:
        stock.remove(item)
        sold_items_prices.append(items[item])
        print(f"{item.capitalize()} purchased for ${items[item]}")
    else:
        print(f"{item.capitalize()} is out of stock or already purchased.")
# Example purchases
purchase_item("apple")
purchase_item("banana")
purchase_item("mango")
purchase_item("orange")
# Calculate total amount, max, and min
if sold_items_prices:
    total_amount = sum(sold_items_prices)
    max_amount = max(sold_items_prices)
    min_amount = min(sold_items_prices)
    
    print("\nSummary:")
    print(f"Total amount of items sold: ${total_amount}")
    print(f"Maximum item price sold: ${max_amount}")
    print(f"Minimum item price sold: ${min_amount}")
else:
    print("No items were sold.")
