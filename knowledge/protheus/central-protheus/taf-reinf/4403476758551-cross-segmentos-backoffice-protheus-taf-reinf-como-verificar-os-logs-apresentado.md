---
article_id: 4403476758551
category: TAF - REINF
content_hash: 40f3536047fb650c8b468587ee189f6d3f75d1336f62b82b47263ab0fb1693b8
fetched_at: '2026-06-28T22:41:33.784802+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como verificar os logs
  apresentados no appserver de inicio e fim da carga das tabelas autocontidas ?
type: support-article
updated_at: '2023-04-04T12:09:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403476758551-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-verificar-os-logs-apresentados-no-appserver-de-inicio-e-fim-da-carga-das-tabelas-autocontidas
---

**Dúvida**Como verificar os logs apresentados no appserver de inicio e fim da carga das tabelas autocontidas ?  
  
**Ambiente**TAF - A partir de 12.1.17  
  
**Solução**

Visando evitar mensagens de notificação e o aumento considerável no arquivo **console.log,** os logs apresentados no appserver de inicio e fim da carga das tabelas autocontidas foram removidos, agora serão apresentados somente quando a chave TafConOut estiver habilitada igual a 1 no appserver.

Para habilitar está funcionalidade é necessário criar a chave TafConOut na seção [General] do appserver.ini

Exemplo:

[General]

TafConOut=1

Opções:

0=Desabilita,1=Habilita

**Informações adicionais:**

DT TAF Conouts de inicio e término da carga nas tabelas autocontidas movidos para a função TAFCONOUT()

<https://tdn.totvs.com/pages/releaseview.action?pageId=626639668>

TAFConOut

<https://tdn.totvs.com/display/TAF/TAFConOut>

Centralizadora TAF

<https://tdn.engpro.totvs.com.br/display/public/TAF/Centralizadora+TAF>
