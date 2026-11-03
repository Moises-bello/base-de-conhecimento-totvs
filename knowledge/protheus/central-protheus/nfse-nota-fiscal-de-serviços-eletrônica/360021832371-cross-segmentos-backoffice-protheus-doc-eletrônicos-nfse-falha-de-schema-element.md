---
article_id: 360021832371
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 337007da1dc35ca7192c743ba708db430c83f16c42df97c5b801d9e5888c351e
fetched_at: '2026-06-28T22:39:57.433460+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Falha de
  schema: Element Servico is not expected. Expected is Prestador'
type: support-article
updated_at: '2025-10-29T21:42:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021832371-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Falha-de-schema-Element-Servico-is-not-expected-Expected-is-Prestador
---

**Ocorrência**No módulo Faturamento, ao tentar realizar a transmissão pela rotina **FISA022** é apresentada a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32272179898263)

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Causa**Esse incidente ocorre pois há mais de um item na nota que está sendo transmitida, porém o layout webservice da Prefeitura em questão **não permite esta operação.**  
  
**Solução**Altere o parâmetro MV\_ITEMAGL para S para que os itens sejam aglutinados no XML **e reinicie o ERP (necessário).**

Para que esta operação funcione, os itens inseridos devem possuir o mesmo valor de:  
  
- CNAE (B1\_CNAE);  
- Tributação Municipal (B1\_TRIBMUN);  
- Código de serviço (B1\_CODISS);  
- Alíquota (B1\_ALIQISS).
