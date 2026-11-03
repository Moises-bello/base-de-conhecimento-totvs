---
content_hash: 54a5032003447ebb59174bc5642652db92725df32ff1e163d7acd9a331851876
fetched_at: '2026-06-29T00:06:26.652726+00:00'
page_id: '226525876'
product: rm
source: tdn-rm
title: TUHJAO_DT_Validação_Bolsa_Aluno_por_Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=226525876
version: 114
---

# GERAR CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Incluir Bolsa do Aluno |
| **Situação/Requisito:** | Ao inserir uma bolsa no contrato do aluno, apresentava mensagem: "O valor total de descontos entre as bolsas deve ser menor que o valor das parcelas em todo o intervalo". Ocorria somente quando estava marcado o parâmetro Educacional/Integração/Financeiro - o campo "Aplicação da bolsa" igual a "Contrato" E a parcela do contrato estivesse marcado o campo "Valor calculado pelo número de créditos". |
| **Solução/Implementação:** | Alterado validação da inclusão de bolsa, para conferir se a somatória do percentual de bolsas não ultrapassa 100%, quando marcado parâmetro Educacional/Integração/Financeiro - o campo "Aplicação da bolsa" igual a "Contrato". |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
