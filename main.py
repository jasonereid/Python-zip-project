# zipfile project
# this project will allow you to zip compress files together, read zipped files, and unzip them

import zipfile, os
# get the path
from pathlib import Path
p = Path.home()

print("Welcome to the zip program. Do you want to read and extract a zip folder, or do you want to create a new zip folder?")
readorZip = input("Choose R for read and unzip, or N for create new zip folder, or any other key to quit.")

if readorZip == "R":
    # set our variable to our example zip file
    zipName = input("Please type the exact name of the zip files stores in your Path folder, including the file extension.")
    exampleZip = zipfile.ZipFile(p / zipName)
    # read and print the contents of the example zip file
    print(exampleZip.namelist())
    # extract files if needed to the path folder
    yorN = input("Do you want to extract those files? Y or N.")
    # extract files
    if yorN == "Y":
        exampleZip.extractall(p)
        exampleZip.close()
    else:
        print("Ok.")
elif readorZip == "N":
    # creating a new zip folder on the path
    print("Creating a new zipped folder")
    newZip = input("What is the name of your new folder? Please include the file extension at the end.")
    print("Now, what is the exact name of the file you want to compress? Please include the file extension at the end.")
    newFileZip = input()
    newZip = zipfile.ZipFile(p / newZip, "w")
    newZip.write(p / newFileZip, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()
else:
    print("You didn't choose R or N. Goodbye.")