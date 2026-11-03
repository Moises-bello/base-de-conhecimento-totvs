---
article_id: 360038202853
category: Call Center - Televendas
content_hash: 87ddde94794e9ae770867217931bddc5de1843696919beb2e812fe55c952c5a7
fetched_at: '2026-06-28T22:41:30.283311+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - variable is not an object
  on TK273CARGAITEM(TMKA273A.PRW)
type: support-article
updated_at: '2024-04-25T14:29:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038202853-Cross-Segmentos-Backoffice-Protheus-SIGATMK-variable-is-not-an-object-on-TK273CARGAITEM-TMKA273A-PRW
---

**Ocorrência**

Ao acessar histórico de ligações do televendas (**TMKA273**) Call Center, ocorre o erro:

**variable is not an object on TK273CARGAITEM(TMKA273A.PRW) 19/04/2018 11:54:00 line : 1003**

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Causa**

O erro era ocasionado devido a uma inconsistência no binário (APPSERVER).

**Solução**

A correção foi efetuada na issue **mtec**-**3334**, todavia ao associar esta correção ao ticket do cliente está recebendo a  seguinte mensagem do desenvolvimento:

*"A Release Oficial 13.2.3.48 foi expedida e publicada na Central de Downloads.*  
*O pacote pode ser acessado no endereço: **[https://suporte.totvs.com](https://suporte.totvs.com/),** seção de Downloads.*

*Não esqueça de responder a nossa Pesquisa de Satisfação para melhor atendê-lo*."

**Ou seja, a indicação é para efetuar o download do Appserver versão 13.2.3.48 no portal do cliente, conforme abaixo:**  
1. Efetue o download do último **APPSERVER** com versão igual ou acima a 13.2.3.48 na central de dowloads:

APPSERVER VERSAO 12 WINDOWS 13.2.3.48 ATÉ A RELEASE 12.1.17 -  <https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657319>

APPSERVER VERSAO 12 LINUX 13.2.3.48 ATÉ A RELEASE 12.1.17 -

<https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657318>

2. Atualize o APPServer do seu ambiente .

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
