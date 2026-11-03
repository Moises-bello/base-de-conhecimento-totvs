---
content_hash: 71e1e1454cd0790f6ec53240ad5c6ad6bb55230916447f41e52c63efd58c2743
fetched_at: '2026-06-29T00:06:07.944816+00:00'
page_id: '201741138'
product: rm
source: tdn-rm
title: TTEYRT_DT_ Valida_Data_Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEYRT_DT_+Valida_Data_Contabil
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Contrato Financeiro |
| **Situação/Requisito:** | No cadastro de Contrato financeiro, quando utiliza contabilização por competência, ao digitar data de contrato com dia 31 e a competência contábil inicial é 06/2015, o sistema emite incorretamente a mensagem “Os parâmetros Year, Month, Day descrevem um DataTime não representável”. |
| **Solução/Implementação:** | Alterada a validação da data do contrato financeiro, quando utiliza contabilização por competência, para que a mesma esteja compreendida dentro da competência contábil. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **Versões/Release:** | *12\_1\_7* |
