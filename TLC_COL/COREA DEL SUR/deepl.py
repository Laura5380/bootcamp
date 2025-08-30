import pandas as pd
import requests
from tqdm import tqdm
import time
import re

# 🔑 Tu API Key de DeepL
API_KEY = "TU_API_KEY_AQUI"
DEEPL_URL = "https://api-free.deepl.com/v2/translate"  # si tienes plan Pro usa "https://api.deepl.com/v2/translate"

# Archivos de entrada y salida
archivo = "Cronograma-Desgravacion-de-Corea.xlsx"
salida = "Cronograma-Desgravacion-de-Corea-Traducido.xlsx"

print(f"📄 Leyendo: {archivo}")
df = pd.read_excel(archivo, dtype=str)

# --- Función para traducir con DeepL ---
def traducir_deepl(texto, target_lang="ES"):
    if pd.isna(texto) or str(texto).strip() == "":
        return texto
    try:
        params = {
            "auth_key": API_KEY,
            "text": str(texto),
            "target_lang": target_lang,
            "source_lang": "EN"
        }
        response = requests.post(DEEPL_URL, data=params)
        result = response.json()
        return result["translations"][0]["text"]
    except Exception as e:
        return f"[Error] {texto}"

# --- Función especial para 'Base Rate' ---
def traducir_base_rate(texto):
    if pd.isna(texto) or str(texto).strip().lower() == "free":
        return texto
    texto = str(texto).strip()

    # Patrón para expresiones como "219.4% or 1,479won/ kg, whichever is greater"
    if "whichever is greater" in texto.lower():
        try:
            traducido = traducir_deepl(texto)
            return traducido.replace("won", "₩")  # opcional: símbolo de won
        except:
            return texto

    # Traducción normal
    try:
        return traducir_deepl(texto)
    except:
        return texto

# --- Traducción de 'Description of Goods' ---
print("🌐 Traduciendo 'Description of Goods' → español…")
columna_desc = "Description of Goods"
valores = df[columna_desc].tolist()
traducidos = []

for i in tqdm(range(len(valores))):
    traducidos.append(traducir_deepl(valores[i]))
    time.sleep(0.3)  # evita límite de peticiones

df[columna_desc] = traducidos

# --- Traducción de 'Base Rate' ---
print("💰 Traduciendo 'Base Rate'…")
df["Base Rate"] = df["Base Rate"].apply(traducir_base_rate)

# --- Guardar ---
df.to_excel(salida, index=False)
print(f"✅ Traducción terminada. Guardado en: {salida}")
