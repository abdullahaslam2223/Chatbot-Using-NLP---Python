def prepare_response(cursor):
    data = []

    data = product_response(data, cursor)

    return data


def product_response(data, cursor):
    cursor.execute("select * from tbl_products_stone")
    results = cursor.fetchall()

    # length responses
    length = len(results)
    data.append(f"There are total {length} products.")
    data.append(f"This website offers a selection of {length} products.")
    data.append(f"You can find {length} products listed on this website.")
    data.append(f"There exist {length} products available for purchase on this website.")
    data.append(f"You'll discover a total of {length} products on this website.")

    # availability responses
    for product in results:
        id_, name, price, description, image, *rest = product
        data.append(f"Yes, {name} is available.")

    return data