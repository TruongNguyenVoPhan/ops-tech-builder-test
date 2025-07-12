import pandas as pd
import os

def parse_csv(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == '.csv':
        df = pd.read_csv(file_path)
    elif ext in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    else :
        raise ValueError("Unsupported file type")
    
    df.columns = [str(c).strip().lower() for c in df.columns]
    
    column_map = {
        "po_number": ["po_number", "po_no", "po number", "po no"],
        "vendor": ["vendor", "supplier", "company"],
        "amount": ["amount", "total", "cost", "price"]
    }
    
    actual_columns = {}
    
    for key, possible_names in column_map.items():
        for name in possible_names:
            if name in df.columns:
                actual_columns[key] = name
                break
        else:
            actual_columns[key] = None
            
    output = []
    for _, row in df.iterrows():
        amount = str(row.get(actual_columns["amount"])).strip().lower()
        if amount in ["n/a", "na", "none", "null", "??", "-500"]:
            amount = "0"
        
        raw_po_number = row.get(actual_columns["po_number"])
        po_number = str(raw_po_number).strip()
        if po_number.lower() in ["", "nan" ,"n/a", "na", "none", "null"]:
            po_number = ""
        
        item = {
            "po_number": po_number,
            "vendor": row.get(actual_columns["vendor"]).strip(),
            "amount": amount,
        }
        output.append(item)
        
    return output

if __name__ == "__main__":
    result = parse_csv("example.csv")
    for item in result:
        print(item)