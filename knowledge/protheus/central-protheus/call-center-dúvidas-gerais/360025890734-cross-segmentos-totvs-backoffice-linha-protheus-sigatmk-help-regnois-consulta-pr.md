---
article_id: 360025890734
category: Call Center - Dúvidas Gerais
content_hash: c35115ac257264ea93ce1e1671cfa2f0dfd3998cdeeeb888f740cc36868b538b
fetched_at: '2026-06-28T22:41:26.832307+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- HELP REGNOIS CONSULTA
  PROSPECT
type: support-article
updated_at: '2022-06-17T14:56:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025890734-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-HELP-REGNOIS-CONSULTA-PROSPECT
---

**Ocorrência :**

No módulo de Call Center, atendimento Televendas, apresenta o Help **Regnois** ao consultar o prospect(**tmka260**) :

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041155073/mceclip0.png)**

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - A partir da release 12.1.17.  
  
**Causa**

O erro ocorre no momento da inclusão de um Atendimento do tipo **TeleVendas (TMKA273)**, onde ao informar um **Prospect** que não possui o mesmo código no cadastro de **Clientes**, é exibida a mensagem **"Regnois - Não existe registro relacionado a este código.", não permitindo "salvar".**  
  
**Solução**

Ajustado tratamento interno referente a consulta padrão do **Prospect** no momento da inclusão de um **Atendimento** do tipo **Televendas**, para corrigir, aplique o pacote referente a sua versão:

12.1.25: **<https://suporte.totvs.com/portal/p/10098/download?e=828905>;**

12.1.23:[**https://suporte.totvs.com/portal/p/10098/download?e=761040**](https://suporte.totvs.com/portal/p/10098/download?e=761040) ;

12.1.17:**<https://suporte.totvs.com/portal/p/10098/download?e=761039>** ;

**Obs...recomenda-se sempre aplicar o pacote em ambiente de testes para validação, e posteriormente aplicar em produção.**
