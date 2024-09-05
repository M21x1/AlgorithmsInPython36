## Find Patterns with Case Insensitivity

def pattern_search(text, pattern, case_sensitive = True):
# validated in an additional layer of conditional statements
  if not case_sensitive:
    text = text.lower()
    pattern = pattern.lower()
  
  for index in range(len(text)):
# range(len(text) - len(pattern)+1)    
    match_count = 0
    for char in range(len(pattern)): 
      if pattern[char] == text[index + char]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)

## Other solution

def pattern_search(text, pattern, case_sensitive=True):
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
# compacted into the existing logic with the use of the "and" keyword
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)

## Replace Found Words: Maintaining the Fixed Text
## Skipping Replaced Characters


def pattern_search(text, pattern, replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0

  for index in range(len(text)):

    if num_skips > 0:
      num_skips -= 1
      continue

    match_count = 0

    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break

    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips = len(pattern)-1
    else:
      fixed_text += text[index]

  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")

## other solution

def pattern_search(text, pattern, replacement, case_sensitive=True):
    # Placeholder for the final text with all replacements
    fixed_text = ""
    num_skips = 0  # Variable to track characters to skip

    # If case sensitivity is off, convert both text and pattern to lowercase
    if not case_sensitive:
        lower_text = text.lower()
        lower_pattern = pattern.lower()
    else:
        lower_text = text
        lower_pattern = pattern
    
    # Iterate through the text
    for index in range(len(text)):
        # If num_skips is active, skip current iteration
        if num_skips > 0:
            num_skips -= 1
            continue
        
        match_count = 0
        # Check for pattern match
        for char in range(len(pattern)):
            if index + char < len(text):  # Ensure we don't go out of bounds
                if case_sensitive:
                    if pattern[char] == text[index + char]:
                        match_count += 1
                    else:
                        break
                else:
                    if lower_pattern[char] == lower_text[index + char]:
                        match_count += 1
                    else:
                        break
            else:
                break
        
        # If pattern is fully matched
        if match_count == len(pattern):
            fixed_text += replacement  # Append the replacement to fixed_text
            num_skips = len(pattern) - 1  # Skip the characters of the matched pattern
        else:
            fixed_text += text[index]  # Append the current character to fixed_text
    
    return fixed_text

# Test cases
friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

# Running the test cases
print(pattern_search(friends_intro, "Language", "language"))
print(pattern_search(friends_intro, "pylhon", "Python", False))
print(pattern_search(friends_intro, "idil", "ideal", False))
print(pattern_search(friends_intro, "zzz ", ""))
print(pattern_search(friends_intro, "syntacs", "syntax"))
print(pattern_search(friends_intro, "languuUuage", "language"))


## Fuzzy Matching (Handling Typos)

import difflib

def fuzzy_search(text, pattern, threshold=0.8):
    words = text.split()
    for index, word in enumerate(words):
        similarity = difflib.SequenceMatcher(None, word, pattern).ratio()
        if similarity >= threshold:
            print(f"'{pattern}' matches '{word}' with {similarity:.2f} similarity at index {index}")


# This could help you find approximate matches where there are small deviations from the exact pattern.

## Word-Based Matching

def word_based_search(text, pattern):
    words = text.split()
    pattern_words = pattern.split()
    for index in range(len(words) - len(pattern_words) + 1):
        if words[index:index + len(pattern_words)] == pattern_words:
            print(f"Pattern '{pattern}' found at word index {index}")

#This approach allows you to search for multi-word patterns in a text.

## Wildcard Matching (Flexible Patterns)

import re

def wildcard_search(text, pattern):
    # Convert wildcard * to regex .*
    regex_pattern = pattern.replace("*", ".*").replace("?", ".")
    matches = re.finditer(regex_pattern, text)
    for match in matches:
        print(f"Pattern '{pattern}' found at index {match.start()}")

#This allows for flexible pattern matching, similar to how wildcards work in file search systems.
