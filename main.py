def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = word_count(text)
  chars_dict = character_frequency(text)
  labeled_char_list = char_list(chars_dict)
  labeled_char_list.sort(reverse=True, key=sort_on)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print()
  print_character_counts(labeled_char_list)
  print("--- End Report ---")

def get_book_text(path):
  # Returns file specified in path as a string
  with open(path) as f:
    return f.read()

def word_count(text):
  # Converts string into a list consisting of separate strings from the text separated by white space or line breaks
  words = text.split()
  # Returns the length of the list
  return len(words)
  

def character_frequency(book_string):
  # Converts the entire string to lowercase
  book_string_lowered = book_string.lower()

  # Initialize empty dictionary to store characters and counts
  char_dict = {}

  # Iterate through each character of the string
  for char in book_string_lowered:
    # Check if the character is alphabetical
    if char.isalpha():
      # If the char is in the dict, increment its count
      # If it's not, add it to the dictionary with a count of 1
      char_dict[char] = char_dict.get(char, 0) + 1
      
      
  return char_dict


# Function that transforms dictionary into list of dictionaries with wanted keys
def char_list(input_dict):
  return [{"character": key, "num": value} for key, value in input_dict.items()]

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def print_character_counts(input_list):
  for item in input_list:
    character = item['character']
    quantity = item['num']
    print(f"The '{character}' was found {quantity} times")

main()