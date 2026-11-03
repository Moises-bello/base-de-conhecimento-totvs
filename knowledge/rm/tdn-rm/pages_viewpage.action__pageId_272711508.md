---
content_hash: 7233f9f2f4a72a4082837990a64089c270c7eb1267e4043bbf1d2c98e786e570
fetched_at: '2026-06-29T00:08:31.012057+00:00'
page_id: '272711508'
product: rm
source: tdn-rm
title: 545939 MRH-8574 Envio de Relatório por E-mail para Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272711508
version: 116
---

# ENVIO DE E-MAIL PARA FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Envio de E-mail para Funcionários |
| **Situação/Requisito:** | Ao executar o processo de envio de e-mail para funcionários com uma grande quantidade de funcionários selecionada, o processo retorna timeout para alguns casos e o e-mail não é enviado |
| **Solução/Implementação:** | Foi feito um tratamento no processo de envio para que a conexão seja aberta para cada e-mail, e finalizada ao ser enviado, evitando o timeout. |
| **Tickets relacionados:** | 545939 |

divs
