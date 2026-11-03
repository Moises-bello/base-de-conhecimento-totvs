---
content_hash: 942999abb5ec715c5e9ea7b4ac8b325c08565f448de0c4d724678e2a5e28f2fc
fetched_at: '2026-07-02T19:24:20.433760+00:00'
page_id: '248580909'
product: protheus
source: tdn-tec
title: Ajuste da aplicação e geração de Patch e Update
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=248580909
version: 2
---

Falha na geração e aplicação de pacotes de atualização (\_patchs\_) em RPO configurado para russo (`rpoLanguage=russian`).

|  |  |
| --- | --- |
| Situação | Falha na geração e aplicação de pacotes de atualização (\_patchs\_) em RPO configurado para russo (`rpoLanguage=russian`). |
| Ocorrência | TDS não identificava o ambiente configurado para uso de russo, |
| Correção | Corrigido o tratamento da chave `rpoLanguage`, passando a tratar russo. |
| Informações adicionais | * Referente ao chamado: TVZVPQ * Referente à ocorrência: <http://jira.totvs.com/browse/SSIM-1212> * Disponível em builds superiores a 11.3.2.201607211753 |
