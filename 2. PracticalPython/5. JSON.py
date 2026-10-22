# JSON is a common format for representing structured data. It's widely used in APIs and AI applications.

import json

settings = {
    "theme" : "dark",
    "notifications" : True,
    "font_size" : 16
}

# Save Python data as JSON
with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)

# Read JSON back into Python
with open("settings.json", "r", encoding="utf-8") as file:
    loaded_settings = json.load(file)

print(loaded_settings)
print(loaded_settings["theme"])
print(loaded_settings["notifications"])

# Important distinction:

    # json.dump() writes Python data to a file.
    # json.load() reads JSON data from a file.
    # json.dumps() converts Python data into a JSON string.
    # json.loads() converts a JSON string into Python data.

