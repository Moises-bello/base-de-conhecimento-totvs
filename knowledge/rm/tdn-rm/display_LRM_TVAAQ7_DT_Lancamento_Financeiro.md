---
content_hash: 97f3078e3bc0e9caaffab6318a6d8de712b8a96c753ca1fcb395c9934f66e90a
fetched_at: '2026-06-29T00:08:13.360910+00:00'
page_id: '244416991'
product: rm
source: tdn-rm
title: TVAAQ7_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TVAAQ7_DT_Lancamento_Financeiro
version: 115
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Informe a função.* |
| **Situação/Requisito:** | Ao gerar sefip com lançamento financeiro é emitido erro: Não é permitido lançamento com valor original igual a zero |
| **Solução/Implementação:** | Ajuste realizado para que lançamentos financeiros com valor zerado, gerados a partir da rotina SEFIP, não sejam enviados para o fluxus, pois não é possível gerar um lançamento financeiro zerado |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVAAQ7 TVGXA2 |
| **Requisito (ISSUE):** |  |

divs
