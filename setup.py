import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Cargar variables de entorno desde .env
load_dotenv(Path('..') / '.env')

# Verificar que la clave esté configurada
api_key = os.getenv('GEMINI_API_KEY')
if api_key:
    print(f'✅ Clave de API configurada: {api_key[:8]}...')
else:
    print('❌ GEMINI_API_KEY no encontrada. Configura tu archivo .env')

# Crear cliente Gemini con la clave del entorno
client = genai.Client(api_key=api_key)

def elegir_modelo_disponible(client, candidatos):
    disponibles = []
    for m in client.models.list():
        nombre = getattr(m, 'name', '')
        if 'generateContent' in getattr(m, 'supported_actions', []):
            disponibles.append(nombre)

    for candidato in candidatos:
        if candidato in disponibles:
            return candidato, disponibles

    if disponibles:
        return disponibles[0], disponibles

    raise RuntimeError('No hay modelos de Gemini disponibles para generateContent en esta cuenta.')

MODELO_FLASH, _modelos_disponibles = elegir_modelo_disponible(
    client,
    ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash']
    )
MODELO_PRO, _ = elegir_modelo_disponible(
    client,
    ['gemini-2.5-pro', 'gemini-1.5-pro', MODELO_FLASH]
    )

print(f'✅ Modelo de texto seleccionado: {MODELO_FLASH}')
print(f'✅ Modelo avanzado seleccionado: {MODELO_PRO}')