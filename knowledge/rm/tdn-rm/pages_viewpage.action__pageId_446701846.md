---
content_hash: 620e4649c6cf47d1a0868b2e0c2ea4f304c198ea3e54fffa0cb1e855dfe82d89
fetched_at: '2026-06-29T00:09:55.090101+00:00'
page_id: '446701846'
product: rm
source: tdn-rm
title: 4213896 FOPCALCULO01-5265 Tabela PFVERBASDIS - presença do IRRF FÉRIAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=446701846
version: 2
---

# Diferença de Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de férias |
| **Situação/Requisito:** | Ao calcular a diferença de Férias, o sistema está gerando um valor de IRRF de Férias indevido nas verbas de diferenças (Tabela PFVERBASDIS) pois esse valor não será levado o envelope de diferença, já que o cálculo do IRRF é Caixa.  Esse problema reflete no eSocial, pois será levado no XML através da Tabela PFVERBASDIS, um desconto de IRRF Férias incorreto. |
| **Solução/Implementação:** | Ajuste para não gravar dados do IRRF Férias na tabela PFVERBASDIS. |
| **Tickets relacionados:** | 4213896; 4257278 |
