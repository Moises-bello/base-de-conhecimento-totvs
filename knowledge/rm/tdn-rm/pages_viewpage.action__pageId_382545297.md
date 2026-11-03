---
content_hash: 898cf6a150dec3fa49be82d83893d38119ba4497d4204386a01caad313e680a7
fetched_at: '2026-06-29T00:09:04.051865+00:00'
page_id: '382545297'
product: rm
source: tdn-rm
title: Como atualizar o Status de Integração com o TAF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382545297
version: 3
---

Este processo consulta o status atual do evento no TAF e atualiza a informação na [Fila de Eventos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.FilaEventos.aspx).

**Observações:**

* A Quebra de Seção e Seleção de funcionários na tela principal e nos parâmetros específicos da coligada, apenas serão habilitados caso seja marcado algum evento que relacione funcionários ou [Eventos Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosPeriodicos.aspx).
* O Período de Apuração será obrigatório caso selecione algum dos [Eventos Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosPeriodicos.aspx).
* Para a atualização do status de uma grande quantidade de registros, não é recomendável utilizar a Fila de Eventos, deverá utilizar o processo "Atualizar Status Integração TAF" que encontra-se disponível no menu  "eSocial".
* Criado o parâmetro "Realizar consulta do status por tafKey" a partir das versões:
  + 12.1.26.124
  + 12.1.25.179
  + 12.1.24.241

Com o parâmetro desmarcado o sistema faz a consulta padrão no TAF por tafTicket;   
Com o parâmetro marcado o sistema faz a consulta no TAF individualmente por tafKey.

Para executar o processo o usuário deve acessar o menu "Atualiza Status Integração TAF" disponível na aba eSocial:
