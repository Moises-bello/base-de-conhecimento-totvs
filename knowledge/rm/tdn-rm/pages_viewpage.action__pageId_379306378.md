---
content_hash: 9cd070f963d3e6701b8536f426da61be5ab531d13dad53c6223ece3b21a93027
fetched_at: '2026-06-29T00:09:02.377970+00:00'
page_id: '379306378'
product: rm
source: tdn-rm
title: 1893002 CONTROLADORIA01-1663 Cadastro de Cliente / Fornecedor - campo "Dias
  em Atraso"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379306378
version: 2
---

# Cadastro de Cliente / Fornecedor - campo "Dias em Atraso"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Cadastro de Cliente / Fornecedor |
| **Situação/Requisito:** | Ao informar o valor de "50000000" no campo de "Dias de Atraso" no Cliente/Fornecedor e incluir um lançamento para este mesmo Cliente/Fornecedor é apresentada mensagem:  Arithmetic overflow: converting expression to data type datetime. |
| **Solução/Implementação:** | Ajuste na tela de cadastro de Cli/For para que o campo "Dias de Atraso" não aceite mais de 6 dígitos pois o valor máximo em dias de vencimento que o banco de dados aceita é 999999. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1893002 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
