---
content_hash: 306e9b2f1e1fa34ae19ae3d4b932472175e49d5e01ac9bd32c9a02e1355106a1
fetched_at: '2026-06-29T00:09:00.843333+00:00'
page_id: '369628131'
product: rm
source: tdn-rm
title: 3055575 FINANCEIRO01-7399 DT Inclusão de cliente/fornecedor via protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=369628131
version: 1
---

# Erro ao salvar cliente/fornecedor através de integração com protheus

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de Cliente/Fornecedor |
| **Situação/Requisito:** | Ao realizar a inclusão de um cliente/fornecedor via Protheus o sistema apresenta a mensagem de erro: "Value was either too large or too small for an Int16." |
| **Solução/Implementação:** | Tratamento realizado no source code para transformar o branchid enviado em valor de filial do RM e salvá-lo no campo FCFO.CODFILIALINTEGRACAO |
| **Tickets relacionados:** | 3055575 |
| **Requisito:** | FIN000060 |
