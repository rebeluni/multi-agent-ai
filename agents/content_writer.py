from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ✅ Load GPT-2 model & tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# ✅ Set up generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def run_content_writer(summary: str = "", research_data: str = "") -> str:
    """
    Generate article-style content using GPT-2 given a summary and research.
    If inputs are missing or too short, it handles them gracefully.
    """
    if not summary and not research_data:
        return "❌ Sorry, I need at least a summary or some research data to generate content."

    prompt = f"""
    You are an expert content writer. Based on the following information, write a short and engaging article:

    Summary: {summary or 'N/A'}
    Research Data: {research_data or 'N/A'}

    Article:
    """

    try:
        result = generator(
            prompt,
            max_length=300,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )

        return result[0]['generated_text'].strip()

    except Exception as e:
        return f"⚠️ Failed to generate article: {str(e)}"
