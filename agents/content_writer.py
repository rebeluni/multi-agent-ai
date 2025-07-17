from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ✅ Public model that works
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set up generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def run_content_writer(summary, research_data):
    prompt = f"""
    You're a professional AI business writer. Based on the summary and research below, write a short article:

    Summary: {summary}
    Research: {research_data}

    Article:
    """

    result = generator(
        prompt,
        max_length=300,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

    return result[0]['generated_text']
