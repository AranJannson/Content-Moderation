import os
import json
import hashlib

extracted_hashes = {}

def extractFileHash(name):

    # Check File extension and if it does not match one of the following close the script
    if not name.split(".")[-1] == "jpg" or name.split(".")[-1] == "jpeg" or name.split(".")[-1] == "png":
        exit("File must be JPEG or PNG")

    # Open the image file
    with open(name, "rb") as image:

        # Get the hash for the current image
        hashValue = hashlib.sha256(image.read()).hexdigest()

        # Check hash value was generated and return it
        if hashValue:
            print(f"File Hash Added: {name}")
            return hashValue
        else:
            # If the has value was not generated provide an error and exit the script
            exit(f"Error Extracting Hash For: {name}")


for filename in os.listdir("Images"):
    file = os.path.join("Images", filename)
    fHash = extractFileHash(file)

    extracted_hashes.setdefault(file, []).append(fHash)


with open("PHF_Hashes.json", 'w') as dump:
    json.dump(extracted_hashes, dump, indent=1)
