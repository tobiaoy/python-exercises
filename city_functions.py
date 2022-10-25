def make_city_country(city, country, population=''):
    """generates a location with a formatted city and country"""
    if population:
        location = f"{city.title()}, {country.title()} - population {population}"
    else:
        location = f"{city.title()}, {country.title()}"
    return location