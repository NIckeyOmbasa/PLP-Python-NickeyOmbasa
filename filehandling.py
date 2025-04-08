def modify_file_content(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()
        
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Content from '{input_file}' has been modified and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Cannot read the file '{input_file}' or write to '{output_file}'.")

