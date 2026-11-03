---
content_hash: 9220538a23caf5dc176619ed3b5da550d8eaaa1ed23989f905f6afc6233e89af
fetched_at: '2026-06-29T00:06:24.665331+00:00'
page_id: '224119354'
product: rm
source: tdn-rm
title: TUCWL1_DT_Emissão_Recebimento_De_Cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224119354
version: 119
---

# Emissão /Recebimento de Cheque

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Emissão/Recebimento de Cheque |
| **Situação/Requisito:** | Ao emitir cheque para lançamento com tipo contabil "contabil" ou "baixa contabil" o formulário de cheque está apresentando o tipo contabil do extrato como "contabil", diferente do comportamento de versões anteriores e do delphi(deveria ser não contábil). |
| **Solução/Implementação:** | Alterado o comportamento da exibição do campo tipo contabil do formulário de emissão de cheque. O default do campo tipo contabil do cheque sempre será não contabil, o usuário deve escolher a opção  "Contabil" ou "A contabilizar" caso seja necessário contabilizar o extrato de lançamentos que tiverem tipo contabil "Contabil" ou "Baixa Contabil". |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000156 |
| **Versões/Release:** | 12.1.10 |
| **Versão Corrigida:** | 12.1.10 |
| **Versão Expedida:** | 12.1.10 |

divs
