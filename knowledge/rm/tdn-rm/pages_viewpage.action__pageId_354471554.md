---
content_hash: 80cb7b472459b6773658b8e5575980ab6268712a68db30c00a3c7f297b3e45c8
fetched_at: '2026-06-29T00:08:57.729785+00:00'
page_id: '354471554'
product: rm
source: tdn-rm
title: 2559329 CONTROLADORIA01-1276 DT Relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354471554
version: 1
---

# Filtro coligada

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Contábil. |
| **Função:** | Filtro coligada. |
| **Situação/Requisito:** | Mensagem  "conversão especificada não é válida" ao ser selecionado o filtro de coligadas na emissão do relatório. |
| **Solução/Implementação:** | Manutenção na função responsavel por criar um treeNode com os registros de uma tabela e adiciona-lo como filho do parametro 'parent' referente a conversão do tipo short que não foi corretamente interpretado pelo oracle em int16. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
