---
content_hash: 2a0fa10b421f8b8a6c524963ab2adfe09d50db614f50e092ee792d8117b3ea38
fetched_at: '2026-06-29T00:06:16.286411+00:00'
page_id: '212894795'
product: rm
source: tdn-rm
title: TTPBR2_DT_Pensao_Alimenticia_Recalculo_BaseIRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPBR2_DT_Pensao_Alimenticia_Recalculo_BaseIRRF
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
| **Chamados   relacionados:** | *TTPBR2* |
| **Versões/Release:** | *12.1.9* |
