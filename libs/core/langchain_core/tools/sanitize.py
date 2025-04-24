"""A tool for validating inputs to model chats."""

import re

def sanitize_inpuy(input_text: str) -> str:
    """Sanitize input for chat by removing any delimiters to prevent escape of context."""
    # Define the delimiters to be removed
    delimiters = [
        r"\[INST\]", r"\[/INST\]", r"\<\<SYS\>\>", r"\<\<\/SYS\>\>",
        r"\<\!\-\-.*?\-\-\>", r"\<\!\-\-.*?\-\-\>"
    ]

    # Create a regex pattern that matches any of the delimiters
    pattern = re.compile("|".join(delimiters))

    # Remove the delimiters from the input text
    sanitized_text = re.sub(pattern, "", input_text)

    return sanitized_text

def validate_input(input_text: str) -> bool:
    """Validate input for chat by checking for delimiters."""
    # Define the delimiters to check for
    delimiters = [
        r"\[INST\]", r"\[/INST\]", r"\<\<SYS\>\>", r"\<\<\/SYS\>\>",
        r"\<\!\-\-.*?\-\-\>", r"\<\!\-\-.*?\-\-\>"
    ]

    # Create a regex pattern that matches any of the delimiters
    pattern = re.compile("|".join(delimiters))

    # Check if the input text contains any of the delimiters
    if pattern.search(input_text):
        return False

    return True