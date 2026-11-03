---
article_id: 360019870372
category: RH - Recibos e Cheques
content_hash: 52e978ee544d9cb59074d2a3c8658f00d3b966736b350668fe0d2bd438c23d55
fetched_at: '2026-06-28T22:43:29.468082+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Como aglutinar verbas repetidas no recibo de pagamento
  (GPER030) e nos relatórios da folha (GPER040 e GPER106)
type: support-article
updated_at: '2025-04-14T16:49:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019870372-RH-Linha-Protheus-GPE-Como-aglutinar-verbas-repetidas-no-recibo-de-pagamento-GPER030-e-nos-relat%C3%B3rios-da-folha-GPER040-e-GPER106
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31402591407383) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como aglutinar verbas repetidas no recibo de pagamento (GPER030) e nos relatórios da folha (GPER040 e GPER106)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
  
**Solução**Para que as verbas sejam apresentadas de forma aglutinadas nos relatórios e recibo de pagamentos, foi criado o parâmetro MV\_AGLUTPD. Para ativar o parâmetro siga os passos abaixo:

**1.** Acesse o configurador **SIGACFG** e em **Ambiente > Cadastros > Parâmetros (CFGX017)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402598102807)

**2.** Pesquise pelo parâmetro **MV\_AGLUTPD**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402591412119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402598105239)

**3.** Para que as verbas sejam aglutinadas configure o parâmetro **MV\_AGLUTPD** com **1**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402591421591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402591426967)

**Recibo de Pagamento:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402598111767)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402598112535)

**Relatório Folha de Pagamento:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31402598114967)

**Observação:** Lembramos que as verbas serão aglutinadas somente nos relatório da folha de pagamento (GPER040 e GPER106) e recibo de pagamento (GPER030).

**Saiba Mais:**RH- Recibos e Cheques
