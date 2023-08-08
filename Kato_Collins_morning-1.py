import tkinter as tk

def add_item():
    item = item_entry.get()
    price = float(price_entry.get())
    items.append((item, price))
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    update_item_list()

def update_item_list():
    item_list.delete(0, tk.END)
    total = 0.0
    for item, price in items:
        item_list.insert(tk.END, f"{item} - ${price:.2f}")
        total += price
    total_label.config(text=f"Total: ${total:.2f}")

def clear_items():
    items.clear()
    update_item_list()

def print_receipt():
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Kato's Receipt")

    receipt_text = tk.Text(receipt_window, height=10, width=30)
    receipt_text.pack()

    receipt_text.insert(tk.END, "----- Receipt -----\n")
    total = 0.0
    for item, price in items:
        receipt_text.insert(tk.END, f"{item} - ${price:.2f}\n")
        total += price
    receipt_text.insert(tk.END, "-------------------\n")
    receipt_text.insert(tk.END, f"Total: ${total:.2f}")

    receipt_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Kato Receipt Printer")

items = []

# Create the item entry and label
item_label = tk.Label(root, text="Item:")
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

# Create the price entry and label
price_label = tk.Label(root, text="Price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Create the "Add" button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Create the item list section
item_list_label = tk.Label(root, text="Added Items:")
item_list_label.pack()
item_list = tk.Listbox(root, height=5)
item_list.pack()

# Create the "Clear" button
clear_button = tk.Button(root, text="Clear Items", command=clear_items)
clear_button.pack()

# Create the total label
total_label = tk.Label(root, text="Total: $0.00")
total_label.pack()

# Create the "Print" button
print_button = tk.Button(root, text="Print Receipt", command=print_receipt)
print_button.pack()

root.mainloop()
