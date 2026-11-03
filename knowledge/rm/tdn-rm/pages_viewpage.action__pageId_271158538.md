---
content_hash: f1ef6fa3a729db322153bfe6b4322ba986ece251c63b74b19a85d591883ce1ce
fetched_at: '2026-06-29T00:08:25.833217+00:00'
page_id: '271158538'
product: rm
source: tdn-rm
title: 330816 MEDU-1997 DT Relatório Balancete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271158538
version: 113
---

# Relatório Balancete

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Balancete |
| **Situação/Requisito:** | Ao gerar o relatório balancete, o saldo atual das contas de passivo é informado com sinal negativo, embora esteja parametrizado para não informação de qualquer sinal que não seja o de conta com saldo diferente de sua natureza. Não obstante, verificamos esta inconsistência também no relatório razão. |
| **Solução/Implementação:** | Ajuste do relatório Balancete para que ao utilizar as opções "3) ou 1)" dos parâmetros do sistema para relatórios, as contas credoras com saldo credor não apresente o sinal e caso seja definido sinal inverso não o imprima nos totalizadores como era feito no Delphi o que causa confusão no usuário que visualiza o relatório. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
