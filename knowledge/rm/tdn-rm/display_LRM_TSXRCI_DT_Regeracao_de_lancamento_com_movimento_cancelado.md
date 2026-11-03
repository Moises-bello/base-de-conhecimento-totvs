---
content_hash: d3fa01e19336e039240298e2ad6b2138cd7fbb20912345a52cb8f9241faa4cef
fetched_at: '2026-06-29T00:06:02.080799+00:00'
page_id: '198943349'
product: rm
source: tdn-rm
title: TSXRCI_DT_Regeracao_de_lancamento_com_movimento_cancelado
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXRCI_DT_Regeracao_de_lancamento_com_movimento_cancelado
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Regeração de lançamentos com movimento cancelado* |
| **Situação/Requisito:** | *Ao tentar regerar um lançamento,aparece a mensagem  "O lançamento possui movimento gerado e não pode ser regerado. ,o movimento esta cancelado no Nucleus".* |
| **Solução/Implementação:** | *Consulta de lançamentos não está considerando a coligada da TMOVLAN pois existem dois registros em coligadas diferentes e um dos movimentos não está cancelado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **Versões/Release:** | *12.1.7* |
