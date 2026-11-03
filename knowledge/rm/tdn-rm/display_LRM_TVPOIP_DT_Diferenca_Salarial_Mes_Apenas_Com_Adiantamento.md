---
content_hash: f8ad7108b4f2b0e61bbd5b62e3cfb289682d502c163921a20b2479a000f8672e
fetched_at: '2026-06-29T00:08:16.256847+00:00'
page_id: '244932412'
product: rm
source: tdn-rm
title: TVPOIP_DT_Diferenca_Salarial_Mes_Apenas_Com_Adiantamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPOIP_DT_Diferenca_Salarial_Mes_Apenas_Com_Adiantamento
version: 111
---

# DIFERENÇA SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *A rotina de diferença salarial retroativa está calculando diferença indevidamente para eventos lançados na tabela PFMOVCC da competência atual e período atual com o campo editado igual a 1.* |
| **Solução/Implementação:** | *Ajustado o cálculo da diferença salarial quando há apenas pagamento de adiantamento em competência retroativa e há movimentação por centro de custo no envelope atual.* |
| **Chamados relacionados:** | *TVPOIP* |

divs
