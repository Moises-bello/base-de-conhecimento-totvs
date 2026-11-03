---
content_hash: 651439746d071a6aa1ad6fa113564862c5811ea6a8ca472055558abc4debb8b1
fetched_at: '2026-06-29T00:06:07.008995+00:00'
page_id: '201734239'
product: rm
source: tdn-rm
title: TSQOWF_DT_Importação_Arquivos_Totvs_Colaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201734239
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Importação de Arquivos Totvs Colaboração |
| **Situação/Requisito:** | A importação de arquivos do Totvs Colaboração não pode ser executada porque existe um Job em andamento para o mesmo processo, porém não é dada nenhuma mensagem descrevendo o problema. |
| **Solução/Implementação:** | Melhoria no processo de importação de arquivos do Totvs Colaboração para verificar se existe algum Job em execução e caso existir, irá gerar uma consistência no Log de processamento. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 12.1.7 |
