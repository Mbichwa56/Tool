import re
import csv
from PyPDF2 import PdfReader

# === Step 1: Load and extract text from PDF ===
pdf_path = "C:\\Users\\user\\Downloads\\Documents\\Principal and Practice of Management Exam Revision.pdf"  # Replace with your actual PDF path
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# === Step 2: Clean text and extract Q&A blocks ===
# Removes multiple newlines and trims edges
full_text = re.sub(r'\n+', '\n', full_text).strip()

# Finds question blocks starting with numbers: "1. question..."
qa_blocks = re.findall(r'(\d+\.\s+.*?)(?=\n\d+\.|\Z)', full_text, re.DOTALL)

flashcards = []
for block in qa_blocks:
    lines = block.strip().split('\n')
    if len(lines) < 2:
        continue
    question_line = lines[0]
    answer_lines = lines[1:]

    # Clean formatting
    question = re.sub(r'^\d+\.\s+', '', question_line).strip()
    answer = "\n".join([line.strip('- ').strip() for line in answer_lines if line.strip()])

    if question and answer:
        flashcards.append((question, answer))

# === Step 3: Write to CSV ===
output_csv = "anki_flashcards_output.csv"
with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Front", "Back"])
    for q, a in flashcards:
        writer.writerow([q, a])

print(f"✅ Flashcards saved to {output_csv}")
