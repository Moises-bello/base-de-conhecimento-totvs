---
article_id: 1500002431261
category: NFe - Nota Fiscal Eletrônica
content_hash: 420d17802a84a837ac4cb427f99eda4cd7dd69775a5202714f36222497b72b17
fetched_at: '2026-06-28T22:40:05.038976+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 438 Rejeição :
  Obrigatória as informações do intermediador da transação para operação por site
  de terceiros'
type: support-article
updated_at: '2025-07-14T14:22:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002431261-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-438-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3ria-as-informa%C3%A7%C3%B5es-do-intermediador-da-transa%C3%A7%C3%A3o-para-opera%C3%A7%C3%A3o-por-site-de-terceiros
---

**Dúvida**Como solucionar a rejeição 438 : Obrigatória as informações do intermediador da transação para operação por site de terceiros ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Para ***gerar o intermediador*** realizar os passos abaixo:

1. Preencher o intermediador em  Faturamento -> Cadastros -> Intermediadores **Nome "A1U\_NOME" e CNPJ "A1U\_CGC"**
2. Preencher o  no pedido de vendas **Presença Com** "**C5\_INDPRES"**  igual a  **2**, **3**,ou **9;**
3. Preencher no **Pedido de Venda Cod. Intermed** "**C5\_CODA1U";**
4. Após isso, ***transmita novamente a Nota fiscal eletrônica.***

  

* **Importante:**

 Lembrando que opção  **4=*****NFC-e em operação com entrega a domicílio,*** não é apresentada no pedido de vendas, apenas no módulo do loja.

* **Validação da Sefaz:**

![438_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007651822)

***Segue em anexo uns vídeos dos campos de cadastro.***
