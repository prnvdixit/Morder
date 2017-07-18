def morse_encryptor(message_text) :

    """
    This functions encrypts a English text into corresponding
    morse-code equivalent (i.e. cipher text) and returns the same
    """

    # Convert the message-text to all uppercases for easy lookup in the dictionary
    message_text = message_text.upper()

    # Initialise cipher-text
    encrypted_text = ""

    for letter in message_text :

        # If there is a space in message-text, add one to cipher-text too
        if letter == ' ' :
            encrypted_text += letter

        # Else, find the equivalent encrypted letter to English letter and
        # append that to the end of encrypted text
        else :
            encrypted_text += morse_codes[letter] + " "

    return encrypted_text

def morse_decryptor(encrypted_text) :

    """
    This function decrypts the encrypted-text (i.e. cipher text) and
    return a English text
    """
    
    # To mark end of last character
    encrypted_text += ' '

    # message_text : Final English sentence obtained on decrypting cipher text
    message_text = ""

    # Consecutive characters in morse are separated by spaces, this contains last charaacter
    char_in_morse = ""

    # Depending on if there are 1 or 2 consecutive spaces, words and letters will
    # be initiated (Letters have single while words have double spaces in between)
    consecutive_spaces = 0

    for morse_character in encrypted_text :

        # Check if this is end of a word of letter
        if morse_character == ' ' :

            # Increament number of consecutive spaces encountered so far
            consecutive_spaces += 1

            # If there is single space between two morse-letters, it means that this is
            # end of one of the morse-letter
            if consecutive_spaces == 1 :
                
                # Accessing keys using values in dictionary - Use the dictionary as lists
                message_text += morse_codes.keys()[morse_codes.values().index(char_in_morse)]

                # Reinitialise the word in morse
                char_in_morse = ""

            # If there are two spaces, it means it is end of a morse-word
            else :
                message_text += " "
                consecutive_spaces = 0

        # Otherwise, add the decrypted morse-letter to the message-text
        else :
            consecutive_spaces = 0
            char_in_morse += morse_character


    return message_text


# A dictionary storing the morse-code equivalents for most letters, numbers, symbols in English
morse_codes = {
        'A' : ".-", 'B' : "-...", 'C' : "-.-.", 'D' : "-..", 'E' : ".",
        'F' : "..-.", 'G' : "--.", 'H' : "....", 'I' : "..", 'J' : ".---",
        'K' : "-.-", 'L' : ".-..", 'M' : "--", 'N' : "-.", 'O' : "---",
        'P' : ".--.", 'Q' : "--.-", 'R' : ".-.", 'S' : "...", 'T' : "-",
        'U' : "..-,", 'V' : "...-", 'W' : ".--", 'X' : "-..-", 'Y' : "-.--",
        'Z' : "--..", '.' : ".-.-.-", ',' : "--..--", '?' : "..--..",
        '/' : "-..-.", '@' : ".--.-.", '(' : "-.--.", ')' : "-.--.-",
        '-' : "-....-", '1' : ".----", '2' : "..---", '3' : "...--",
        '4' : "....-", '5' : ".....", '6' : "-....", '7' : "--...",
        '8' : "---..", '9' : "----.", '0' : "-----"
        }
