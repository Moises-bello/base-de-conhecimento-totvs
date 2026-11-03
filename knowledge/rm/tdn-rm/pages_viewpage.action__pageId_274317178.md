---
content_hash: f1bccf638ee611d53443f22187ee5e0e2ab0441df8b62d072010e00c9efcdb68
fetched_at: '2026-06-29T00:08:33.432773+00:00'
page_id: '274317178'
product: rm
source: tdn-rm
title: 335565 CONTROLADORIA01-47 DT Alteração Conta Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274317178
version: 106
---

# Alteração Código Conta Contábil Global

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | Alteração do código de contas contábeis |
| **Situação/Requisito:** | Ao realizar a alteração do código da conta contábil é apresentada uma mensagem de chave duplicada. |
| **Solução/Implementação:** | O processo de alteração do código de contas contábeis estava gravando, para contas globais, a coligada corrente. Foi necessário alterá-lo para que o campo CODCOLIGADA, da tabela CHISTTROCACODCONTA, armazene o valor zero (código da coligada global) quando a conta é global. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
