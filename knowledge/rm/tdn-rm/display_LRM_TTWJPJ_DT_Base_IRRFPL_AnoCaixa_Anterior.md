---
content_hash: b1924137ae2ec0c14fece3429f531d2038a2fc33171d9c61a2b87036f32920f6
fetched_at: '2026-06-29T00:06:21.194860+00:00'
page_id: '223163731'
product: rm
source: tdn-rm
title: TTWJPJ_DT_Base_IRRFPL_AnoCaixa_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWJPJ_DT_Base_IRRFPL_AnoCaixa_Anterior
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
| **Chamados   relacionados:** | *TTWJPJ* |
| **Versões/Release:** | *12.1.9* |
