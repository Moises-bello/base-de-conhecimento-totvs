---
content_hash: 04dd0aedada49c63c51902e3ffd15ddb8483045e4a398823488a9aa6fca5feef
fetched_at: '2026-06-29T00:06:27.358409+00:00'
page_id: '232820421'
product: rm
source: tdn-rm
title: TUIA09_DT_FuncaoND_Horista_Afastado_Fevereiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIA09_DT_FuncaoND_Horista_Afastado_Fevereiro
version: 3
---

# FUNÇÃO ND INCORRETA EM FEVEREIRO PARA HORISTA COM AFASTAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Função de fórmula “ND” não esta realizando o cálculo corretamente no mês de fevereiro, para funcionários com o recebimento do tipo “Horista”, que possuem afastamentos.* |
| **Solução/Implementação:** | *Ajuste na função de fórmula "ND" no mês de fevereiro, para funcionários com o recebimento do tipo “Horista”, que possuem afastamentos.*  *Quando existem afastamentos no mês, o cálculo da função não estava tratando número de dias total do mês menor que 30.* |
| **Chamados   relacionados:** | *TUIA09, TUJG76* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
