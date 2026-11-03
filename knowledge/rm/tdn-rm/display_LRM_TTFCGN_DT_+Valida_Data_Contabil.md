---
content_hash: e20c254e67b99cfcb5898af7d5b5d248cf4263225583e4e6b01c04cd7b834c1d
fetched_at: '2026-06-29T00:06:07.966184+00:00'
page_id: '201741573'
product: rm
source: tdn-rm
title: TTFCGN_DT_ Valida_Data_Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFCGN_DT_+Valida_Data_Contabil
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
| **Versões/Release:** | *12\_1\_8* |
