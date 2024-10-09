import os
import json

# Paths to your cards directory and order file
cards_dir = '/cards'
order_file = '/order.json'
cards_data = {}
ordered_types = []

# Load the specified order from the JSON file
with open(order_file, 'r') as f:
    order_data = json.load(f)
    ordered_types = order_data.get('order', [])

# Recursively scan the directory for cards
for root, dirs, files in os.walk(cards_dir):
    card_type = os.path.basename(root)
    if card_type != 'cards':  # Avoid including the root directory itself
        cards_data[card_type] = []
        for file in files:
            if file.endswith('.jpeg'):
                cards_data[card_type].append(file)

# Create a new dictionary to hold cards in the specified order
ordered_cards_data = {}
for card_type in ordered_types:
    if card_type in cards_data:
        ordered_cards_data[card_type] = cards_data[card_type]

# Include any remaining card types that weren't specified in the order
for card_type, files in cards_data.items():
    if card_type not in ordered_types:
        ordered_cards_data[card_type] = files

# Write the ordered data to a JSON file
with open('../cards.json', 'w') as f:
    json.dump(ordered_cards_data, f, indent=4)
