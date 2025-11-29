import json

# 1. Read the animal data from the JSON file
with open('animals_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 2. Generate one big string with all the animals' information
output = ''                             # start with empty string
for animal in data:
    name = animal['name']
    diet = animal['characteristics'].get('diet', 'Unknown')
    location = animal['locations'][0]   # first location only
    animal_type = animal.get('type', 'Unknown')

    output += f"Name: {name}\n"
    output += f"Diet: {diet}\n"
    output += f"Location: {location}\n"
    output += f"Type: {animal_type}\n"
    output += "\n"                      # blank line between animals
# ← Add this line to see the generated string
print(output)
# 3. Read the HTML template
with open('animals_template.html', 'r', encoding='utf-8') as file:
    template = file.read()

# 4. Replace the placeholder with our generated text
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# 5. Write the result to animals.html
with open('animals.html', 'w', encoding='utf-8') as file:
    file.write(final_html)

print("animals.html has been created successfully!")
print("Right-click → Preview Static (or open in browser) to see it.")