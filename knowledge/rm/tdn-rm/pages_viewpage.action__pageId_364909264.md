---
content_hash: cbf590dd18847b83a6ed09e499d25eb76f2cbcf6b3b8ecfdb1de067f5cc9e2b0
fetched_at: '2026-06-29T00:08:59.667729+00:00'
page_id: '364909264'
product: rm
source: tdn-rm
title: 2939627 CONTROLADORIA01-1500 SPED Contábil (K210)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364909264
version: 88
---

# SPED Contábil - Registro K210

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | SPED Contábil |
| **Situação/Requisito:** | Existem contas do plano de contas que foram associadas a contas do plano consolidado (Bloco K), porém não possuem movimentação ou saldo. Estas contas não são geradas no I050, porém estão sendo levadas no K210. O registro K210 também deverá verificar se o parâmetro "Enviar para o SPED Contábil / ECF Contas Contábeis que não tenha saldo ou movimentação no período da geração?", das rotinas legais, está marcado ou desmarcado. |
| **Solução/Implementação:** | Na geração do SPED Contábil, durante a criação do registro K210, só serão exibidas contas contábeis que estiverem presentes no registro I050. Essa restrição está sendo aplicada somente na coligada responsável por gerar o bloco K. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
