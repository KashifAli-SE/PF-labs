def duplicate(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        words = content.split()
        
        seen_words = set()
        for word in words:
            word = word.lower()
            if word in seen_words:
                return True  
            seen_words.add(word)
            
        
        return False  
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return False
print(duplicate('file.txt'))
