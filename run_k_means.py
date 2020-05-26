from image_utils import *

print("Enter the file name of your picture")
input_file = input('>')

print("Enter the name of the output file this program will create")
output_file = input('>')

print("Enter a value for k")
k = input('>')

k = int(k)

image = read_jpg(input_file)

new_image = assign_clusters(image, k)

save_jpg(output_file, new_image)

