---
content_hash: 88af7c5cd4e6cdf8dfff959a017551e5ddae3b2f1e08ee2d63360de219951844
fetched_at: '2026-06-29T00:06:21.147009+00:00'
page_id: '223162426'
product: rm
source: tdn-rm
title: TTVW05_DT_Base_IRRFPL_AnoCaixa_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVW05_DT_Base_IRRFPL_AnoCaixa_Anterior
version: 1
---

# BASE DE IRRFPL ESTÁ CONSIDERANDO VALORES DO ANO CAIXA ANTERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *IRRF PL* |
| **Situação/Requisito:** | *No cálculo do IRRF de Participação nos Lucros, está sendo considerado na base, valores já lançados no mesmo ano competência, mas no ano caixa anterior.*  *A situação só ocorre em PL lançada na competência dezembro, com caixa janeiro.* |
| **Solução/Implementação:** | *Ajuste na composição da base de IRRF PL para verificar o ano caixa, ao invés do ano competência, ao buscar valores de PL já lançados anteriormente.* |
| **Chamados   relacionados:** | *TTVW05* |
| **Versões/Release:** | *11.82.43* |
