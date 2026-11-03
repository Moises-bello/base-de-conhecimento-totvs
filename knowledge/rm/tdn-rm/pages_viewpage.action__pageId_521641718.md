---
content_hash: 61882eb6fe1135b0bed17f7603d4311076d71f13fedd4c1a7912637a7b059a5f
fetched_at: '2026-06-29T00:10:31.659530+00:00'
page_id: '521641718'
product: rm
source: tdn-rm
title: DEDUMOBILE 2609 - DT No Menu Agendamento/ envio de mensagens está convertendo
  mensagem HTML em Texto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521641718
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Totvs Gestão Educacional |
| Módulo: | Central de Comunicações |
| Função: | Agendamento/Envio de Mensagens |
| Ticket: | [7560544](https://totvssuporte.zendesk.com/agent/tickets/7560544 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2609](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2609) |

## **02. SITUAÇÃO/REQUISITO**

No Cadastro da Mensagem, foi utilizada a opção “HTML”, porém, ao acessar o menu "Agendamento/envio de mensagens" e selecionar a mensagem pré-configurada, esta vem com a opção "Texto" marcada e com o conteúdo desformatado (convertido).  
Ao tentar alterar a seleção de Texto para HTML, apresenta mensagem que o texto será apagado.

## **03. SOLUÇÃO**

Otimizado o processo para que, ao alterar o tipo de formatação do texto configurado na mensagem por email, não seja refletido na formatação do tipo da mensagem a ser enviado através do eduCONNECT.
