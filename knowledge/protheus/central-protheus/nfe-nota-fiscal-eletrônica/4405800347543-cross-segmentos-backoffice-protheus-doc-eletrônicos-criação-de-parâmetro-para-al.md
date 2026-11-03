---
article_id: 4405800347543
category: NFe - Nota Fiscal Eletrônica
content_hash: 6295d76d207788fd6ad615d29480e63e250b46931a5f8959f7961ab636a517de
fetched_at: '2026-06-28T22:40:01.817330+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Criação de parâmetro
  para alteração da descrição de produto na nota complementar de ICMS'
type: support-article
updated_at: '2021-11-08T17:42:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405800347543--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Cria%C3%A7%C3%A3o-de-par%C3%A2metro-para-altera%C3%A7%C3%A3o-da-descri%C3%A7%C3%A3o-de-produto-na-nota-complementar-de-ICMS
---

**Dúvida**Como criar o parâmetro para alteração da descrição de produto na nota complementar de ICMS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

## **01. VISÃO GERAL**

Criação de parâmetro **MV\_DSCICMS** para ser utilizado em **Nota de Entrada Complementar de ICMS**, a fim de substituir a descrição do produto que consta na *tag***<xProd>,** pela descrição que será inserida automaticamente através deste parâmetro.

## **02. Criação do parâmetro:**

Acesse o módulo**SIGACFG:**

**![](https://tdn.totvs.com/download/thumbnails/629753406/image2021-7-14_18-36-25.png?version=1&modificationDate=1626298585513&api=v2)**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-37-2.png?version=1&modificationDate=1626298622163&api=v2)**

Depois acesse o menu **Ambiente/Cadastros/Parâmetros:**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-38-11.png?version=1&modificationDate=1626298692103&api=v2)**

Acessar a rotina e clicar em **Incluir:**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-39-19.png?version=1&modificationDate=1626298759170&api=v2)**

Preencha o **Nome de Var***.* com o parâmetro **MV\_DSCICMS.**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-41-20.png?version=1&modificationDate=1626298880527&api=v2)**

E selecione o **Tipo 1- Caractere:**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-42-21.png?version=1&modificationDate=1626298941963&api=v2)**

Preencha o conteúdo conforme a descrição que pretende enviar em sua **nota de entrada complementar de ICMS,**como  exemplo: **"NOTA FISCAL COMPLEMENTAR REF A ICMS NAO DESTACADO NA ORIGINAL" :**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-43-17.png?version=1&modificationDate=1626298997307&api=v2)**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-44-46.png?version=1&modificationDate=1626299086637&api=v2)**

Clique em **Salvar:**

**![](https://tdn.totvs.com/download/attachments/629753406/image2021-7-14_18-45-8.png?version=1&modificationDate=1626299108937&api=v2)**

Com isso o processo de criação do **parâmetro será finalizado.**
