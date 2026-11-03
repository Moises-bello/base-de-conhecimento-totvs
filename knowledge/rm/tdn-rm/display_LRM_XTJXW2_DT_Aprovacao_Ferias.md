---
content_hash: 86e37d9db0338fd94c00b7e4aa732293ef2226396250a78d3c42ec83cc62bba4
fetched_at: '2026-06-29T00:08:14.836038+00:00'
page_id: '244718307'
product: rm
source: tdn-rm
title: XTJXW2_DT_Aprovacao_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/XTJXW2_DT_Aprovacao_Ferias
version: 119
---

# Aprovação Dados Cadastrais

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Aprovação Dados Cadastrais* |
| **Situação/Requisito:** | Ao realizar o processo de aprovação de férias que foram cadastradas pelo portal o sistema emite um erro informando que o funcionário possui 0 dias de direito de férias. |
| **Solução/Implementação:** | Ajuste na rotina de aprovação de férias para tratar o valor de faltas como dias e não como horas. Sistema considerava o valor em horas como se fossem dias, por este motivo o sistema descontava os dias de férias de direito de acordo com quantidade de faltas. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | XTJXW2 |
| **Requisito (ISSUE):** |  |

divs
