import os
import json

cards_dir = 'cards'
order_file = 'order.json'
cards_data = {}
ordered_types = []

with open(order_file, 'r') as f:
    order_data = json.load(f)
    ordered_types = order_data.get('order', [])

for root, dirs, files in os.walk(cards_dir):
    card_type = os.path.basename(root)
    if card_type != 'cards':
        cards_data[card_type] = []
        for file in files:
            if file.endswith('.jpeg'):
                cards_data[card_type].append(file)

ordered_cards_data = {}
for card_type in ordered_types:
    if card_type in cards_data:
        ordered_cards_data[card_type] = cards_data[card_type]

for card_type, files in cards_data.items():
    if card_type not in ordered_types:
        ordered_cards_data[card_type] = files

with open('../cards.json', 'w') as f:
    json.dump(ordered_cards_data, f, indent=4)
