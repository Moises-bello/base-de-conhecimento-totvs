---
content_hash: a9798d23d8b146316c393e1f8d49d640343dcff59e305bd568e1902cf1afb8ce
fetched_at: '2026-06-29T00:09:45.399696+00:00'
page_id: '433241472'
product: rm
source: tdn-rm
title: 4146205 FISCAL01-6938 DT - SPED Fiscal G125 com valores negativos
type: documentation
url: https://tdn.totvs.com/display/LRM/4146205+FISCAL01-6938+DT+-+SPED+Fiscal+G125+com+valores+negativos
version: 7
---

# SPED FISCAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | SPED Fiscal |
| **Situação/Requisito:** | Na geração do SPED FISCAL o G125 está sendo gerado com valores negativos. |
| **Solução/Implementação:** | * Foi modificado a inclusão do Lançamento Fiscal através da escrituração para não incluir registro na DATIVO quando o lançamento estiver cancelado. * Foi modificado o cancelamento do Lançamento Fiscal para excluir o registro na tabela DATIVO. * Foi modificado a geração do Registro G125 do SPED Fiscal para ser gerado até o mês de saída do bem. |
