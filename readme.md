# 🥋 Jiu-Jitsu ETL AI Sentinel

Este projeto foi desenvolvido como parte do desafio **Santander Dev Week 2023 (DIO)**, reimaginado para o contexto de alta performance no Jiu-Jitsu. O sistema automatiza a criação de dicas técnicas personalizadas utilizando a API do **Google Gemini**.



## 🚀 Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal do pipeline.
* **Pandas**: Manipulação e estruturação de dados (CSV/DataFrames).
* **Google GenAI SDK**: Integração com o modelo Gemini 2.5 Flash.
* **Python-dotenv**: Gerenciamento seguro de variáveis de ambiente.

## 🛠️ O Pipeline de Dados
1. **Extract**: Coleta dados de atletas (nome, faixa, objetivo) a partir de estruturas Python ou arquivos CSV.
2. **Transform**: Envia os dados para a IA do Google, que atua como um mestre de Jiu-Jitsu, gerando dicas unindo as escolas *Old School* e *Modern*.
3. **Load**: Exporta os dados enriquecidos para um arquivo `.csv` formatado para o padrão brasileiro (Excel PT-BR).

## 📋 Como Executar
1. Clone o repositório.
2. Crie um arquivo `key.env` e adicione sua `GEMINI_API_KEY`.
3. Instale as dependências:
   ```bash
   pip install pandas google-genai python-dotenv
   python main.py

   🛡️ Segurança e Privacidade
Este projeto utiliza o Free Tier da API do Gemini. Em conformidade com as políticas do Google, dados sensíveis não são processados, apenas informações técnicas esportivas para fins de estudo.

Feito por Pedro Putinatti