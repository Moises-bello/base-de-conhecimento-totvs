---
content_hash: 5aa86c91237af4dbe85fa36fb41f1ce7fda4f704d62a39cfecd1c83720867ae5
fetched_at: '2026-06-29T00:09:13.629027+00:00'
page_id: '421380473'
product: rm
source: tdn-rm
title: 3761817 TRCT - Quantidade de Dias de Aviso Prévio Indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421380473
version: 1
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | TRCT |
| **Situação/Requisito:** | Ao cadastrar uma rescisão de Comum Acordo, informando a quantidade de Dias de Aviso indenizado e marcando o parâmetro ‘Aviso prévio indenizado abate 0,5”, o sistema calcula corretamente a quantidade de dias e o valor desse aviso , o mesmo é levado corretamente para o envelope. Porem, ao gerar o TRCT o relatório não respeita o parâmetro e leva a referência de dias divergente do envelope com menos 0,5 dia. |
| **Solução/Implementação:** | Foi alterada a consulta SQL que traz informações para o TRCT assim o relatório passa a respeita o parâmetro: "Abate 0.5 dia aviso prévio indenizado. |
| **Tickets relacionados:** | 3761817 |
