def format_scraped_data(item):
    if isinstance(item, dict):
        return {key: format_scraped_data(value) for key, value in item.items()}
    elif isinstance(item, list):
        return [format_scraped_data(element) for element in item]
    else:
        return item
