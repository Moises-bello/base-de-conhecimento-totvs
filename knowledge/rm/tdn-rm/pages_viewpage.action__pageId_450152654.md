---
content_hash: a9b1cd396f877ca9a61f7772761b770bc6872cfe284f6a36a67c772aa33d639c
fetched_at: '2026-06-29T00:09:55.803256+00:00'
page_id: '450152654'
product: rm
source: tdn-rm
title: 4540889 FINANCEIRO01-10295 Cálculo Valor Líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152654
version: 1
---

# Cálculo Valor Líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Cálculo Valor Líquido. |
| **Situação/Requisito:** | Ao vincular um lançamento tipo de documento sem classificação a dois lançamento de vínculos diferentes (ex: devolução e nota credito) e em seguida emitir um cheque parcial para o lançamento, o cálculo do valor líquido está apresentando valor inconsistente. |
| **Solução/Implementação:** | Ajustado calculado do valor vinculado, quando existe vínculos diferentes (ex: devolução e nota credito vinculados a um mesmo lançamento ) e depois emitimos um cheque parcial para o lançamento. Agora, caso o valor líquido seja calculado novamente, após a emissão de cheque, o valor do vinculo passa a ser considerado ou não, por tipo de vinculo. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [4540889](https://totvssuporte.zendesk.com/agent/tickets/4540889 "Open ticket in Zendesk Support") |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
