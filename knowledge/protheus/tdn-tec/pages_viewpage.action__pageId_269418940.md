---
content_hash: 1f7240ede70329fd257a044e401b8880f46869c260397ede115d2ae6a65a3579
fetched_at: '2026-07-02T19:24:22.317383+00:00'
page_id: '269418940'
product: protheus
source: tdn-tec
title: TDS atualizado não permite abrir fontes com mesmo nome mas de projetos diferentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269418940
version: 2
---

Ao tentar abrir um segundo fonte com o mesmo nome de um fonte já aberto o TDS não abre o segundo fonte e apenas dá foco no primeiro já aberto.

|  |  |
| --- | --- |
| Situação | TDS atualizado não permite abrir fontes com mesmo nome mas de projetos diferentes. |
| Ocorrência | Ao tentar abrir um segundo fonte com o mesmo nome de um fonte já aberto o TDS não abre o segundo fonte e apenas dá foco no primeiro já aberto. |
| Correção | Foi implementada uma estratégia de comparação que se baseava no nome do recurso. A estratégia foi alterada para comparar o caminho completo dos arquivos. |
| Informações adicionais | * Referente ao chamado: TWJIYO * Referente à ocorrência: SSIM-1286 * Disponível em builds superiores a 11.3.3 |
