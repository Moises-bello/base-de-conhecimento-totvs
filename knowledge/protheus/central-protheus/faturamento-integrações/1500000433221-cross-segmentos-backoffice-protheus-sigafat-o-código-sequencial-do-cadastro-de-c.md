---
article_id: 1500000433221
category: Faturamento - Integrações
content_hash: 2f4e7d9288f49e6c5dd2b20b029b2038509e06bdfeb4aa61f205bcbdd7fcf166
fetched_at: '2026-06-28T22:38:26.520331+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - O código sequencial do cadastro
  de cliente Vtex não segue o Padrão do Protheus, como validar os campos A1_COD e
  A1_LOJA na integração
type: support-article
updated_at: '2025-04-07T12:44:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000433221-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-O-c%C3%B3digo-sequencial-do-cadastro-de-cliente-Vtex-n%C3%A3o-segue-o-Padr%C3%A3o-do-Protheus-como-validar-os-campos-A1-COD-e-A1-LOJA-na-integra%C3%A7%C3%A3o
---

**Ocorrência**

O código sequencial do cadastro de cliente Vtex não segue o Padrão do Protheus, como validar os campos **A1\_COD** e **A1\_LOJA** na integração.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Causa**

Quando o Vtex integra com o Protheus  o campos **A1\_COD** assume a numeração dos **8 primeiros dígitos** da chave única do Vtex, exemplo:

* **Chave única do Vtex:** InternalId":"b7ab9d5n-ce24-43a2-8a5f-419f61ad1a38",
* **CustomerVendorId:** "b7ab9d5n-ce24-43a2-8a5f-419f61ad1a38"
* O sistema grava no Protheus A1\_COD = b7ab9d5n

**Solução**

Esta é uma tratativa padrão da integração, então mesmo que utilize GetSxeNum ou numeração por CNPJ no código do cliente (A1\_COD) no Protheus, o sistema permanece gravando os 8 primeiros dígitos da chave única  do Vtex. 

Para mudar esse comportamento utilize os Pontos de entrada abaixo:

* **[MTI030NOM - Permite a inclusão de campos customizados no array](https://tdn.totvs.com/x/SAvMCg)**
* **[MT030EAI - Executado antes da chamada da rotina automática do cadastro de Cliente](https://tdn.totvs.com/x/4yIlD)**
