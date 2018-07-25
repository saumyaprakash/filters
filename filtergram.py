import filters

#def main():
print("hello")
# Ask the user for a file
filename = input("Enter the name of the image file to edit: ")

# Load the image from the file
img = filters.load_img(filename)
# Apply the filters
new_img = filters.obamicon(img)

# Save the final Image
filters.save_img(new_img, "gwcFilters.jpg")


#if __name__ == '__main__':
#    main()
