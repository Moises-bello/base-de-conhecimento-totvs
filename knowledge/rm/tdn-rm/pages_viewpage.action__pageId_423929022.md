---
content_hash: 5318c3acd75cb6a086d9ba8d3ddb7d4505753d99ca357d94dec069670c6fe817
fetched_at: '2026-06-29T00:09:24.033037+00:00'
page_id: '423929022'
product: rm
source: tdn-rm
title: 4023096 DEDUINTEGRACOES-3540 DT Cancelamento de Remessa/Boleto - Parâmetro
  Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423929022
version: 1
---

# CANCELAMENTO DE REMESSA / BOLETO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Cancelamento de contrato |
| **Situação/Requisito:** | Não está cancelando remessa de boleto, ao tentar cancelar lançamento financeiro, mesmo com o seguinte parâmetro marcado: "Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado" |
| **Solução/Implementação:** | Alteração do **texto** do parâmetro de cancelamento de remessa/boleto: "Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado"  para "Cancelar Remessa automaticamente ao cancelar contrato com lançamento(s) financeiro(s) cujo(s) boleto(s) estiver(em) com status Remetido ou Registrado".  Alteração do **hint** explicativo do parâmetro conforme texto abaixo:  *Durante o cancelamento de Contrato com Lançamento Financeiro que tenha Boleto com status igual a Remetido ou Registrado,*  *o TOVS Educacional realizará automaticamente o cancelamento da remessa desses lançamentos.*  *Para este cenário a remessa ficará como pendente no módulo TOTVS Financeiro, sendo necessário reenviar a remessa ao banco novamente.*  *OBSERVAÇÃO: Parâmetro válido para todos os processos do TOTVS Educacional que cancelam contrato.* |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
