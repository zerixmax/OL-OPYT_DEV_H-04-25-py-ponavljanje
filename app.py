# Invoice
invoice_number = "INV-1001"
invoice_date = "2024-06-15"
due_date = "2024-07-15"
client_name = "Acme Corporation"
client_address = "123 Business Rd, Business City, BC 54321"
items = [
    {"description": "Web Design Services", "quantity": 1, "unit_price": 1500.00},
    {"description": "Hosting (12 months)", "quantity": 1, "unit_price": 240.00},
    {"description": "Domain Registration (1 year)", "quantity": 1, "unit_price": 15.00},
]
tax_rate = 0.25  # 25% sales tax
def calculate_totals(items, tax_rate):
    subtotal = sum(item["quantity"] * item["unit_price"] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total
subtotal, tax, total = calculate_totals(items, tax_rate)
print(f"Invoice Number: {invoice_number}")
print(f"Invoice Date: {invoice_date}")
print(f"Due Date: {due_date}")
print(f"Bill To: {client_name}")
print(f"Address: {client_address}\n")
print("Items:")
for item in items:
    print(f"- {item['description']}: {item['quantity']} x ${item['unit_price']:.2f}")
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax (25%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
# Invoice
