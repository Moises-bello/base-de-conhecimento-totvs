---
article_id: 360037836754
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 72a267089bbfad049297654e59e45cffe4fbb744b4825a977daa8077e6a3226a
fetched_at: '2026-06-28T22:45:21.159884+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Funcionalidades - O tipo de evento informado
  não é aceito para este tipo de lote/serviço
type: support-article
updated_at: '2026-06-26T11:47:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037836754-RH-Linha-Protheus-TAF-eSocial-Funcionalidades-O-tipo-de-evento-informado-n%C3%A3o-%C3%A9-aceito-para-este-tipo-de-lote-servi%C3%A7o
---

**Dúvida**Ao transmitir o evento para o e-Social, é apresentado a mensagem: "O tipo de evento informado não é aceito para este tipo de lote/serviço".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - FUNCIONALIDADE - Todas as versões  
**Solução**O motivo da mensagem apresentada ao enviar qualquer evento para o e-Social, é devido a não geração do valor XMLID na tabela do evento, ou seja, esse identificador do XML serve para o governo conseguir validar o registro.   
  
A falta dessa informação, ocorre o erro citado.  
1 - Acesse o Painel eSocial (monitor) do TAF, localize os eventos que estão apresentando a inconsistência, e retransmita ao e-Social;

**Obs.:** A retransmissão do evento para o governo, automaticamente o campo XMLID deverá ser preenchido.

2 - Caso não tenha êxito em retransmitir e continuar com o mesmo problema, acesse a rotina do evento no TAF e exclua o registro do sistema;

[TAF - FUNCIONALIDADES - Como excluir eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035475634)

3 - Acesse seu ERP de Origem (GPE, RM, Datasul), integre novamente o evento para o TAF, e transmita ao governo.
