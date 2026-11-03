---
content_hash: c55bd902bd21dc0aefb80c893edfef829199fe257a1f7f0dcb8e0ab1df783b09
fetched_at: '2026-06-29T00:05:58.353733+00:00'
page_id: '185753077'
product: rm
source: tdn-rm
title: Como Fazer - Envio de e-mail pelo Gerador de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185753077
version: 1
---

|  |  |  |
| --- | --- | --- |
| Produto | : | RM Gerador de Relatórios |
| Versão RM | : | Qualquer Versão |
| Banco de Dados | : | Qualquer Versão |
| Processo | : | Execução de agendamento de envio de e-mail via Gerador de Relatórios |
| Sub Processo | : | FAQ |
| Data da Publicação | : | 06/04/2015 |

***Sintoma***

Envio de email referente a algum processo do sistema apresentando erro.

***Causas***

* Parametrização de envio de email incorreta;
* Servidor de email com problema ou fora do ar;
* Relatório utilizado para envio inconsistente.

***Solução***

Acesse o menu Relatórios -> Gerador

Identifique e selecione o relatório utilizado em envio de email e clique em editar.

Será exibida a tela abaixo, nela marque a opção “Executa em Job Server” e  clique em OK

 Selecione novamente o relatório utilizado em assistente e clique no botão “Agendar a execução do relatório”

Clique em avançar e na tela seguinte marque a opção “Enviar o Relatório gerado por e-mail” e informe seu e-mail no espaço em branco conforme tela abaixo e clique em avançar

Clique em avançar novamente e logo depois clique em executar

O processo será executado e o e-mail será encaminhado ao destinatário escolhido.
