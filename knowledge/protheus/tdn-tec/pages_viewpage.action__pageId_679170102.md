---
content_hash: 934ffc060a62ac74abe43dfeb96522945e0842880095ee659590c1e6eb2cb765
fetched_at: '2026-07-02T19:24:27.733251+00:00'
page_id: '679170102'
product: protheus
source: tdn-tec
title: Correção - Com o parâmetro -OLDDPI rotinas 4GL apresentam os botões de ação
  com fonte muito grande
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679170102
version: 1
---

Ao ativar o parâmetro -OLDDPI o tamanho da interface deveria se assemelhar a uma tela sem escalonamento.

|  |  |
| --- | --- |
| Situação | Em telas com escalonamento os botões de ação de rotinas 4GL aparecem com fonte muito grande mesmo com o parâmetro -OLDDPI. |
| Ocorrência | A fonte destes botões acaba não sendo escalonada para 100% como deveria ser com o parâmetro ligado. |
| Correção | O estilo de fonte foi alterado quando o parâmetro estiver ligado, já que a fonte do estilo atual não obedece as instruções de escalonamento corretamente. |
| Informações adicionais | * Referente ao chamado: #LOGIX-95 * Referente à ocorrência: DTCLIENT01-3323 * Disponível em builds superiores a 20.3.0.3 |
