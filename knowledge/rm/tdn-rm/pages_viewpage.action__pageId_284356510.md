---
content_hash: 3dd8bc04a142e49ece396ef2428276dd2f868527193b2fda8fd729747880c74e
fetched_at: '2026-06-29T00:08:36.117608+00:00'
page_id: '284356510'
product: rm
source: tdn-rm
title: 1008894 EDUCACIONAL01-1445 DT Aproveitamento de crédito em conta corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284356510
version: 103
---

# APROVEITAMENTO DE CRÉDITO EM CONTA CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Aproveitamento de crédito em conta corrente |
| **Situação/Requisito:** | Sistema não está aproveitando créditos em conta corrente do aluno fazendo com que o crédito possa gerar N lançamentos a pagar indevidamente. |
| **Solução/Implementação:** | Ajuste na consulta de créditos em conta corrente para que considere o responsável financeiro correto do crédito na conta corrente do aluno tendo em vista que, quando o sistema está integrado com o Protheus, ele gera o registro de conta corrente na baixa do lançamento para o responsável da parcela e, quando o sistema vai aproveitar o crédito, ele estava consultando o fornecedor do cliente da aba Protheus do "Cliente/Fornecedor" fazendo com que o crédito não fosse encontrado pois o lançamento a pagar é gerado para esse Fornecedor associado citado.    Consideração de aproveitamento de crédito a menor em conta corrente quando o sistema está integrado com o Protheus (Anteriormente, o sistema não estava aproveitando pagamentos a menor quando o sistema estava integrado) |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
