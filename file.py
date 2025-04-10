def read_and_modify_file():
    # Ask the user for the input filename
    filename = input("Enter the name of the file you want to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content has been written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Something went wrong while reading or writing the file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the function
read_and_modify_file()
