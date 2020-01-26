import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        print(filename)
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        # Replaces the filename with the path so that it would sort the file in its respective directory
        os.rename(filename, "{}/{}".format(extension, filename))


main()
