# Tradutor de Artigos com Azure OpenAI

Este projeto permite traduzir textos extraídos de URLs para o idioma desejado utilizando a API Azure OpenAI e a biblioteca BeautifulSoup para processar o HTML das páginas.

## Funcionalidades

### Extração de Texto de URLs:

Acessa uma página da web e extrai o texto principal, removendo scripts e estilos.

### Tradução via Azure OpenAI:

Traduz o texto extraído para o idioma especificado pelo usuário usando o modelo de linguagem OpenAI hospedado no Azure.

## Tecnologias Utilizadas

Python

Requests: Para realizar requisições HTTP.

BeautifulSoup (bs4): Para processar e extrair o conteúdo HTML.

Azure OpenAI: Para a tradução dos textos.

## Como executar

Configure os seguintes valores para o cliente Azure OpenAI:

URL do ponto de extremidade

Chave da API

Versão do GPT

Nome do deployment

Esses valores devem ser fornecidos no código, na inicialização do cliente AzureChatOpenAI.
