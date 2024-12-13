def distribution(filename):
    try:
        # Read grades from file
        with open(filename, 'r') as file:
            grades = file.read().split()
        
        # Count occurrences of each grade
        grade_counts = {}
        for grade in grades:
            grade_counts[grade] = grade_counts.get(grade, 0) + 1
        
        # Sort grades alphabetically for consistent output
        for grade in sorted(grade_counts.keys()):
            print(f"students got {grade} {grade_counts[grade]}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
distribution('grades.txt')
