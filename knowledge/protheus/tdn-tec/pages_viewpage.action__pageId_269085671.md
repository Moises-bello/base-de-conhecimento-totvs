---
content_hash: 6b5192d1d61c0f41388bfaeb50fc84efe17fc40c11eb195e5678527f332faf0d
fetched_at: '2026-07-02T19:24:22.270226+00:00'
page_id: '269085671'
product: protheus
source: tdn-tec
title: PARSER SQL ORACLE - Criar chave para mudar comportamento da instrução LIKE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085671
version: 1
---

Diferença de comportamento da instrução LIKE que gera diferença com o comportamento nos bancos INFORMIX e SQLSERVER

|  |  |
| --- | --- |
| Situação | Os bancos INFORMIX e SQLSERVER tem comportamento diferente para a instrução LIKE. |
| Ocorrência |  |
| Correção | Implementado a tradução para o comando LIKE onde quando banco for ORACLE, o comando será traduzido para REGEXP\_LIKE. Esse comportamento poderá ser ligado ou desligado através da chave de ini "TranslateLikeOracle". Por default, o comportamento de tradução é desligado. |
| Informações adicionais | * Referente ao chamado:TVRFIC * Referente à ocorrência: TTEC-897 * Disponível em builds superiores a 7.00.131227a - 1.3.1 |
