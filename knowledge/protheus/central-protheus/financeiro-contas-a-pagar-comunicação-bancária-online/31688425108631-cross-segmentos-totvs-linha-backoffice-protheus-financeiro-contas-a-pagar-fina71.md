---
article_id: 31688425108631
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: b0c8251f143e39e23f40a8fbf51a0b3de613b48f35136705685eb3191b660b9c
fetched_at: '2026-06-28T22:37:49.970734+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Pagar
  - FINA717 - Não grava informações de Juros/Multa para boletos
type: support-article
updated_at: '2025-04-28T11:41:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31688425108631-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Pagar-FINA717-N%C3%A3o-grava-informa%C3%A7%C3%B5es-de-Juros-Multa-para-boletos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31688425101975) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao realizar a transmissão de pagamentos via **API de (Boletos) - Modelo 30/31, não está gerando informação de juros / multa.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois os campos de **Juros e Multa** não estão devidamente configurados no **Novo Gestor Financeiro (FINA710) - Configuração de Contas**  
  
**Solução**A API do BB permite um campo de **Juros / Multa** para boletos, através da tag no JSON **valorMoraMulta**, neste caso, é necessário acessar a rotina **FINA710 - Configuração de Contas** e informar o campo de **Juros / Multa em (Multa)** conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31688434577047)

Após a transmissão, os dados de Juros / Multa serão enviados ao banco. 

**Saiba mais**  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)
