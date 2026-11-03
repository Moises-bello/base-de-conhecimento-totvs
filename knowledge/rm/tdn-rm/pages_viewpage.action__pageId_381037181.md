---
content_hash: c3dd26be1654a13066c35c6ae3c6f5ba1dccb8bccd1d59ef0d7cabc8c27bc91d
fetched_at: '2026-06-29T00:09:03.000427+00:00'
page_id: '381037181'
product: rm
source: tdn-rm
title: CONTROLADORIA01-1736 DT Lookup do CEI do Cliente / Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381037181
version: 5
---

# Lookp do CEI do Cliente / Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Lookup do CEI do Cliente / Fornecedor |
| **Situação/Requisito:** | Na inclusão do Lançamento Fiscal no preenchimento do campo “Identificador CEI do Cliente Fornecedor”, se tenho que incluir um novo registro através do Lookup ocorre mensagem: Referência de Objeto não encontrada. |
| **Solução/Implementação:** | Ajuste na tela de cadastro do lookup do campo “Identificador CEI do Cliente Fornecedor” para que ao incluir um novo registro não apresente mensagem de exceção.  Obs.: O LookUp do CEI do Cliente/Fornecedor é tratado no financeiro como anexo, onde precisa do CODCFO passado pelo MasterBindingSource. Já no LookUp não contem essa informação para realizar a inclusão do registro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
