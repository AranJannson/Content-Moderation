import os
import json
# ImageHash Library
# https://github.com/JohannesBuchner/imagehash
from PIL import Image
import imagehash

extracted_hashes = {}
extracted_Avhashes = {}


def extractFilePHash(name):

    # Check File extension and if it does not match one of the following close the script
    if not name.split(".")[-1] == "jpg":
        exit("File must be JPG")

    # Open the image file
    with Image.open(name) as image:

        # Get the hash for the current image
        hashValue = imagehash.phash(image)

        # Check hash value was generated and return it
        if hashValue:
            print(f"File PHash Added: {name}")
            return str(hashValue)
        else:
            # If the has value was not generated provide an error and exit the script
            exit(f"Error Extracting PHash For: {name}")


def extractFileHashAverage(name):

    # Check File extension and if it does not match one of the following close the script
    if not name.split(".")[-1] == "jpg":
        exit("File must be JPG")

    # Open the image file
    with Image.open(name) as image:

        # Get the hash for the current image
        hashValue = imagehash.average_hash(image)

        # Check hash value was generated and return it
        if hashValue:
            print(f"File Average Hash Added: {name}")
            return str(hashValue)
        else:
            # If the has value was not generated provide an error and exit the script
            exit(f"Error Extracting Average Hash For: {name}")

# Get The Hashes For All Images in the Images Folder
output_data = {
    "PHash": {},
    "AvHash": {}
}

# Loop through all files in the Images directory
for filename in os.listdir("Images"):
    file = os.path.join("Images", filename)
    userSelection = ""

    # Prompt user for hash type until a valid selection is made
    while(userSelection != "A" and userSelection != "P"):
        userSelection = input(f"Type P (PHash) or A (Average Hash) For The Hashing Format for {filename}: ")
        if(userSelection != "A" and userSelection != "P"):
            print("Invalid Selection. Please Choose A or P.")

    # Apply the selected hash type
    if(userSelection == "P"):
        PHash = extractFilePHash(file)
        output_data["PHash"][filename] = PHash
    if(userSelection == "A"):
        AvHash = extractFileHashAverage(file)
        output_data["AvHash"][filename] = AvHash

# Save the hashes to the JSON file
with open("PHF_Hashes.json", 'w') as dump:
    json.dump(output_data, dump, indent=4)
