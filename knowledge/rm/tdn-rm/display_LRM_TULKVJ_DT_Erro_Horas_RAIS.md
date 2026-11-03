---
content_hash: 91f5137527b8a09844d9ef770ad6e6f356ad6f217390e6ab6b75a30e4f67784c
fetched_at: '2026-06-29T00:06:28.774684+00:00'
page_id: '233760607'
product: rm
source: tdn-rm
title: TULKVJ_DT_Erro_Horas_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TULKVJ_DT_Erro_Horas_RAIS
version: 112
---

# RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *RAIS* |
| **Situação/Requisito:** | Quando o funcionário possui um desconto de banco de horas na rescisão e o valor de desconto é maior que o de proventos, sistema retorna o valor do evento de desconto no campo "Banco de Horas" da RAIS incorretamente. |
| **Solução/Implementação:** | *Ajustado cálculo do valor do banco de horas quando a hora fica negativa. Sistema passa a zerar o valor.* |
| **Chamados relacionados:** | *TULKVJ* |

divs
