def main():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (for demo, let's convert to uppercase)
        modified_content = content.upper()

        # Create a new filename to write the modified content
        new_filename = "modified_" + filename

        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
