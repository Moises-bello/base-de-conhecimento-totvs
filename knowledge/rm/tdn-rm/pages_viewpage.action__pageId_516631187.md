---
content_hash: 6eea5f198f1730363d1349ffa05dfe67826bc2b1a467304740330e169fd19e72
fetched_at: '2026-06-29T00:10:27.680764+00:00'
page_id: '516631187'
product: rm
source: tdn-rm
title: DEDUMOBILE-2329 DT Mensagem de "tamanho máximo 4000 caracteres excedido" sendo
  exibida indevidamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516631187
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Totvs Gestão Educaiconal |
| Função: | Agendamento Envio de Mensagens |
| Ticket: | [6608971](https://totvssuporte.zendesk.com/agent/tickets/6608971 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2329](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2329) |

## **02. SITUAÇÃO/REQUISITO**

No processo de agendamento, se o usuário marcar a opção enviar email (no corpo do texto informar inserir imagens) e enviar mensagem para o eduCONNECT com o Tipo: HTML, o sistema está validando a quantidade de caracteres no "Texto" do email, não permitindo que a mensagem seja enviada para os destinatários. 

## **03. SOLUÇÃO**

Otimizado o processo de envio de notificação do eduCONNECT, onde estava validando a quantidade de caracteres informado no texto de email ao invés do texto do aplicativo.
