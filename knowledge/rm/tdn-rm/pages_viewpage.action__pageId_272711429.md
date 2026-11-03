---
content_hash: eac64b8cc6811c53d33b63c5481968555da6b4b25f599ab40996d52fd21e1cdf
fetched_at: '2026-06-29T00:08:31.004640+00:00'
page_id: '272711429'
product: rm
source: tdn-rm
title: 487269 MRH-8706 Exclusão de Funcionário Integração SigaMNT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272711429
version: 113
---

# EXCLUSÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Exclusão de Funcionários |
| **Situação/Requisito:** | Ao exlcuir um funcionário em uma base integrada com o SigaMNT, estava sendo disparada uma mensagem única mesmo com a fórmula visual desabilitada. Nessa integração, a mensagem deve ser disparada apenas pela fórmula visual. |
| **Solução/Implementação:** | Adicionado um tratamento para verificar a integração com o SigaMNT antes de gerar a mensagem de exclusão do funcionário |
| **Tickets relacionados:** | 487269 |

divs
