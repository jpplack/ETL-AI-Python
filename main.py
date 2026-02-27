import csv
import pandas as pd
import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv(dotenv_path="key.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERRO: Chave API não encontrada!")
else:
    client = genai.Client(api_key=api_key)
    
#tabela de usuarios (EXTRACT- Extração)
usuarios = [
    {"id": 1, "nome": "Pedro Putinatti", "faixa": "marrom", "objetivo": "passagem de guarda"},
    {"id": 2, "nome": "Maria Luiza", "faixa": "azul", "objetivo": "melhorar guarda"},
    {"id": 3, "nome": "Luiz Magalhães", "faixa": "branca", "objetivo": "melhorar finalizações"}
]
#cria tabela do pandas
df = pd.DataFrame(usuarios)

#TRANFORM (Uso da IA)
def gerar_dica_jj(row):
    try:
        print(f"Solicitando sabedoria para {row['nome']}... ⌛")
        time.sleep(10)

        prompt = (f"Aja como mestre de Jiu-Jitsu. O atleta {row['nome']} é faixa {row['faixa']} "
                  f"e quer {row['objetivo']}. Dê uma dica técnica de Jiu-Jitsu moderno "
                  f"e uma dica de Jiu-Jitsu Old School. Seja breve (2 linhas).")
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Erro na IA: {e}"

print("Solicitando dicas ao Jiujitsuka Gemini... 🥋")
df['dica_ia'] = df.apply(gerar_dica_jj, axis=1)

#LOAD (carreando[voltando para o usuario])
df.to_csv('meu_projeto_SDW.csv', 
          index=False,
          sep=';',
          encoding='utf-8-sig',
          quoting=csv.QUOTE_ALL)

print("Domo Arigato Gosaimashita! Se torne um Jiujitisuka cada vez melhor, até logo pupilo! 🥋🥋 ")
