---
article_id: 16333206660247
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: c842a9575be9cbd9a3c9a1efeb3b01c211021102a1d4e4996d9216316220f871
fetched_at: '2026-06-28T22:38:48.175691+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Como configurar
  o alerta de finalização das etapas de processamento da rotina Acompanha Custos?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16333206660247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Como-configurar-o-alerta-de-finaliza%C3%A7%C3%A3o-das-etapas-de-processamento-da-rotina-Acompanha-Custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16333195939479) Tempo aproximado para leitura: **00:02:59 min****Dúvida**Como configurar o alerta de finalização das etapas de processamento da rotina Acompanha Custos?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da release 12.1.33

**Solução**

Durante as etapas de processamento, existe o seguinte trecho de texto:

"será alertado quando o processo estiver finalizado."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16333137820183)

Na verdade, esse texto se refere da possibilidade de configurar um alerta, a ser enviado por e-mail, quando a rotina em processamento foi finalizada.

A rotina Acompanha custos, é como se fosse uma biblioteca, que agrupa as rotinas:

-MATA330 - Recalculo do custo médio;

-MATA350 - Saldo Atual para final;

-MATA331 - Contabilização de estoque;

-MATA280 - Virada de saldos;

Então, caso queira ser alertado, durante a finalização de alguma dessas etapas, as rotinas podem ser configuradas via eventviwer, para que receba um e-mail quando elas forem finalizadas.

Abaixo, segue boletim, de como realizar essa configuração de eventos.

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)**

**Saiba Mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*
