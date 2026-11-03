---
content_hash: 34b7ded78ef355327fb5d278c6ab08a51122fa81659f43036d7d03b3a6a50c38
fetched_at: '2026-06-29T00:08:34.906905+00:00'
page_id: '274852229'
product: rm
source: tdn-rm
title: 347882 FOPROTINAS01-10 DT HomologNet Campo 71 (Salário Líquido do Mês Anterior
  à Rescisão)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274852229
version: 107
---

# HOMOLOGNET

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração do HomologNet |
| **Situação/Requisito:** | O sistema não está validando se o salário do mês anterior a rescisão já foi pago ou não. Quando é gerado o HomologNet para um funcionário que teve pagamento do salário no mês anterior a rescisão, o sistema não identifica que já foi pago e leva o valor para o arquivo. |
| **Solução/Implementação:** | Uma vez que o sistema não oferece atualmente um modo seguro de garantir que o salário foi pago, será criado um lookup para utilização de fórmula para indicar se o salário do mês anterior à rescisão de determinado funcionário foi pago ou não. Dado um funcionário, a fórmula deverá retornar TRUE se o salário do mês anterior à rescisão dele foi pago, ou FALSE, caso contrário. |
| **Tickets relacionados:** | 347882 |

divs
