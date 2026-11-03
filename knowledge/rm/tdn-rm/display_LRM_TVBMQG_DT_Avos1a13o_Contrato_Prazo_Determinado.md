---
content_hash: 0bc639b41c0a684335d3fead0b5393eb2132a450fb3ca0a2ba5f42cddaa3fc36
fetched_at: '2026-06-29T00:08:10.097527+00:00'
page_id: '240301232'
product: rm
source: tdn-rm
title: TVBMQG_DT_Avos1a13o_Contrato_Prazo_Determinado
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBMQG_DT_Avos1a13o_Contrato_Prazo_Determinado
version: 1
---

# CONTAGEM DE AVOS 13o. COM CONTRATO POR PRAZO DETERMINADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o.Salário* |
| **Situação/Requisito:** | *Ao lançar o evento de Adiantamento da Primeira Parcela do 13º Salário, está sendo pago 12/12 avos para funcionário com contrato de trabalho por Prazo Determinado, com data de término na competência atual.*  *Quando a data final do Contrato é em competências posteriores, a contagem dos avos fica correta.* |
| **Solução/Implementação:** | *Ajuste no cálculo do evento de CC 9, Adiantamento da Primeira Parcela do 13º Salário, para considerar somente os avos até o final do Prazo Determinado, para funcionários com Contrato sendo finalizado na competência corrente.* |
| **Chamados   relacionados:** | *TVBMQG, TVBZ19* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
