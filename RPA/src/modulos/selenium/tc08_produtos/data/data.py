selectors = {
    "products_list": "div.features_items",
    "btn_view_product_1": 'a[href="/product_details/1"]',
}

# Elementos que precisam estar visíveis na página de detalhes do produto
product_details = {
    "product_name": "div.product-information h2",
    "category": "div.product-information p:nth-child(3)",
    "price": "div.product-information span > span",
    "availability": "div.product-information p:nth-child(6) > b",
    "condition": "div.product-information p:nth-child(7) > b",
    "brand": "div.product-information p:nth-child(8) > b",
}
