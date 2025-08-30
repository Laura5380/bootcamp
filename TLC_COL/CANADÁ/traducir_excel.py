import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm
import re
import time

# Archivo de entrada y salida
archivo = "Lista-Productos-Canada-Limpio-v2.xlsx"
salida = "Lista-Productos-Canada-Traducido.xlsx"

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
    except Exception as e:
        return f"[Error] {texto}"

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
    if pd.isna(texto) or texto.strip().lower() == "free":
        return texto
    match = re.match(r"(\d+)% but not less than ([\d\.]+)¢ each", str(texto))
    if match:
        return f"{match.group(1)}% pero no menos de {match.group(2)}¢ cada uno"
    try:
        return translator.translate(str(texto))
    except:
        return texto

# --- Traducción por lotes ---
print("🌐 Traduciendo 'Description of Goods' → español…")
columna_desc = "Description of Goods"
batch_size = 20
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
