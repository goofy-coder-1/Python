# =====================================================================
# STRING BASICS (str)
# =====================================================================
# A string is simply a sequence of characters wrapped inside quotes. 
# Python treats single quotes ('') and double quotes ("") exactly the same.

message_1 = "Hello World!"
message_2 = 'Python is fun.'

print(message_1)
print(message_2, "\n")


# =====================================================================
# THE QUOTATION TRAP (ESCAPING CHARACTERS)
# =====================================================================
# If your text contains an apostrophe, using single quotes will crash!
# Example: 'What's up' breaks because Python thinks the string ends at 'What'.

# Solution A: Wrap the sentence in double quotes so the single quote inside is safe.
correct_quote = "What's up with Python today?"

# Solution B: Use an escape character (\) to tell Python the quote is just text.
escaped_quote = 'What\'s up with Python today?'

print("--- Handling Quotes Safely ---")
print(correct_quote)
print(escaped_quote, "\n")


# =====================================================================
# MULTI-LINE STRINGS (TRIPLE QUOTES)
# =====================================================================
# Standard quotes cannot span across multiple lines. For long paragraphs or 
# text blocks, we use triple quotes (''' or """).

multi_line_text = """This is a multi-line string.
It preserves all the line breaks
and spaces exactly how you type them!"""

print("--- Multi-line Text ---")
print(multi_line_text)