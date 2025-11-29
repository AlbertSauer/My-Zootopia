import json

def load_data(file_path):
    """Load JSON file safely"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Main script
file_path = "animals_data.json"

try:
    animals = load_data(file_path)

    for animal in animals:
        # --- Required fields ---
        name = animal.get("name")

        # Diet is inside characteristics
        diet = animal.get("characteristics", {}).get("diet")

        # Locations is a top-level list
        locations = animal.get("locations")
        first_location = locations[0] if locations and len(locations) > 0 else None

        # Type is inside characteristics (note: sometimes lowercase 'mammal')
        animal_type = animal.get("characteristics", {}).get("type")

        # --- Print only existing fields ---
        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if first_location:
            print(f"Location: {first_location}")
        if animal_type:
            print(f"Type: {animal_type}")

        print()  # blank line between animals

except FileNotFoundError:
    print(f"Error: '{file_path}' not found!")
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON → {e}")
except Exception as e:
    print(f"Unexpected error: {e}")