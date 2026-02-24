shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
shopping_list.append({"item": "Butter", "price": 80})
shopping_list.pop(0)
print(f"Number of items in the list: {len(shopping_list)}")

total_cost = 0
most_expensive_item = shopping_list[0]

for entry in shopping_list:
    total_cost += entry["price"]
    if entry["price"] > most_expensive_item["price"]:
        most_expensive_item = entry
print(f"Most Expensive Item: {most_expensive_item['item']} at {most_expensive_item['price']}")
print(f"Total Cost: {total_cost}")

average_price = total_cost / len(shopping_list)
summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": round(average_price, 2)
}
print("\nSummary Dictionary:")
print(summary)