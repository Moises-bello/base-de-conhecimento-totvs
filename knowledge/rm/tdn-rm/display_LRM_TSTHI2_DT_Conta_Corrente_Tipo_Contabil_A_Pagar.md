---
content_hash: c3d5d69ac6bd480b8f66c32e9b5249c0177122dfd22f435dd3316079c43fa666
fetched_at: '2026-06-29T00:06:24.147607+00:00'
page_id: '224113569'
product: rm
source: tdn-rm
title: TSTHI2_DT_Conta_Corrente_Tipo_Contabil_A_Pagar
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTHI2_DT_Conta_Corrente_Tipo_Contabil_A_Pagar
version: 122
---

# GERAR CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | *Aproveitar valores em conta corrente* |
| **Situação/Requisito:** | No aproveitamento de conta corrente, ao gerar lançamento A Pagar, identificar qual tipo contábil será gravado quando parametrizado para buscar tipo contábil no Serviço. |
| **Solução/Implementação:** | No processo de "Aproveitar valores em conta corrente", quando natureza da conta corrente é um Crédito e estiver configurado para buscar o Tipo Contábil do Serviço, o sistema irá observar o parâmetro do Fluxus "Contas a Pagar | Contab. Inclusão | Default Contábil no lançamento".     Obs.: Como o lançamento gerado será do tipo "A Pagar", não temos um serviço para observar o tipo contábil, portanto se faz necessário fixar o default do Financeiro.. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *12.1.10; 11.82.43* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
