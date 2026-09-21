from pathlib import Path

folder = Path(".")

# Find only JPG files numbered 30 or higher
files = []

for file in folder.iterdir():
    if not file.is_file():
        continue

    if file.suffix.lower() != ".jpg":
        continue

    try:
        number = int(file.stem)
    except ValueError:
        continue

    if number >= 30:
        files.append((number, file))

# Sort by number
files.sort()

# First rename everything to temporary names
temporary_files = []

for number, file in files:
    temp_name = folder / f"temp_{number}.jpg"
    file.rename(temp_name)
    temporary_files.append((number, temp_name))

# Now rename temporary files to their final names
for number, temp_file in temporary_files:
    new_number = number - 10
    new_name = folder / f"{new_number}.jpg"

    temp_file.rename(new_name)

    print(f"{number}.jpg -> {new_number}.jpg")

print("Renaming completed.")