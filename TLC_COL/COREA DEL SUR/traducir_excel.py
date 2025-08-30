import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm
import re
import time

# Archivo de entrada y salida
archivo = "Cronograma-Desgravacion-de-Corea.xlsx"
salida = "Cronograma-Desgravacion-de-Corea-Traducido.xlsx"

print(f"📄 Leyendo: {archivo}")
df = pd.read_excel(archivo, dtype=str)

# Traductor
translator = GoogleTranslator(source="en", target="es")

# --- Funciones de traducción ---
def traducir_texto(texto):
    if pd.isna(texto):
        return texto
    try:
        return translator.translate(str(texto))
    except Exception:
        return texto

def traducir_batch(lista):
    traducidos = []
    for item in lista:
        if pd.isna(item):
            traducidos.append(item)
        else:
            try:
                traducidos.append(translator.translate(str(item)))
            except:
                traducidos.append(item)
        time.sleep(0.5)  # evita bloqueo
    return traducidos

def traducir_base_rate(texto):
    if pd.isna(texto):
        return texto
    txt = str(texto).strip()

    # Mantener "Free" tal cual
    if txt.lower() == "free":
        return "Free"

    # Caso especial: "% or ... whichever is greater"
    match = re.match(r"([\d\.]+%) or\s+(.+), whichever is greater", txt, re.IGNORECASE)
    if match:
        return f"{match.group(1)} o {match.group(2)}, el que sea mayor"

    # Caso Canadá (por compatibilidad)
    match_old = re.match(r"(\d+)% but not less than ([\d\.]+)¢ each", txt)
    if match_old:
        return f"{match_old.group(1)}% pero no menos de {match_old.group(2)}¢ cada uno"

    # Traducción general
    try:
        return translator.translate(txt)
    except:
        return txt

# --- Traducción por lotes ---
print("🌐 Traduciendo 'Description of Goods' → español…")
columna_desc = "Description of Goods"
batch_size = 40
valores = df[columna_desc].tolist()
traducidos = []

for i in tqdm(range(0, len(valores), batch_size)):
    lote = valores[i:i+batch_size]
    print(f"➡️ Procesando lote {i//batch_size+1} ({len(lote)} filas)…")
    traducidos.extend(traducir_batch(lote))

df[columna_desc] = traducidos

# --- Base Rate ---
print("💰 Traduciendo 'Base Rate'…")
df["Base Rate"] = df["Base Rate"].apply(traducir_base_rate)

# --- Guardar ---
df.to_excel(salida, index=False)
print(f"✅ Traducción terminada. Guardado en: {salida}")
