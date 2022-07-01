import os
import tifftools

# tifftools library used
# Input: Page level TIFF Images
# Output: Consolidated TIFF Image

filepath = input(" Enter the TIF Image file path: ")

filepath1 = filepath + "/"

# Creating "Output" folder for Merge file creation
output_dir = "Output"
output = filepath + "/" + output_dir
if os.path.exists(output):
	pass
else:
	os.mkdir(output)

# collect all the TIFF images into the list variable "file_list"
file_list = []
for fname in os.listdir(filepath):
	if not fname.endswith(".tif"):
		continue
	print(fname)
	# append the tif file list one by one
	file_list.append(fname)
	# defining the output filename as "Merge.tif
	outputname = "Merge.tif"
	outputdir = output + "/" + outputname


# changing the control to input tif file path
dname = os.path.dirname(filepath1)
os.chdir(dname)

# All listed tiff images from file_list variable will merged together as "Merge.tif" in the outputdir path.
tifftools.tiff_concat(file_list, outputdir, overwrite=True)
print(" \n\nProcess Completed\n\n")

