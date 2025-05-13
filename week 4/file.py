def process_file():
    try:
        # Asking user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # opening the file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask for output filename
        output_filename = input("Enter the name for the new file to write to: ")

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read or write to the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
process_file()
