---
content_hash: a4aee3105f2b1623ee77c8304a4f1305ac4c4276cce6eac45e6adbe5f1fdfb10
fetched_at: '2026-06-29T00:06:29.665549+00:00'
page_id: '234615356'
product: rm
source: tdn-rm
title: DT_TTURW9_Soma_TotalProvento/Descontos_Relatorio_RMReports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234615356
version: 118
---

# SOMA INCORRETA DO TOTAL DE PROVENTOS E DESCONTOS NO RELATÓRIO "FOPREL25.0025 - 2.004.101 - Envelope de pagamento - Labo 05.0.TotvsReport" DO RM REPORTS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar soma do total de proventos e total de descontos do relatório do rm reports corretamente.* |
| **Situação/Requisito:** | Ao gerar o relatorio "FOPREL00025 - Envelope de pagamento - Labo 05.0" o campo "Período" está incorreto, e os campos "Total Proventos" e "Total Descontos" está sendo somado o valor quando é emitido para mais de 1 chapa. |
| **Solução/Implementação:** | Ao gerar o relatorio "FOPREL00025 - Envelope de pagamento - Labo 05.0" sendo que no campo "Período" o valor apresentado deve ser o mesmo informado na tela de "Parametros". O campo "Total Proventos" deve apresentar o valor da soma de proventos da chapa e o campo "Total Descontos" deve apresentar o valor da soma de descontos da chapa. |
| **Chamados relacionados:** | TTURW9 |

divs
