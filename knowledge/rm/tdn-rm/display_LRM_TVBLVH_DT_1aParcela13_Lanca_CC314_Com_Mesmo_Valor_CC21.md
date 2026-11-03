---
content_hash: 0cfcf308b9d3545e7750d7a29bd29dbf5946494981882663108c85ebebabe7da
fetched_at: '2026-06-29T00:08:10.591367+00:00'
page_id: '240307519'
product: rm
source: tdn-rm
title: TVBLVH_DT_1aParcela13_Lanca_CC314_Com_Mesmo_Valor_CC21
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBLVH_DT_1aParcela13_Lanca_CC314_Com_Mesmo_Valor_CC21
version: 1
---

# 1a.PARCELA DE 13o.SALÁRIO ESTÁ LANÇANDO CC314 COM MESMO VALOR DO CC21 JÁ EXISTENTE NO ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o.Salário* |
| **Situação/Requisito:** | *Quando está sendo lançada a 1a.parcela de 13o. em um mesmo envelope de folha, onde já existe o evento de desconto do Arredondamento (CC 21), está sendo lançado o evento de Arredondamento Base (CC 314) com o mesmo valor do CC 21.*  *Com isto, no próximo período a ser calculado é descontado novamente o mesmo valor de arredondamento.* |
| **Solução/Implementação:** | *Ajuste no cálculo da 1a.parcela de 13o.salário para que o lançamento o evento de CC 314, Arredondamento Base, iniba o cálculo do CC 21, Arredondamento Desconto.* |
| **Chamados   relacionados:** | *TVBLVH* |
| **Versões/Release:** | *11.83.55* |
