---
content_hash: 1ec653cc18ea227519d5734ac6267d1444abe9ed77531ea266cdec18e6f7bfad
fetched_at: '2026-06-29T00:09:42.616255+00:00'
page_id: '431680249'
product: rm
source: tdn-rm
title: 4038367 FISCAL01-6878 DT - EFD Contribuições - Geração de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431680249
version: 1
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Saída |
| **Situação/Requisito:** | Erro ao gerar o arquivo do EFD Contribuições:  [12:49:30] ======================================================  [12:49:30] Ocorreu um erro inesperado na geração.  [12:49:30]  [12:49:30] System.Data.InvalidConstraintException  [12:49:30] Erro: As colunas pai e filho não têm colunas de tipo correspondente. |
| **Solução/Implementação:** | Foi realizada uma correção no script(select), para as bases Oracle, onde agora a coluna *IDTIPOAPLFIN* é tipada em *number*. |
