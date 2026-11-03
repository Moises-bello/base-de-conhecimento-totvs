---
content_hash: d28d847dd1400aa89a9db184eb8a0a5609a1243007d45aa1b7295e4227bfa430
fetched_at: '2026-06-29T00:06:29.626035+00:00'
page_id: '234614463'
product: rm
source: tdn-rm
title: TTLGGK_DT_Tipo_Documento_Aproveitamento_de_Conta_Corrente_Credora
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLGGK_DT_Tipo_Documento_Aproveitamento_de_Conta_Corrente_Credora
version: 122
---

# APROVEITAMENTO DE CONTA CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Aproveitamento de conta corrente |
| **Situação/Requisito:** | No processo de aproveitamento de conta corrente, quando estiver marcado o parâmetro Educacional/Integração Financeira/ Tipo de documento por serviço, e a natureza da conta corrente for Credora, o campo "Tipo de documento" estava sendo preenchido incorretamente com o valor do  parâmetro Educacional "Tipo de documento padrão". |
| **Solução/Implementação:** | Alterado processo de aproveitamento de conta corrente, quando estiver marcado o parâmetro Educacional/Integração Financeira/ Tipo de documento por serviço, e a natureza da conta corrente for Credora, o campo "Tipo de documento" ficará sempre em branco para que o usuário possa preencher, visto que lançamento a pagar não tem serviço. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | TUNIA7 |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *11.82.43; 12.1.11* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
