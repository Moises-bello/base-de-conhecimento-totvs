---
content_hash: 9ab5ad2b24e15fdb0e1edc83b3fc8719892cd22f5710080d047c0f9ac4ff997a
fetched_at: '2026-06-29T00:06:10.318725+00:00'
page_id: '203760921'
product: rm
source: tdn-rm
title: TSZBBM_DataServer_RhuPlanoTreinData
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZBBM_DataServer_RhuPlanoTreinData
version: 1
---

# DATASERVER RHUPLANOTREINDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | DataServer RhuPlanoTreinData |
| **Situação/Requisito:** | Ao tentar realizar a leitura do DataServer, RhuPlanoTreinData pelo SOAP UI é retornada a seguinte mensagem:  "Ocorreu um erro ao efetuar a leitura da visão: Index was outside the bounds of the array." |
| **Solução/Implementação:** | Alterado a forma de recuperar os dados do DataServer e foi adicionada validação que verifica se há dados a ser recuperado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSZBBM |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |
