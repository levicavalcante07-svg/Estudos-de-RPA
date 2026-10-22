import csv

from src.shared.config import output_file


class DataHandler:
    def __init__(self, data):
        self.items = data

    def max_min(self):
        # Os preços vêm no formato "Rs. 500"
        all_prices = [float(product["price"].split()[1]) for product in self.items]
        return max(all_prices), min(all_prices)

    def save_to_csv(self, filename):
        path = output_file(filename)
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "id", "href"])
            writer.writeheader()
            writer.writerows(self.items)
        return path
