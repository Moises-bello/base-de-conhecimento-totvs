---
content_hash: b3797f54c3684b68174b32e60b5b80335b7605440ef99886c6766b139e4b64c7
fetched_at: '2026-06-29T00:08:44.455990+00:00'
page_id: '307854311'
product: rm
source: tdn-rm
title: 1226411 FINANCEIRO01-2234 Integração CheckOut Débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307854311
version: 97
---

# CheckOut Pagamento com Débito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Pagamento com Débito Portal CheckOut |
| **Situação/Requisito:** | Ao realizar pagamento no portal com a forma de pagamento débito o sistema não baixava o lançamento automaticamente. |
| **Solução/Implementação:** | Melhoria no processo de integracao com o checkout cielo.  Inclusão do tratamento do status pendente, pois no pagamento com cartão de debito é enviado primeiro uma notificação com status pendente.  Retirada do parâmetro codcoligada dos metodos ConsisteTransacaoCheckoutNotificacao e ConsisteTransacaoCheckoutStatus, pois não existe no context de pagina anominas (publicas).  Nas paginas de Notificação e MudancaStatus adicionado todos os status tratados em ambas as paginas  Alterado o método GetIdTransacaoByIdOrigem |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000296 |

divs
