import os


def main():
    """Move files into where user wants to store them based on extension."""
    extension_to_category = {}
    os.chdir("FilesToSort-1")
    for filename in os.listdir('.'):
        print(filename)
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
            # If the user choose an existing folder, it would just put the items in the folder together without
            # overwriting anything

        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()