---
content_hash: 8bdf27f24caf7e6bef03b84cb50aad53db347c5e8402833381d5c5fe21da8e31
fetched_at: '2026-06-29T00:10:13.763360+00:00'
page_id: '458756476'
product: rm
source: tdn-rm
title: 5034846 FINANCEIRO01-10904 DT Baixa de Crédito de Adiantamento associado a
  Lançamentos Vinculados em Moeda Estrangeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458756476
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao executar a baixa de uma lista de lançamentos em US$, associados a um crédito de adiantamento em R$, ocorreu mensagem indicando que estava ocorrendo uma tentativa de baixar um valor acima do valor líquido do lançamento. |
| **Solução/Implementação:** | Constatou-se que o problema se devia a uma diferença da ordem de R$ 0,0005 (cinco centésimos de centavo). Adotamos como regra para validação que qualquer diferença menor que 1 centavo deve ser considerado como valores idênticos, pois se trata de menor que a menor porção monetária possível. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 5034846 |
| **Requisito:** | FIN000040 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | 12.1.20, 12.1.23, 12.1.24 |
