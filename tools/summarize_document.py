from transformers import pipeline

def summarize_document(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    results = summarizer(chunks, max_length=300, min_length=100, do_sample=False)
    return " ".join([r['summary_text'] for r in results])
