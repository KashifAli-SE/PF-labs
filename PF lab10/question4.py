def abc(input_filename):
    try:
        # Open the input file and read its content
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Split content into words
        words = content.split()
        
        # Replace four-letter words with 'xxxx'
        modified_words = ['xxxx' if len(word) == 4 else word for word in words]
        
        # Join the modified words into a single string
        modified_content = ' '.join(modified_words)
        
        # Write the modified content to abc.txt
        with open('abc.txt', 'w') as output_file:
            output_file.write(modified_content)
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
abc('example.txt')
