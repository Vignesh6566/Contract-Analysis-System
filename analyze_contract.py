import os
import pandas as pd
from preprocess import load_contract_text, clean_text
from entity_extractor import EntityExtractor

def run_analysis(text=None, file_path=None):
    extractor = EntityExtractor()
    
    if file_path:
        print(f"Loading and analyzing contract from file: {file_path}")
        raw_text = load_contract_text(file_path)
        text = clean_text(raw_text)
    elif text:
        text = clean_text(text)
    else:
        print("Error: No input provided.")
        return

    entities = extractor.extract_entities(text)
    
    if not entities:
        print("No entities found.")
        return

    print("\nExtracted Entities:")
    print("-" * 30)
    for ent in entities:
        print(f"Entity: {ent['text']}")
        print(f"Type: {ent['label']}")
        print()

    # Save to CSV
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        
    df = pd.DataFrame(entities)
    output_path = os.path.join(results_dir, "extracted_entities.csv")
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Contract Analysis Tool")
    parser.add_argument("--file", help="Path to contract text file")
    args = parser.parse_args()

    if args.file:
        run_analysis(file_path=args.file)
    else:
        print("Contract Analysis System")
        print("Enter contract text below (or press Ctrl+C to exit):")
        user_input = input("> ")
        if user_input:
            run_analysis(text=user_input)
