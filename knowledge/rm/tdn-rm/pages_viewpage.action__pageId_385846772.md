---
content_hash: 6eb87632621e6661599ce4a46d31aff4d6d47b162b0ae4b0c730f16344c9c120
fetched_at: '2026-06-29T00:09:07.777180+00:00'
page_id: '385846772'
product: rm
source: tdn-rm
title: DSAUGHCOM-741 DT Soroteca exclusão de amostras cadastradas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385846772
version: 1
---

# Soroteca exclusão de amostras cadastradas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Soroteca |
| **Situação/Requisito:** | Ao excluir um código de barras, mesmo que exista o código, a rotina de exclusão não deleta o registro e ainda informa que não foi possível encontrar o registro. |
| **Solução/Implementação:** | Ajustada a rotina que exclui o registro através do código informado, ao incluir no log (SZSOROTECALOG) não estava preenchendo a coluna DATAVALIDADE, então gerava uma exerção interna e a rotina de exclusão não prosseguia. |
