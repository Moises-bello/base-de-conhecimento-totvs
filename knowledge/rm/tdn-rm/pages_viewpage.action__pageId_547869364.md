---
content_hash: 3ce989cbec291b29fd6725e8b5131bc3d4228c8a1f8effab266fa62dc2aae6f7
fetched_at: '2026-06-29T00:10:42.891330+00:00'
page_id: '547869364'
product: rm
source: tdn-rm
title: DEDUMOBILE-2859 DT Erro ao enviar mensagem se usuário não tiver e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547869364
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Meu eduCONNECT |
| Função: | Mensagens pessoais |
| Ticket: | 8291059 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUMOBILE-2859 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar uma mensagem para o educonnect sem enviar também e-mail no processo de agendamento/envio de mensagens, a mensagem é enviada normalmente para quem não tem e-mail cadastrado.  
Porém, se mandarmos um e-mail junto com a mensagem para esse mesmo destinatário (sem e-mail cadastrado), o processo não envia o e-mail (obviamente) mas também não envia a mensagem.  
No nosso entendimento uma coisa não deveria anular a outra. Se o destinatário não tem e-mail, ele não irá recebê-lo mas deveria receber a mensagem no App, já que usuário ele tem.

## **03. SOLUÇÃO**

Otimizado a rotina para que seja possível enviar mensagens (Parametrizada para o envio simultâneo "Email" e "eduCONNECT") quando o destinatário não possui email cadastrado.
