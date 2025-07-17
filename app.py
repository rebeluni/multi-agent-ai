from agents.document_parser import run_document_parser
from agents.market_researcher import run_market_research
from agents.content_writer import run_content_writer
from agents.tool_logger import run_logger
from agents.validator import validate_article  # ✅ new validator

doc_text = """
Generative AI is transforming the financial sector. It helps create synthetic financial data, automate compliance tasks, and enhance customer service with intelligent agents. Major banks are adopting these technologies to increase efficiency and reduce fraud.
"""

topic = "Generative AI in Finance"

# Step 1: Document Parsing
summary = run_document_parser(doc_text)

# Step 2: Market Research
research = run_market_research(topic)

# Step 3: Content Writing
article = run_content_writer(summary, research)

# Step 4: Validation Check
is_valid, feedback = validate_article(article)
if not is_valid:
    print("❌ Validation Failed:", feedback)
else:
    # Step 5: Logging to Slack
    status = run_logger(article)
    print("✅ Article sent to Slack! Status:", status)
