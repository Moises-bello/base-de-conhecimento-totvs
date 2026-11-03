---
content_hash: 327c878e024a45c09a34fa37f1c6f362b185efc5d24cb6167a936d96e21e1d18
fetched_at: '2026-06-29T00:06:03.513148+00:00'
page_id: '198955902'
product: rm
source: tdn-rm
title: TSTP59_DT_Meio_Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTP59_DT_Meio_Pagamento
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Função:** | Meio de Pagamento |
| **Situação/Requisito:** | Consistência ao inserir movimento quando o meio de pagamento é cheque e o tipo de movimento é compras, pois obriga o preenchimento do campo banco, agência, Conta Corrente e cheque. O correto é consistir somente em tipo de movimento de venda |
| **Solução/Implementação:** | Melhoria na inclusão de movimentos quando se utiliza meio de pagamento igual a cheques. Ajuste para consistir os campos banco, agência, Conta Corrente e cheque em branco caso o movimento seja de vendas. Anteriormente consistia para ambos tipos de movimentos |
| **Conversores e Parâmetros:** | Não se aplica |
| **Chamados relacionados:** | Não se aplica |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *11.82.41* |
