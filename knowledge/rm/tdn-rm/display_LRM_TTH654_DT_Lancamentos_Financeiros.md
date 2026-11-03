---
content_hash: 047ee05633558f98b54d5ccb41084f0a51d51c6d2a807f2e9980a59c69aa2877
fetched_at: '2026-06-29T00:06:11.964745+00:00'
page_id: '204966650'
product: rm
source: tdn-rm
title: TTH654_DT_Lancamentos_Financeiros
type: documentation
url: https://tdn.totvs.com/display/LRM/TTH654_DT_Lancamentos_Financeiros
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
| **Chamados relacionados:** | TTH654 |
| **Versões/Release:** | *11.82.40* |
