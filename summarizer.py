import os
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT="""You are a document analyst.
Respond ONLY with valid JSON in this format: 
{
    "summary": "2-3 sentence summary",
    "key_points": ["point 1", "point 2", "point 3"],
    "doc_type": "guidance|policy|report|other"
}"""

def summarize_document(text: str, filename: str) -> dict:
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Sumarize this document: \n\n{text[:3000]}"}
        ]
    )
    
    result = json.loads(response.choices[0].message.content)
    result["filename"] = filename
    return result


def process_folder(folder_path: str) -> list[dict]:
    docs_folder = Path(folder_path)
    results = []

    for file in docs_folder.glob("*.txt"):
        print(f"Processing {file.name}...")
        text = file.read_text(encoding="utf-8")
        result = summarize_document(text, file.name)
        results.append(result)
        print(f"Done. Summary: {result['summary'][:50]}...")
    return results


if __name__ == "__main__":
    results = process_folder("./documents")

    with open("summaries.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nDone. {len(results)} documents processed.")
    print(f"Total key points: {sum(len(r.get('key_points', [])) for r in results)}")
