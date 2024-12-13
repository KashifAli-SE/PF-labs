def hexASCII():
    print("Lowercase Character to Hexadecimal ASCII Mapping:\n")
    for char in range(ord('a'), ord('z') + 1):
        hex_value = format(char, 'x')  # Convert ASCII value to hexadecimal
        print(f"'{chr(char)}': 0x{hex_value}")

# Example usage
hexASCII()
