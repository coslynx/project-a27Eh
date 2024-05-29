# multiLanguageSupport.py (Python)

'''
This file contains functions to support multiple languages in the Discord moderation bot.
'''

languages = {
    "en": {
        "profanity_warning": "Please refrain from using profane language.",
        "spam_warning": "Stop spamming the chat, or you will be muted.",
        "inappropriate_content_warning": "Your message contains inappropriate content. Please keep the chat clean.",
        "welcome_message": "Welcome to the server! Enjoy your stay.",
        "goodbye_message": "Goodbye! We hope to see you again.",
        # Add more language-specific messages here
    },
    "es": {
        "profanity_warning": "Por favor, abstente de usar lenguaje grosero.",
        "spam_warning": "Deja de hacer spam en el chat, o serás silenciado.",
        "inappropriate_content_warning": "Tu mensaje contiene contenido inapropiado. Por favor, mantén el chat limpio.",
        "welcome_message": "¡Bienvenido al servidor! Disfruta tu estancia.",
        "goodbye_message": "¡Adiós! ¡Esperamos verte de nuevo!",
        # Add more language-specific messages here
    },
    # Add more languages as needed
}

def get_message(language, key):
    '''
    Retrieve a message based on the specified language and key.
    
    Args:
    language (str): The language code (e.g., "en", "es").
    key (str): The key for the desired message.
    
    Returns:
    str: The message corresponding to the language and key.
    '''
    if language in languages and key in languages[language]:
        return languages[language][key]
    else:
        return "Message not found for the specified language and key."
  
# End of multiLanguageSupport.py