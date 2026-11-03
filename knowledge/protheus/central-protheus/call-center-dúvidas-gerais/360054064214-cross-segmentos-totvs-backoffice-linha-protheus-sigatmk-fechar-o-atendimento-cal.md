---
article_id: 360054064214
category: Call Center - Dúvidas Gerais
content_hash: e90f0c51bcd7041281dec3a8df52b45cee720d5e008702f6df01549f4594ba43
fetched_at: '2026-06-28T22:41:26.983065+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK -Fechar o atendimento
  Call Center após confirmar a ligação
type: support-article
updated_at: '2022-12-23T18:53:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054064214-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Fechar-o-atendimento-Call-Center-ap%C3%B3s-confirmar-a-liga%C3%A7%C3%A3o
---

**Dúvida**Como fechar fechar a tela do atendimento ao confirmar o sucesso na ligação pelo atendimento na Agenda do Operador?  
  
**Ambiente**Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK – A partir da versão 11.80  
  
**Solução**Trata-se de um conceito da rotina, antes de abrir a tela com o atendimento de tele cobrança, pela **Agenda do Operador** (**TMKA380**), o sistema solicita confirmação do operador quanto ao sucesso no contato com o cliente.

Uma vez que ele confirma que conseguiu realizar o contato, é necessário realizar o **registro** **do contato**, caso os títulos permaneçam em aberto, é necessário indicar uma nova **data** (**ACF\_PENDEN**) e/ou um novo **horário** (**ACF\_HRPEND**) para retorno do contato.

Preenchendo as informações de data e horário de retorno, o sistema permitirá que o Operador saia do atendimento.  
  
OBS: Os campos (**ACF\_PENDEN**) e (**ACF\_HRPEND**) são campos obrigatórios da rotina , não sendo possível desabilitar os mesmos.
