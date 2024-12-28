import text_processor

def main():
    # Ask user the text to be processed
    user_input = input("Enter the text to be processed: ")
    
    # Process the text
    processed_text = text_processor.process_text(user_input)
    
    # Show processed text
    print("Processed Text:", processed_text)

if __name__ == "__main__":
    main()
