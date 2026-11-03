---
article_id: 360037895954
category: Call Center - Telemarketing
content_hash: 4f3bf7dd89c0c868ff4ac34a13e0d5e4ce91712bfbefb3f614704bbd1411652d
fetched_at: '2026-06-28T22:41:29.437094+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-Geração de OS para
  Gestão de Serviço através do atendimento Telemarketing
type: support-article
updated_at: '2022-06-22T18:06:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037895954-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Gera%C3%A7%C3%A3o-de-OS-para-Gest%C3%A3o-de-Servi%C3%A7o-atrav%C3%A9s-do-atendimento-Telemarketing
---

**Dúvida**

Configurada uma ação do telemarketing com o campo "Gera OS" (**UQ\_GERAOS**) preenchido com Sim, mas não está gerando Ordem de Serviço (**TECA450**) no Gestão de Serviços.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- todas as versões.

**Solução**

Para habilitar a geração de Ordem de Serviço no módulo Gestão de Serviços, em **Telemarketing , Cadastro de ações (TMKA240)**, além de configurar o campo **Gera OS** como **Sim** , precisa configurar na aba **Outros**, uma ocorrência técnica no campo **Oco/Prb Tec (UQ\_TECOCOR).**

Este campo se refere a ocorrência cadastrada no Gestão de Serviços para que haja a integração, além, disso, no atendimento Telemarketing (**TMKA272**), é necessário informar o número de série do produto no campo **UD\_NSERIE** (Num.Serie), tendo em vista que a base de atendimento é composta pelo código do produto e a série.

Feito estas ações, basta confirmar o atendimento que haverá a integração com o módulo Gestão de Serviços e a geração da OS (Ordem de Serviço).

![Telemarketing_x_gera__o_da_OS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360050650693/Telemarketing_x_gera__o_da_OS.gif)
