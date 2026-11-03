---
content_hash: c27d4dbc17c1cb23bfd48192436f2fe3ffb8084215c1c126717fd92f7c664c8f
fetched_at: '2026-06-29T00:09:54.396580+00:00'
page_id: '444615698'
product: rm
source: tdn-rm
title: 4536663 FISCAL01-7382 DT - Escrituração Fiscal - Divergência de valores ao
  escriturar redução Z via escrituração .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444615698
version: 2
---

# Escrituração Fiscal - Redução Z

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos Fiscais |
| **Situação/Requisito:** | Ao escriturar redução Z "Valor Total" fica divergente do "Valor Total da Situação Tributária" dentro do lançamento fiscal gerado em 30 centavos.  Isso se deve ao fato de que o campo "Valor Mercadoria" se encontra com o valor maior que o valor bruto calculado para os cupons da TRIBUTACAOECF existente nos totalizadores da redução Z. |
| **Solução/Implementação:** | No processo de escrituração de cupom fiscal, os valores serão arredondados ou truncados conforme parametrização definida no cadastro de Ponto de Venda.  Obs: O valor de 30 centavos de diferença era porque o processo estava olhando a parametrização geral de Arredonda ou Trunca do gestão de compras, estoque e Faturamento. |
