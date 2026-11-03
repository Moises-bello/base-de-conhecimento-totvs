---
article_id: 360018760351
category: Call Center - Telemarketing
content_hash: fd93bc2256a16952c295db290b46b5aa4b36be23de8404303c05bcfa267a3d0a
fetched_at: '2026-06-28T22:41:29.448397+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-Utilização dos
  campos: Grava Atendimento e Evento'
type: support-article
updated_at: '2022-06-22T18:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760351-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Utiliza%C3%A7%C3%A3o-dos-campos-Grava-Atendimento-e-Evento
---

**Dúvida**

Qual a utilização dos campos UQ\_INTWOR e UQ\_EVENTO no atendimento Telemarketing?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-a partir da versão 11.  
  
**Solução**

Procedimento de uso dos campos **UQ\_INTWOR** e **UQ\_EVENTO** no atendimento Telemarketing:

A configuração dos campos UQ\_INTWOR e UQ\_EVENTO é efetuada em **Call Center/ Atualizações/ Telemarketing/ Ações (Rotina: TMKA240)**.

Quando configurado no Cadastro de Ações, o campo **Grv.Atendim** (UQ\_INTWOR**)**como **Sim**, ao incluir um Atendimento Telemarketing, utilizando a entidade **SUSPECT**, ao finalizar o atendimento, confirmando a conversão do SUSPECT em **PROSPECT**, conforme a mensagem sistêmica: (Confirmar a conversão desse SUSPECTem um novo PROSPECT?), o sistema gravará o Atendimento Telemarketing e informará o código deste atendimento realizado no campo **ACH\_CODTMK**.

Se o campo **UQ\_INTWOR**estiver configurado como **Não,** mesmo realizando o processo descrito anteriormente, o sistema gravará o atendimento telemarketing, mas não gravará o código do atendimento no campo **ACH\_CODTMK.**

Quanto ao campo **Evento** (**UQ\_EVENTO)** somente é utilizado para o atendimento telemarketing quando fizer uso de campanhas cadastradas e amarradas a ele.

Obs:Esses campos são utilizado somente para atendimento (**Telemarketing**).
