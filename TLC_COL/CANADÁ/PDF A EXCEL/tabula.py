import pdfplumber
import pandas as pd
import re

def extract_tariff_data(pdf_path):
    all_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            
            # Filtrar líneas relevantes (que contienen datos de tarifas)
            for line in lines:
                if re.match(r'^\d{4}\.\d{2}\.\d{2}', line) or re.match(r'^\d{4}\.\d{2}\.\d{1}', line) or re.match(r'^\d{4}\.\d{2}\.00', line):
                    # Procesar la línea para separar en columnas
                    processed = process_tariff_line(line)
                    if processed:
                        all_data.append(processed)
    
    return all_data

def process_tariff_line(line):
    # Patrón para identificar el formato de los datos
    # Busca el patrón de tariff item (ej: 0101.10.00)
    tariff_match = re.search(r'(\d{4}\.\d{2}\.\d{2})', line)
    if not tariff_match:
        tariff_match = re.search(r'(\d{4}\.\d{2}\.\d{1})', line)
    if not tariff_match:
        return None
    
    tariff_item = tariff_match.group(1)
    remaining_text = line.replace(tariff_item, '').strip()
    
    # Separar base rate y staging category (generalmente al final)
    # Buscar los últimos 1-3 palabras que podrían ser base rate y staging
    parts = remaining_text.split()
    
    if len(parts) < 2:
        return None
    
    # Los últimos elementos suelen ser staging category y base rate
    staging_category = parts[-1]
    base_rate = parts[-2]
    
    # Reconstruir la descripción (todo lo que queda en el medio)
    description = ' '.join(parts[:-2])
    
    return [tariff_item, description, base_rate, staging_category]

def main():
    pdf_path = "Lista-Productos-de-Canada.pdf"
    excel_path = "Tariff_Schedule_Canada.xlsx"
    
    print("Extrayendo datos del PDF...")
    data = extract_tariff_data(pdf_path)
    
    # Crear DataFrame
    df = pd.DataFrame(data, columns=["Tariff Item", "Description of Goods", "Base Rate", "Staging Category"])
    
    # Guardar en Excel
    df.to_excel(excel_path, index=False)
    print(f"Datos guardados en: {excel_path}")
    print(f"Total de registros procesados: {len(data)}")

if __name__ == "__main__":
    main()