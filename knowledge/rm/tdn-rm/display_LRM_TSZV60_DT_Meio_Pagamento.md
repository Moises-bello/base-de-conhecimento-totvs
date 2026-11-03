---
content_hash: bae14f0ea2c6916fc86125f28fb46fd17841038c636268efb3f33d524b51c04c
fetched_at: '2026-06-29T00:06:04.829925+00:00'
page_id: '200911702'
product: rm
source: tdn-rm
title: TSZV60_DT_Meio_Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZV60_DT_Meio_Pagamento
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Função:** | Meio de Pagamento |
| **Situação/Requisito:** | Consistência ao inserir movimento quando o meio de pagamento é cheque e o tipo de movimento é compras, pois obriga o preenchimento do campo banco, agência, Conta Corrente e cheque. O correto é consistir somente em tipo de movimento de venda |
| **Solução/Implementação:** | Melhoria na inclusão de movimentos quando se utiliza meio de pagamento igual a cheques. Ajuste para consistir os campos banco, agência, Conta Corrente e Cheque em Branco, caso o movimento seja de vendas. Anteriormente consistia para ambos tipos de movimentos |
| **Conversores e Parâmetros:** | Não se aplica |
| **Chamados relacionados:** | Não se aplica |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *12.1.7* |
