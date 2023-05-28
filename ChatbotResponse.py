def prepare_response(cursor):
    data = []

    data = product_responses(data, cursor)
    data = color_responses(data, cursor)
    data = size_responses(data, cursor)
    data = category_responses(data, cursor)
    data = shape_responses(data, cursor)

    return data


def product_responses(data, cursor):
    cursor.execute("SELECT * FROM tbl_products_stone")
    results = cursor.fetchall()

    # length responses
    length = len(results)
    data.append(f"There are total {length} products.")
    data.append(f"This website offers a selection of {length} products.")
    # data.append(f"You can find {length} products listed on this website.")
    # data.append(f"There exist {length} products available for purchase on this website.")
    # data.append(f"You'll discover a total of {length} products on this website.")

    # availability responses
    for product in results:
        id_, name, price, description, image, *rest = product
        price = int(price)
        data.append(f"We have {name} and it's price is Rs: {price}.")
        data.append(f"Indeed, {name} can be obtained and its cost is Rs: {price}.")
        data.append(f"Affirmative, {name} is accessible you can buy it at Rs: {price}.")
        data.append(f"Absolutely, {name} is ready for purchase at Rs: {price}.")
        data.append(f"Yes, {name} is on offer with the price of Rs: {price}.")
        data.append(f"Correct, {name} is available for you at the cost of Rs: {price}.")
        data.append(f"True, {name} is present and ready you can buy it at Rs: {price}.")
        data.append(f"Yes, {name} is in supply with the price of Rs: {price}.")
        

    return data



def color_responses(data, cursor):
    cursor.execute("SELECT * FROM tbl_stone_colors")
    results = cursor.fetchall()

    sentence = "We don't have any colors yet"
    if(results):
        sentence = "We have these colors "
        for color in results:
            id_, color_name = color
            sentence += f", {color_name}"
        sentence += "."
    
    data.append(sentence)
    return data



def size_responses(data, cursor):
    cursor.execute("SELECT * FROM tbl_stone_sizes")
    results = cursor.fetchall()

    sentence = "We don't have any sizes yet"
    if(results):
        sentence = "We have these sizes "
        for size in results:
            id_, size_name = size
            sentence += f", {size_name}"
        sentence += "."
    
    data.append(sentence)
    return data



def shape_responses(data, cursor):
    cursor.execute("SELECT * FROM tbl_stone_shapes")
    results = cursor.fetchall()

    sentence = "We don't have any shapes yet"
    if(results):
        sentence = "We have these shapes "
        for shape in results:
            id_, shape_name = shape
            sentence += f", {shape_name}"
        sentence += "."
    
    data.append(sentence)
    return data



def category_responses(data, cursor):
    cursor.execute("SELECT * FROM tbl_stone_categories")
    results = cursor.fetchall()

    sentence = "We don't have any categories yet"
    if(results):
        sentence = "We have these categories "
        for category in results:
            id_, category_name = category
            sentence += f", {category_name}"
        sentence += "."
    
    data.append(sentence)
    return data