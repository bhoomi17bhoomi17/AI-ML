def analyze_text(text):
    # Remove extra spaces
    text = text.strip()
    
    # Count characters (including spaces)
    char_count = len(text)
    
    # Count characters (excluding spaces)
    char_no_space = len(text.replace(" ", ""))
    
    # Count words
    words = text.split()
    word_count = len(words)
    
    # Count sentences (approximate)
    sentence_endings = text.count('.') + text.count('!') + text.count('?')
    
    # Display results
    print("\nTEXT ANALYSIS RESULTS")
    print("=" * 40)
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (without spaces): {char_no_space}")
    print(f"Words: {word_count}")
    print(f"Sentencesb: {sentence_endings}")
    print("=" * 40)
    
    # Average word length
    if word_count > 0:
        avg_word_length = char_no_space / word_count
        print(f"Average word length: {avg_word_length:.2f} characters")

# Main program
print("Word Counter Tool\n")
text = input("Enter your text: ")

if text.strip():  # Check if the input is not just empty spaces
    analyze_text(text)
else:
    print("No text entered!")