---
article_id: 360022395111
category: CRM - Dúvidas Gerais
content_hash: 66b53c819764776daf9e5ea756bbeb5b5bbd01c74f3318dadd3249d142ed8a01
fetched_at: '2026-06-28T22:40:27.425620+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Como configurar envio do
  e-mail via WORKFLOW quando chega a determinado estágio do Processo de Vendas na
  Oportunidade
type: support-article
updated_at: '2024-04-25T12:18:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022395111-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Como-configurar-envio-do-e-mail-via-WORKFLOW-quando-chega-a-determinado-est%C3%A1gio-do-Processo-de-Vendas-na-Oportunidade
---

**Dúvida**

Como configurar envio do e-mail via WORKFLOW quando chega a determinado estágio do Processo de Vendas na Oportunidade  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
  
**Solução**

A partir da configuração dos Estágios do Processo de Vendas (FATA010) é possível indicar pelo campo AC2\_SENDFENDWF se deverá ser enviado um Workflow aos responsáveis pelos produtos da Proposta relacionada à Oportunidade que atingir este estágio.

**Observação**: Tendo configurado o WorkFlow do Protheus, inserir os arquivos do link: [Arquivos para implantação do disparo de eventos nos estágios da oportunidade de venda - Versão 11.5](http://tdn.totvs.com/pages/viewpage.action?pageId=123601624) na Pasta WorkFlow (Localizada na Protheus Data).

Na rotina Processo de Vendas (FATA010), configurar o campo AC2\_SENDFENDWF (Notifica RSP) como Sim.

**Para realizar a configuração, saiba mais:**

<http://tdn.totvs.com/pages/viewpage.action?pageId=307840446>
