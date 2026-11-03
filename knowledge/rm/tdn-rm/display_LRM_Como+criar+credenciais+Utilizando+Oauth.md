---
content_hash: c2cbc22f1de9dac6aa9324449d84686dfde9fc2892feeafc03ce845de3951883
fetched_at: '2026-06-29T00:12:15.368208+00:00'
page_id: '977177700'
product: rm
source: tdn-rm
title: Como criar credenciais Utilizando Oauth
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+criar+credenciais+Utilizando+Oauth
version: 12
---

ATENÇÃO

Funcionalidade disponível a partir das versões:

* 12.1.2502.198
* 12.1.2506.140
ATENÇÃO

**É** altamente recomendável fazer a autenticação OAuth, utilizando uma conta exclusiva para isso, assim, garantimos que o espaço utilizado pelo google drive não será compartilhado com uma conta pessoal.

**Não** recomendamos fazer a autenticação utilizando contas pessoais.

## **01. Como gerar as credenciais OAuth no Google Cloud:**

1. Acesse: <https://console.cloud.google.com/apis/credentials>
2. Se esta for a primeira vez que você faz login no console, **aceite os Termos de Serviço**.

   Demonstração
3. Caso ainda não tenha um projeto, clique em **Selecionar projeto → Novo projeto**, informe um nome e salve.

   Demonstração
4. Após a criação do projeto, clique em **Selecionar projeto → Nome do Seu Projeto**.

   Demonstração
5. Acesse novamente **APIs e serviços → Credenciais** e clique em **Criar credenciais → ID do cliente OAuth**.

   Demonstração
6. Antes de prosseguir, é necessário criar a tela de Consentimento, clique no botão **"Configurar tela de consentimento"**

   Demonstração
7. Preencha as informações de configuração do projeto:

   Demonstração
8. Acesse **Clientes** e clique em **Criar cliente**.

   Demonstração
9. Em **Tipo de aplicativo**, selecione **Aplicativo para computador**.

   Demonstração
10. Dê um nome às credenciais e clique em **Criar**.

    Demonstração
11. Baixe o arquivo `client_secret_XXXXX.json` e guarde-o em local seguro — ele será usado na configuração do RM.

    Demonstração

## **02. Habilitar API Google Drive**

1. No painel de navegação esquerdo, clique em "**APIs & Services**" e depois em "**APIs e serviços ativados.**"
2. No canto superior da tela, clique em "**ATIVAR APIs E SERVIÇOS**".
3. Na barra de pesquisa, digite "**Google Drive API**" e clique no resultado correspondente.
4. Clique no botão "**Ativar**" para habilitar a API do Google Drive para o seu projeto.

   Demonstração

## **03. Publicando o App**

1. No painel de navegação esquerdo, clique em "**Público-alvo**".
2. Clique no botão "**Publicar app**".
3. Na janela que abrir, clique no botão "**Confirmar**".

1. Demonstração

## **04. Autenticando as credenciais**

ATENÇÃO

**Pré-requisto:**

Para esta etapa, é necessário executar o **RM.exe** **como administrador** para concluir a atividade **Autenticar**.

Ressaltamos que essa ação **será exigida apenas para a autenticação** e criação do Conector.

1. Adicionar o arquivo em **Selecionar Arquivo.**
2. Clicar em **Autenticar.**
3. Conectar com a conta do google drive que será utilizada. O email para acesso deve ter permissão para acessar o aplicativo.

   Demonstração
