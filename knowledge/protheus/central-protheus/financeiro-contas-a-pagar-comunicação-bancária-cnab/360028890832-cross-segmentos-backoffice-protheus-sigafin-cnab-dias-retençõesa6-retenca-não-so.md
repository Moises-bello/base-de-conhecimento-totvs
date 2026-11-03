---
article_id: 360028890832
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 2239b9e96ebb9fef7b91aa4e0f0102a629bb52d21a5510212ae3fcd3f702b7d3
fetched_at: '2026-06-28T22:37:56.465648+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - CNAB - Dias Retenções(A6_RETENCA)
  não soma a Data Disponibilidade(E5_DTDISPO)
type: support-article
updated_at: '2024-08-26T20:43:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028890832-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-CNAB-Dias-Reten%C3%A7%C3%B5es-A6-RETENCA-n%C3%A3o-soma-a-Data-Disponibilidade-E5-DTDISPO
---

**Ocorrência**No módulo **Financeiro**, após processar o arquivo envido pelo banco através da rotina **Retorno de Cobrança(FINA200)** não foi considerado D+1 informado no campo **Dias Retenca(A6\_RETENCA)** no cadastrado de Banco e somado na **Data de Disponibilidade(E5\_DTDISPO)**.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – CNAB -  A partir da versão 12  
  
**Causa**No arquivo de configuração, existe um posição chamada **Data Credito**. O banco envia o arquivo de retorno com esta data definida na posição citada. A rotina **Retorno de Cobrança** não considera o campo **Dias Retenca**(**A6\_RETENCA**), será considerado a **Data Credito** que o banco envia no **arquivo de retorno** e gravado no campo **Data de Disponibilidade**(**E5\_DTDISPO**).

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajuste o arquivo de configuração de retorno, zerando a posição **Data Credito** e com isso não será considerado a Data do mesmo quando o banco envia no **arquivo de retorno**. Será somado os dias de retenções de acordo com o conteúdo preenchido no campo **Dias Retenca**(**A6\_RETENCA**) com base na data logado que está processando o **arquivo de retorno** na rotina **Retorno de Cobrança(FINA200)**.
