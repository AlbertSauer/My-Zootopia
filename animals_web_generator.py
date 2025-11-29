import json

# 1. Load the animal data (same as before)
with open('animals_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Generate proper HTML for each animal card
output = ''

for animal in data:
    # Safely extract the fields (some animals may miss certain keys)
    name = animal.get('name', 'Unknown Animal')

    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'Unknown')

    # Most animals have 'locations' as a list
    location = 'Unknown'
    if animal.get('locations') and len(animal['locations']) > 0:
        location = animal['locations'][0]

    # Some use 'type', others use 'class' or nothing at all
    animal_type = 'Unknown'
    if 'type' in characteristics:
        animal_type = characteristics['type']
    elif 'class' in characteristics:
        animal_type = characteristics['class']

    # Build one <li> card per animal
    output += '<li class="cards__item">\n'
    output += f"    Name: {name}<br/>\n"
    output += f"    Diet: {diet}<br/>\n"
    output += f"    Location: {location}<br/>\n"
    output += f"    Type: {animal_type}<br/>\n"
    output += '</li>\n\n'  # extra newline for readability in the HTML source

# 3. Read the template
with open('animals_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 4. Replace the placeholder with our nice HTML cards
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# 5. Write the beautiful result
with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Step 3 complete! animals.html now has beautiful cards")
print("Open animals.html in the browser — it should look much better now!")