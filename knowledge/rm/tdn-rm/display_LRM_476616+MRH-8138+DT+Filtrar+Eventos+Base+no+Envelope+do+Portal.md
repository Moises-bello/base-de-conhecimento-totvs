---
content_hash: bd974d18f18f32fc376048373d9d07dd84f3894f1adb9be7afdc0788e929f300
fetched_at: '2026-06-29T00:08:30.371805+00:00'
page_id: '272427229'
product: rm
source: tdn-rm
title: 476616 MRH-8138 DT Filtrar Eventos Base no Envelope do Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/476616+MRH-8138+DT+Filtrar+Eventos+Base+no+Envelope+do+Portal
version: 106
---

# ENVELOPE DE PAGAMENTO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Envelope de Pagamento Portal |
| **Situação/Requisito:** | O cliente deseja que os eventos do tipo Base não fossem exibidos no envelope de pagamento do Portal nos diversos tipos de relatórios. |
| **Solução/Implementação:** | Para filtrar os eventos a serem exibidos no envelope, basta seguir os seguintes passos:   * Edite os eventos que deseja ocultar e no campo "Chave", informe um valor. Esse valor pode variar de 0 a 5 e deve ser o mesmo para todos os eventos que deseja ocultar.      * Em seguida, edite os parâmetros da Folha Normal, na aba de Ficha Financeira, selecione as chaves ativas. A chave dos eventos que você deseja ocultar deve ficar desmarcada. Por exemplo: defini a chave 5 para os meus eventos do tipo Base, então deixo a chave 5 desmarcada (inativa).      * E por fim, edite os parâmetros do demonstrativo de pagamento do Portal e marque o parâmetro de "Usar Chaves Ativas para filtrar eventos do envelope".      * Dessa forma apenas os eventos das chaves ativas serão exibidos no envelope de pagamento. |
| **Tickets relacionados:** | 476616 |

divs
