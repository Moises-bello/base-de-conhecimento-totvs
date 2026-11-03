---
content_hash: 881f67db01635c7b104360e4b8233f36af9c3e70e264dc5c147f1a25b72e11df
fetched_at: '2026-06-29T00:08:06.055333+00:00'
page_id: '236431355'
product: rm
source: tdn-rm
title: TULNWK_DT_Inserir_Bolsa_Retroativa_Data_Contabilização_Conciliar_Extrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236431355
version: 118
---

# INCLUSÃO/EXCLUSÃO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | Inclusão/Exclusão de bolsa retroativa |
| **Situação/Requisito:** | Ao incluir bolsa retroativa em um lançamento já baixado, a data de contabilização foi alterada incorretamente para data atual e deveria ser data da baixa. Somente ocorre quando está marcado o  parâmetro Educacional Integração Financeiro | "Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa" e o parâmetro Fluxus Contab. Baixa Receber  - "Data default de Baixa a Receber", está marcado como "Baixa". |
| **Solução/Implementação:** | Criado novo parâmetro Educacional | Integração Financeiro | "Data de contabilização de baixa igual ao Padrão RM Fluxus, ao reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa ".     Caso parâmetro esteja marcado, no processo de inclusão/exclusão de bolsa retroativa  a data de contabilização gravada obedecerá ao parâmetro  Fluxus Contab. Baixa Receber  - "Data default de Baixa a Receber", no caso em que estiver também marcado o parâmetro Educacional "Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa".     As opções possíveis para data de contabilização são: Sistema, Baixa, Vencimento, Emissão, Previsão de Baixa, Cheque, Inclusão, Data remessa, Remessa Raydan, Comp.cheque.     Caso parâmetro esteja desmarcado, continua o comportamento atual que é gravar a data de contabilização igual à data atual. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
