---
content_hash: 1329d6810d3facf176f88dfa717e8e5cc0f2cc136e0be4c7ab79dca1eeccfa49
fetched_at: '2026-06-29T00:08:59.598023+00:00'
page_id: '364908446'
product: rm
source: tdn-rm
title: S-2206 - Alteração de Contrato de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908446
version: 14
---

* Este evento registra as alterações do contrato de trabalho, tais como: remuneração e periodicidade de pagamento, duração do contrato, local, cargo ou função, jornada, entre outros.
* Deve ser transmitido até o dia 07 (sete) do mês subsequente ao da competência informada no evento ou até o envio dos eventos mensais de folha de pagamento da competência em que ocorreu a alteração contra

1º Passo:Quando o usuário realizar qualquer alteração no cadastro do funcionário será  gerado gatilho na Fila de eventos para o evento S-2206 com status 0-Pendente.

O Usuário poderá visualizá-lo através do  menu eSocial | Eventos de tabelas/ Não Periódicos.

2º Passo: Gerar XML:

Deverá  executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3º Passo-Integrar evento com o TAF .

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado para o TAF.

4º Passo: Enviar os eventos gerados na fila para o TOTVS Automação  Fiscal (TAF):

5º Passo: Atualizar status da integração TAF:

Para atualizar o status da integração do TAF Terá as seguintes opções:

Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados:
