---
content_hash: c8f71367f7c20aa00ed07c6b6f07584c6c79c95339c83d19c391b8256e75bd73
fetched_at: '2026-06-29T00:08:57.744063+00:00'
page_id: '354473661'
product: rm
source: tdn-rm
title: 2657154 CONTROLADORIA01-1335 DT Obrigações acessórias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354473661
version: 1
---

# Gerar SPED contábil

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Contábil. |
| **Função:** | Gerar SPED contábil. |
| **Situação/Requisito:** | Mensagem  "conversão especificada não é válida" ao ser selecionado o filtro de Coligada / Filial na tela de parametrização do SPED contábil. |
| **Solução/Implementação:** | Manutenção na função responsavel por criar um treeNode com os registros de uma tabela e adiciona-lo como filho do parametro 'parent' referente a conversão do tipo short que não foi corretamente interpretado pelo oracle em int16. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
