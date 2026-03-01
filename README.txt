PHF Hash Extractor & Comparison

Pre-Requisites
- Python 3.10 or Higher
- Imagehash
- PIL
- operator
- json
- \Images Folder with jpg images

Files
- PHF Hash Extractor.py
- PHF Comparison.py

Developed On A Local Machine Using Python 3.12.3 and VS Code, The Scripts Have Both Been Tested On The DF VM Succesfully


Description
- The two scripts are used for generation and comparison of PHF in order to detect the level of similarity between two images based on the PHF values
  "PHF Hash Extractor.py" generates a json file storing hash values of provided images
  "PHF Comparison.py" compares the hash value of a submitted image with pre computed hash values inside of a json file. Providing a result based on a pre defined hamming distance.


Usage
- PHF Hash Extractor.py:
    - A folder called \Images including jpg files of images you want to exract the hashes for must be present in the same directory as the Scripts
      The script can be directly run, once run the user will be prompted with an option to choose what hash type should be generated for the first file in the \Images folder
      The user will have a choice between "A" for Average Hash and "P" for Perceptual Hashing (PHash). Once the user applies there selection
      The same prompt is provided to the user for each file in the \Images directory.
      Following this a json file called "PHF_Hashes.json" will be generated including all generated hashes, the hashes are stored based on type

- PHF Comparison.py
    - The user must include the "PHF_Hashes.json" file or a file of similar format in the same directory as the script. Once this file is included the user can directly run the script
      The script is pre setup with a hamming distance of 10 and can be edited by changing the value on the final line of the script.
      When the script is run the system prompts the user to choose which image in the same directory as the script they want to compare with the "PHF_Hashes.json" hash library
      When the user chooses a valid jpg, the system calculates the Average and Perceptual Hash value of the image. Using the generated hashes it searches the hash library for a matching or similar record
      If a hash is located with an exact match the user recives an output stating that the same image has been found, otherwise if an image within the specified hamming distance (10) is located
      They are prompted with the information on the file as well as the hamming distance between the two. Otherwise the user is prompted with a "No Matches Found" prompt

