travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, visit_times, cities_visited):
    new_country={
    "country":country_visited,
    "visits":visit_times,
    "cities":cities_visited
    }
    travel_log.append(new_country)

def show_stats():
    visited_country=""
    visits=""
    visited_cities=""
    for countries in travel_log:
        visited_country=countries["country"]
        visits=countries["visits"]
        visited_cities=countries["cities"]
        print(f"You visited {visited_country}, {visits} time. The cities are: {visited_cities}")


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
show_stats()
# print(travel_log)