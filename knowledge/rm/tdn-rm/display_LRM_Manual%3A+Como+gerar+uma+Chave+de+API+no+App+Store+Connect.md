---
content_hash: 0d778257e97ffa9a36d80434add90a9c7f8d019c59eb12fcc87c478b7ba891c5
fetched_at: '2026-06-29T00:05:51.726091+00:00'
page_id: '1054123278'
product: rm
source: tdn-rm
title: 'Manual: Como gerar uma Chave de API no App Store Connect'
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual%3A+Como+gerar+uma+Chave+de+API+no+App+Store+Connect
version: 1
---

Este guia tem como objetivo auxiliá-lo na geração da Chave de API (API Key) da sua conta de desenvolvedor da Apple. Essa chave é necessária para que nossa equipe possa realizar integrações, automações ou publicações do seu aplicativo de forma segura.  
  
**⚠️ Importante antes de começar:**

* Você precisa ter acesso de Titular da Conta (Account Holder) no App Store Connect para gerar essas chaves.
* O arquivo gerado no final deste processo só pode ser baixado uma única vez. Guarde-o em segurança.

## **Passo 1: Acesse o App Store Connect**

1. Acesse o portal do [App Store Connect](https://appstoreconnect.apple.com/).
2. Faça o login com o seu ID Apple.

## **Passo 2: Navegue até a área de Integrações**

1. Na página inicial, clique no ícone "Usuários e Acesso" (Users and Access)

      2. No menu superior, clique na aba "**Integrações**" (Integrations).

## **Passo 3: Acesse a seção da API**

1. No menu lateral esquerdo, em "**Keys**" (Tipo de Chave), clique em **"App Store Connect API"**.

       2. Selecione a opção **"Solicitar Acesso" (Request Access).** Basta aceitar os termos e clicar em enviar.

## **Passo 4: Gerar a nova Chave de API**

1. Clique no botão "+" **(Sinal de adição)** ou em **"Generate API Key"** (**Gerar Chave de API**).

       2. Uma janela vai se abrir para você configurar a chave.

       3. No campo **"Name"** **(Nome)**, digite um nome para identificar a chave (Ex: **AppStore\_<Nome do seu app>**).

       4. No campo **"Access"** **(Acesso)**, selecione a função **"Gerente de Apps" (App Manager)** 

       5. Clique em **"Generate" (Gerar).**

**Passo 5: Coletar os dados e enviar**

1. **Issuer ID (ID do Emissor):** Fica na parte superior da página. Clique em "Copy" (Copiar).
2. **Key ID (ID da Chave):** Fica na linha da chave que você acabou de criar.
3. **Arquivo .p8:** Na mesma linha da chave, clique em **"Download API Key"**.   
   **⚠️ Atenção***: Uma mensagem avisará que o download só pode ser feito uma vez. Confirme o download.*

## **Passo 6: Envio Seguro**

Por favor, envie-nos os dados da seguinte forma para mantermos a segurança:

* Envie o **Issuer ID** e o **Key ID** no corpo do e-mail.
* Anexe o arquivo **.p8** baixado.
