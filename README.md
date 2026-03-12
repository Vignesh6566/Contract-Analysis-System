# Contract Analysis System

A simple NLP application that analyzes legal or contract text and extracts important entities such as person names, organizations, dates, and monetary values using a pretrained Named Entity Recognition (NER) model.

## Features
- **Preprocessing**: Cleans contract text for better entity extraction.
- **NER Extraction**: Extracts `PERSON`, `ORG`, `DATE`, `MONEY`, and `GPE` using spaCy.
- **Interactive Analysis**: Input text directly in the terminal or provide a file.
- **Results Export**: Saves extracted entities to a CSV file.

## Project Structure
```
contract_analysis_system/
│
├── data/               # Sample contract text files
├── src/
│   ├── preprocess.py       # Text cleaning logic
│   ├── entity_extractor.py # NER model wrapper
│   └── analyze_contract.py # Main interactive script
├── results/            # Exported CSV results
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## Installation
1. Install Python 3.x.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage
### Run with terminal input:
```bash
python src/analyze_contract.py
```
After running, type your contract text when prompted.

### Run with a file input:
```bash
python src/analyze_contract.py --file data/sample_contract.txt
```

## Example
**Input:**
"The obligor John Smith shall repay the loan to JPMorgan before 30 June 2026."

**Output:**
```
PERSON: John Smith
ORG: JPMorgan
DATE: 30 June 2026
```

The entities are also saved to `results/extracted_entities.csv`.
