---
content_hash: 498b8442f49a1428a0ff3e2f71f5129d3f25dd158e7df17988006c50291167ce
fetched_at: '2026-06-29T00:06:16.283520+00:00'
page_id: '212894768'
product: rm
source: tdn-rm
title: TTJJWD_DT_Pensao_Alimenticia_Recalculo_BaseIRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJJWD_DT_Pensao_Alimenticia_Recalculo_BaseIRRF
version: 1
---

# RECÁLCULO DA BASE DE IRRF NO CÁLCULO DA PENSÃO ALIMENTÍCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Ao calcular Pensão Alimentícia sobre o líquido em um período onde já existia lançamentos de outra competência com o mesmo mês caixa, o valor está ficando incorreto, após o segundo recálculo abatendo o valor de pensão na base de IRRF.* |
| **Solução/Implementação:** | *Não executar o segundo recálculo da base de IRRF no cálculo da pensão alimentícia quando no primeiro recálculo a base ficar abaixo do limite mínimo para desconto de IRRF.* |
| **Chamados   relacionados:** | *TTJJWD* |
| **Versões/Release:** | *11.82.42* |
