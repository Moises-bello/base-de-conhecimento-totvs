---
content_hash: 9cc5f61afbf2ecf68c8f0636c4cec8c985e704960d6a92e709ba0c06c5d05134
fetched_at: '2026-06-29T00:06:03.685030+00:00'
page_id: '200901951'
product: rm
source: tdn-rm
title: TSQMUU_DT_Faturamento_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/TSQMUU_DT_Faturamento_Contrato
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Faturamento de Contrato |
| **Situação/Requisito:** | Ao faturar um contrato que possui item de contrato com quantidade de faturamento superior a um, o sistema gera apenas um movimento. |
| **Solução/Implementação:** | Foi realizado uma melhoria no sistema para gerar a quantidade de movimentos de acordo com a parametrização do contrato. O dia de faturamento, que era levado para o Lote, só irá ser utilizado quando a parametrização estiver definida para utilizar vencimento em dias fixos ou para contratos não periódicos. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 12.1.7 |
