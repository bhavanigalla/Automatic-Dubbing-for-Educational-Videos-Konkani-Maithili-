from deep_translator import GoogleTranslator

def translate_text(text, language):

    if language == "Konkani":
        target = "hi"   # use Hindi as base

    elif language == "Maithili":
        target = "hi"   # use Hindi as base

    translated = GoogleTranslator(
        source="auto",
        target=target
    ).translate(text)

    return translated