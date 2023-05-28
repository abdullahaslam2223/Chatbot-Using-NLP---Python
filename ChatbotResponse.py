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

    # availability responses
    for product in results:
        id_, name, price, description, image, category_id, color_id, weight, shape_id, origin, size_id, hardness, dispersion, gravity, density, quantity = product
        price = int(price)
        # data.append(f"Indeed, {name} can be obtained and its cost is Rs: {price}.")
        # data.append(f"Affirmative, {name} is accessible you can buy it at Rs: {price}.")
        # data.append(f"Absolutely, {name} is ready for purchase at Rs: {price}.")
        # data.append(f"Yes, {name} is on offer with the price of Rs: {price}.")
        # data.append(f"True, {name} is present and ready you can buy it at Rs: {price}.")

        data.append(f"We have {name}, it's stock is {quantity} and price is {price}/- pkr.")
        data.append(f"We currently have a supply of {quantity} {name}s in stock, and the price for each {name} is {price}/- pkr.")
        
        # stock quantity responses
        if quantity == 0:
            data.append(f"{name} is not in stock")


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
    sentence2 = "We offer a variety of categories to choose from, including "
    if(results):
        sentence = "We have these categories "
        for category in results:
            id_, category_name = category
            sentence += f", {category_name}"
            sentence2 += f"{category_name}, "
        sentence += "."
        sentence2 += ". Each category represents a unique selection of precious gemstones that are sure to capture your interest."
    
    data.append(sentence)
    data.append(sentence2)
    return data