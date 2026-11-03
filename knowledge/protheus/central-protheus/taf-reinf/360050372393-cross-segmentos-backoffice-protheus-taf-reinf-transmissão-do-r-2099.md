---
article_id: 360050372393
category: TAF - REINF
content_hash: ae6b6ca1b1564cced2bb60be6344ab92e746ba8c8899da4374cb75d33f6353a9
fetched_at: '2026-06-28T22:41:34.883866+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Transmissão do R-2099
type: support-article
updated_at: '2023-04-04T12:06:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050372393-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Transmiss%C3%A3o-do-R-2099
---

**Dúvida**Transmissão Evento R-2099 - Transmitido/Aguardando   
  
 **Ambiente**  
Microsiga Protheus – TAF – A partir da versão 12  
  
**Solução**Prezado cliente,

O envio do evento R-2099 não é o fechamento efetivamente. Ele é apenas uma solicitação de fechamento.

A principal função deste evento é informar a Receita, que os movimentos do período foram encerrados e a DctfWeb, pode ser gerada.

Este evento se trata de um evento Assíncrono, em resumo, isso significa que será enviado a Receita e somente após processamento das informações pela receita, ele será retornado.

Então, dependemos da agilidade do Governo para retornar as informações para dentro do TAF, isso pode demorar, temos acompanhado que no período de fechamento, esse processo, tem ocorrido alguma demora.

Podemos ter 3 tipos de retorno sobre:

##### Erro – Onde o fechamento NÃO FOI ACEITO pela RFB, logo o período se mantem ABERTO. É preciso verificar o erro, corrigir e então enviar um novo R-2099.

Tivemos um erro com o retorno da Mensagem pela Receita **MS1078 (A EFD já foi fechada para o período informado, ou existe um evento de fechamento em processamento)**, essa mensagem ocorre pois o evento foi apurado novamente antes mesmo de ter recebido o retorno da Receita.

##### **Em processament**o – Onde o fechamento ainda está em processamento, neste caso o período não estaria nem aberto nem fechado.

**Evento está sendo rejeitado com o erro 2 - EM PROCESSAMENTO.**

<ideStatus>

<cdRetorno>2</cdRetorno>

<descRetorno>EM PROCESSAMENTO</descRetorno>

</ideStatus>

Essa mensagem ocorre pois o processo na Receita se encontra em processamento e ainda não tivemos nenhum retorno, o que deve ser feito neste caso é monitorar a transmissão, não devemos apurar novamente o Evento.

***Segue posicionamento da Receita, sobre o Status EM PROCESSAMENTO:***

***<http://sped.rfb.gov.br/pagina/show/2791>***

##### **Sucesso**– Onde a RFB aceitou o fechamento do período, logo o período está fechado e seria preciso enviar o R-2098 para reabertura.

Para maiores informações sobre retorno da Receita, pode consultar essa página:

[FAQ - 0004 - Rejeições apresentadas nas Transmissão da Reinf.](https://tdn.totvs.com/pages/viewpage.action?pageId=366646855)

<https://tdn.totvs.com/pages/releaseview.action?pageId=387293198>
