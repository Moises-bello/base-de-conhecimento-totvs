---
article_id: 4412989502487
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c1dc78d865f72c8c655c059cf2dd5605e7f09aaa3610697b419b5c485cc32301
fetched_at: '2026-06-28T22:38:38.643342+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Variable is
  not array Type [U] on MAFISRET(MATXFIS.PRX) 27/06/2019 13:19:39 line : 2235'
type: support-article
updated_at: '2021-12-17T19:39:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412989502487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Variable-is-not-array-Type-U-on-MAFISRET-MATXFIS-PRX-27-06-2019-13-19-39-line-2235
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao incluir um atendimento televendas, orçamento de vendas ou pedido de vendas, ocorrer o erro:

**variable is not array - Type [U] on MAFISRET(MATXFIS.PRX) 27/06/2019 13:19:39 line : 2235**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Causa**O erro ocorre por conta da falta de atualização da matxfis.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o downloads do pacote expedição contínua da escrita fiscal, conforme a sua release: **[Pacotes de Atualização - Fiscal - P12](https://tdn.totvs.com/x/a29XHw)**  
2. Via Vs-code, aplique a atualização. Observação, sempre efetue o devido backup do RPO antes de atualizar;  
3. Posteriormente, reinicie o smartclient e efetue o processo novamente.

***Importante: Para aplicação de pacotes, é necessário uma analista com conhecimento em Vs-code, caso seja um cliente Cloud - Totvs, solicite a aplicação pela equipe Cloud de atendimento.***

***Dúvidas sobre a rotina matxfis e impostos, contate a equipe de atendimento da Escrita Fiscal.***
