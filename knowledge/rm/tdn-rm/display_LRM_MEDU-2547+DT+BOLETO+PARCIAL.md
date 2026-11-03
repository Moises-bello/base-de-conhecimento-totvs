---
content_hash: 73bdb96ccfc2050ebcf9e66dbbbb76b5455ff75ab867e1903b076f738dac29e7
fetched_at: '2026-06-29T00:08:30.427379+00:00'
page_id: '272431529'
product: rm
source: tdn-rm
title: MEDU-2547 DT BOLETO PARCIAL
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-2547+DT+BOLETO+PARCIAL
version: 108
---

# Baixa Parcial de Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao realizar a baixa de mais de um lançamento vinculado a um único boleto, no momento de incluir o meio de pagamento na baixa completa não foi informado um meio de pagamento para um dos lançamentos. Ao concluir a baixa o sistema não gera um novo boleto para o lançamento com o valor restante. |
| **Solução/Implementação:** | Agora o sistema irá gerar um novo boleto para o lançamento que não participou da baixa do seu boleto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
