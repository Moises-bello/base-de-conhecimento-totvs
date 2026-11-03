---
article_id: 14849670118039
category: TAF - REINF
content_hash: 353b720dfb80cc3351f218b305c178722fa6fe9c7461c336d1a8f18c4ba818ce
fetched_at: '2026-06-28T22:41:33.614735+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Cadastro de FCI/SCP para
  layout 2.1.1
type: support-article
updated_at: '2023-05-31T12:24:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14849670118039-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Cadastro-de-FCI-SCP-para-layout-2-1-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar o evento R1050  a partir do layout 2.1.1 ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução**

O cadastro de FCI/SCP serve como base para geração das informações do evento R1050 - Tabelas de entidades.

Este cadastro pode ser preenchido de forma manual na  rotina Cadastro FCI Scp   (**TAFA536**)  ou pode ser integrado por meio do layout **T159/T159AA**.

Para que a amarração correta do evento R-1050 seja feita com os eventos de pagamento R-4010/R-4020 é necessário que os participantes que serão utilizados nos eventos de movimento estejam listados neste cadastro.

Segue o exemplo:

![FCI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14849158639511)

Após a apuração do evento R1050  no painel Reinf, o evento pode ser acessado através do menu:

**Eventos REINF > Tabelas > R1050 Entidade Ligadas**
