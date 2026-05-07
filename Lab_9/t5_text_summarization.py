from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "t5-small"

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

text = """
Artificial intelligence is transforming the world.
It helps in automation, data analysis, and decision making.
Many industries rely on AI to improve efficiency and accuracy.
AI is also used in healthcare, education, and robotics.
"""

input_text = "summarize: " + text

inputs = tokenizer.encode(
    input_text,
    return_tensors="pt",
    max_length=512,
    truncation=True
)

summary_ids = model.generate(
    inputs,
    max_length=50,
    min_length=20,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("Original Text:\n", text)

print("\nSummary:\n", summary)