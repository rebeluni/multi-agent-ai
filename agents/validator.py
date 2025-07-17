def validate_article(text):
    # Check for repeated phrases (basic version)
    repeated_phrases = ["the United States", "artificial intelligence"]
    repeat_count = sum(text.count(phrase) for phrase in repeated_phrases)

    if repeat_count > 3:
        return False, "⚠️ Too many repeated phrases."

    # Check for word count
    word_count = len(text.split())
    if word_count < 250:
        return False, "⚠️ Too short. Less than 250 words."

    return True, "✅ Looks good!"
