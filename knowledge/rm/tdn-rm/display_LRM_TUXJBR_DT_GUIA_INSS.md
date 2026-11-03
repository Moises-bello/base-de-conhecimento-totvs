---
content_hash: 9f6ced35162e1785777b8ae68e43ff524924008ab403365548dd11ab8d3ffa53
fetched_at: '2026-06-29T00:08:07.707184+00:00'
page_id: '237385378'
product: rm
source: tdn-rm
title: TUXJBR_DT_GUIA_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXJBR_DT_GUIA_INSS
version: 118
---

# GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Guia de inss* |
| **Situação/Requisito:** | Implementada questões disponibilizadas via dll na versão 12.1.8 para SERVENG: |
| **Solução/Implementação:** | - Otimizada lançamentos financeiros realizados pela tela de  geração de lançamentos, incluído filtro para restringir funcionários demitidos e funcionários em que a data de última movimentação seja anterior a 3 meses da data escolhida de competência na geração do relatório .   - Otimizado agrupamento dos lançamentos financeiros da Guia de Inss , de forma que para cada guia gerada seja gerado 1 lançamento financeiro   - Otimizado consulta de retornar os tomadores do funcionário, pois no join com a tabela FCFOCEI, não era considerado o código do tomador. Como havia mais de um tomador com o mesmo CEI na base do cliente, o sistema trazia o tomador incorreto para a geração da GUIA de inss |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUXJBR TUXXCB |
| **Requisito (ISSUE):** | *.* |

divs
