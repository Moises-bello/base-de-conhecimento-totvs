---
article_id: 4402868119959
category: RH - Rescisão
content_hash: 589583dc024f6a535eef74d4169a01ee715e0f5b5b63594526c9a6b71e2d9d3d
fetched_at: '2026-06-28T22:43:48.609302+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular rescisão pedido de demissão durante
  período gozo de Férias
type: support-article
updated_at: '2025-06-12T12:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402868119959-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-pedido-de-demiss%C3%A3o-durante-per%C3%ADodo-gozo-de-F%C3%A9rias
---

**Dúvida**Como calcular rescisão pedido de demissão durante período gozo de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Ao calcular a rescisão o sistema busca da rotina Ausência quanto a situação de afastamento do colaborador, deste modo é necessário editar o período de ausência para calcular a rescisão.  
 **Exemplo:**Férias de 01/04/2019 a 20/04/2019, sendo que houve pedido de demissão em 10/04/2019. Neste caso é necessário atualizar o afastamento férias com término em 09/04/2019 para calcular a rescisão em 10/04/2019.  
  
**Lançamento ausência período férias:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402868076823/mceclip0.png)

**Edição período férias:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402868082711/mceclip1.png)

Após edição período férias, deve ser integrado roteiro FER através da rotina do cálculo da rescisão, clicando no botão outras ações / Integrações. Desta forma será integrado somente este funcionário e calcular rescisão com data de 10.04.2019. 

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402882574871/mceclip2.png)

**Saiba mais:**Para adquirir mais conhecimento acesse o(s) link(s) abaixo:  
[MP - GPE - Cálculo de rescisão após retorno de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047533313-MP-GPE-C%C3%A1lculo-de-rescis%C3%A3o-ap%C3%B3s-retorno-de-f%C3%A9rias?source=search)
