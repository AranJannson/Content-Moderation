import json
from operator import xor
# ImageHash Library
# https://github.com/JohannesBuchner/imagehash
from PIL import Image
import imagehash


def hashComparison(file, threshold, phfjson):

    # Check File can be opened as an image
    if Image.open(file) == None:
        exit(f"File {file} could not be opened as an image. Check file path and format.")

    # Check PHF JSON file name is of type str
    if type(phfjson) != str:
        exit(f"PHF JSON file name must be of type str.")

    # Check PHF JSON file can be opened
    if json.load(open(phfjson)) == None:
        exit(f"PHF JSON file {phfjson} could not be opened. Check file path and format.")
    
    # Ensure threshold is of type int
    if type(threshold) != int:
        exit(f"Threshold must be of type int.")

    # Can also work on PNG if the flag is changed
    if file.split(".")[-1] != "jpg":
        print(file.split(".")[-1])
        exit("File must be JPG")
        
    # Open the image file
    with Image.open(file) as image:
        # Get the hashes for the current image
        providedFilePHash = imagehash.phash(image)
        providedFileAvHash = imagehash.average_hash(image)

        # print(providedFileHash)

    # Check hash value was generated and return it
    if providedFilePHash == None:
        exit(f"Error Extracting Hash For: {file}")

    if providedFileAvHash == None:
        exit(f"Error Extracting Hash For: {file}")

    # Load in the PHF Hash JSON
    hashList = json.load(open(phfjson))
    resultHashListPHash = []
    resultHashListAvHash = []

    for currentPHash in hashList["PHash"]:
        # Calculate the current Hamming Distance (PHash)
        xorVal = bin(xor(int.from_bytes(bytes.fromhex(str(providedFilePHash)), byteorder='little'), int.from_bytes(bytes.fromhex(hashList["PHash"][currentPHash]), byteorder='little'))).count("1")    
        # Append the Hamming Distance to a list
        resultHashListPHash.append(xorVal)

    for currentAvHash in hashList["AvHash"]:
        # Calculate the current Hamming Distance (AvHash)
        xorVal = bin(xor(int.from_bytes(bytes.fromhex(str(providedFileAvHash)), byteorder='little'), int.from_bytes(bytes.fromhex(hashList["AvHash"][currentAvHash]), byteorder='little'))).count("1")    
        # Append the Hamming Distance to a list
        resultHashListAvHash.append(xorVal)

    # PHash Comparison
    if resultHashListPHash != [] and min(resultHashListPHash) <= threshold:
        # Check for exact match first
        if min(resultHashListPHash) == 0:
            index = resultHashListPHash.index(min(resultHashListPHash))
            imageName = list(hashList["PHash"].keys())[index]
            PHashVal = hashList["PHash"][imageName]

            print(f"Exact Image Match Found In PHash Format.\n"
                  f"-Located File's Name: {imageName}\n"
                  f"-Located File's Hash Value : {PHashVal}\n"
                  f"-Provided File's PHash Value: {providedFilePHash}",
                  )
            return True   
        
        # Check if the Hamming Distance is within the provided threshold
        index = resultHashListPHash.index(min(resultHashListPHash))
        fileHash = list(hashList["PHash"].keys())[index]
        PHashVal = hashList["PHash"][currentPHash]

        print(f"Similar Image Found In PHash Format.\n"
                f"-Located File's Name: {fileHash}\n"
                f"-Located File's PHash Value : {PHashVal}\n"
                f"-Provided File's PHash Value: {providedFilePHash}\n",
                f"-Hamming Distance Value: {min(resultHashListPHash)}"
                )
        return True
    

    # Average Hash Comparison
    if resultHashListAvHash != [] and min(resultHashListAvHash) <= threshold:
        # Check for exact match first
        if min(resultHashListAvHash) == 0:
            index = resultHashListAvHash.index(min(resultHashListAvHash))
            imageName = list(hashList["AvHash"].keys())[index]
            AvHashVal = hashList["AvHash"][imageName]

            print(f"Exact Image Match Found In Average Hash Format.\n"
                  f"-Located File's Name: {imageName}\n"
                  f"-Located File's AvHash Value : {AvHashVal}\n"
                  f"-Provided File's AvHash Value: {providedFileAvHash}",
                  )
            return True   
        
        # Check if the Hamming Distance is within the provided threshold
        index = resultHashListAvHash.index(min(resultHashListAvHash))
        fileHash = list(hashList["AvHash"].keys())[index]
        AvHashVal = hashList["AvHash"][currentAvHash]

        print(f"Similar Image Found In Average Hash Format.\n"
                f"-Located File's Name: {fileHash}\n"
                f"-Located File's AvHash Value : {AvHashVal}\n"
                f"-Provided File's AvHash Value: {providedFileAvHash}\n",
                f"-Hamming Distance Value: {min(resultHashListAvHash)}"
                )
        return True
    # No Matches Found
    print("No Valid Match Found")
    return False

userSelection = ""

# Prompt user for file name until a valid image file is provided
while(userSelection == ""):
        # Get file name from user (including file extension)
        fileName = input("Type the name of the file to be compared: ")
        try:
            # Attempt to open the file as an image
            with Image.open(fileName) as img:
                userSelection = fileName
            # If successful, break out of the loop
        except (FileNotFoundError, OSError):
            # Provide an error message and prompt again
            print("Invalid File Name. Please Try Again.")


hashComparison(userSelection, 10, "PHF_Hashes.json")
