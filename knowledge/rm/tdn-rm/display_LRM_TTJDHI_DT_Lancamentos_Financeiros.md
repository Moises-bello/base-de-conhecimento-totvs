---
content_hash: 96b10903f7658b9e9b36dfaec9f8c351fc2d6d3cb81696dc46686bc5b87af56a
fetched_at: '2026-06-29T00:06:11.968225+00:00'
page_id: '204966661'
product: rm
source: tdn-rm
title: TTJDHI_DT_Lancamentos_Financeiros
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJDHI_DT_Lancamentos_Financeiros
version: 2
---

# SEFIP - LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Sefip - Lançamentos Financeiros* |
| **Situação/Requisito:** | Ao gerar a SEFIP com lançamento financeiro, o valor que está compondo a base do FGTS está considerando em duplicidade os dias que o mesmo esteve afastado. |
| **Solução/Implementação:** | Foi criado uma consulta que verifica se no envelope de pagamento existe alguma verba com código de cálculo igual a 315, se existir é realizado o calculo da base do FGTS com base no valor dessa verba. Senão existir, é verificado as verbas que tem incidência para FGTS para realizar o cálculo da base de FGTS. |
| **Chamados relacionados:** | TTJDHI |
| **Versões/Release:** | *12.1.8* |
