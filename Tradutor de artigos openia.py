import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI

# Cliente Azure
client = AzureChatOpenAI(
    azure_endpoint="Url do ponto de extremidade",
    api_key="ApiKey",
    api_version="Versão do GPT",
    deployment_name="Nome do GPT",
    max_retries=0
)

def traduzir_artigo(texto, lang):

    messages = [
        {"role": "system", "content": "Você atua como tradutor de textos"},
        {"role": "user", "content": f"Traduza o seguinte texto para o idioma {lang}:\n\n{texto}"}
    ]

    try:
    
        response = client.predict_messages(messages=messages, max_tokens=500)
        translated_text = response.content  
        print("Texto traduzido:")
        print(translated_text)
        return translated_text

    except Exception as e:

        print(f"Erro ao traduzir o artigo: {e}")
        return None

def extrair_texto_do_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for script_or_style in soup(['script', 'style']):
                script_or_style.decompose()

            texto = soup.get_text(separator=' ')
            return texto.strip()
        else:
            print(f"Falha ao acessar URL. Código de status: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro ao acessar URL: {e}")
        return None

# Entrada do usuário
url = input("Digite o url: ")
texto = extrair_texto_do_url(url)

if texto:
    traduzir_artigo(texto, "português")
else:
    print("Não foi possível extrair o texto do URL.")
