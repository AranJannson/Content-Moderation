import json
import hashlib
from operator import xor


def hashComparison(name, threshold, phfjson):

    if type(threshold) != int:
        exit(f"Threshold must be of type int.")

    # Can also work on PNG if the flag is changed
    if name.split(".")[-1] != "jpg":
        print(name.split(".")[-1])
        exit("File must be JPEG, PNG, GIF or BMP")

    with open(name, "rb") as image:
        # Get the hash for the current image
        providedFileHash = hashlib.sha256(image.read()).hexdigest()
        providedFileHashValue = bytes.fromhex(hashlib.sha256(image.read()).hexdigest())

    if providedFileHashValue == None:
        exit(f"Error Extracting Hash For: {name}")

    hashList = json.load(open(phfjson))

    for fileHash in hashList:

        hashByte = bytes.fromhex(hashList[fileHash][0])


        if (hashList[fileHash][0]) == providedFileHash:
            print(f"Exact Image Match Found.\n"
                  f"-Located File's Name: {fileHash}\n"
                  f"-Located File's Hash Value : {hashList[fileHash][0]}\n"
                  f"-Provided File's Hash Value: {providedFileHash}"
                  )
            return True

        if len(providedFileHashValue) != len(hashByte):
            continue
        else:
            xorVal = bin(xor(int.from_bytes(bytes.fromhex(providedFileHash), byteorder='little'), int.from_bytes(bytes.fromhex(hashList[fileHash][0]), byteorder='little'))).count("1")

        # print(f"The XOR Value is: {xorVal}")


        if xorVal >= threshold:
            # print("Not Similar")
            continue
        else:
            print(f"Similar Image Found.\n"
                  f"-Located File's Name: {fileHash}\n"
                  f"-Located File's Hash Value : {hashList[fileHash][0]}\n"
                  f"-Provided File's Hash Value: {providedFileHash}"
                  )
            return True
    print("No Match Found")
    return False


hashComparison("10-mz.jpg", 150, "PHF_Hashes.json")

