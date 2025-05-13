def file_read_write():
    # Get filename from user
    try:
        input_filename = input("Enter the name of the file to read: ")
        
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Modify the content (for example, converting to uppercase)
            modified_content = content.upper()
            
            # Create output filename by adding '_modified' before extension
            output_filename = input_filename.rsplit('.', 1)
            output_filename = f"{output_filename[0]}_modified.{output_filename[1]}"
            
            # Write modified content to new file
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                
            print(f"Successfully created modified file: {output_filename}")
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    file_read_write()
