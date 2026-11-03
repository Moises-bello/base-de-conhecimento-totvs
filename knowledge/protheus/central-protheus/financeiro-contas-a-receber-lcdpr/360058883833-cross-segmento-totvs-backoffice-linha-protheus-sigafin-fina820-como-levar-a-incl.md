---
article_id: 360058883833
category: Financeiro - Contas a Receber - LCDPR
content_hash: a91243c48f4163f56861521744f6f45c132c65f0a251ecb992d1c57082aef700
fetched_at: '2026-06-28T22:38:15.815855+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA820 - Como
  levar a inclusão do PA ou RA no LCDPR
type: support-article
updated_at: '2022-03-24T19:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058883833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Como-levar-a-inclus%C3%A3o-do-PA-ou-RA-no-LCDPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:02 min**

**Dúvida**Como levar a inclusão do **Pagamento Antecipado** (**PA**) ou **Recebimento Antecipado** (**RA)** no **Extrator do LCDPR** ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12.1.17  
  
**Solução**Deverá ser criados manualmente os parâmetros citado abaixo, para que o **Pagamento Antecipado** (**PA**) ou **Recebimento Antecipado** (**RA**) seja levado no momento da inclusão do **LCDPR** no **Livro Caixa do Produtor Rural**.

**MV\_LCDPRRA**Conteúdo:  
D = Digitação, títulos do tipo RA serão incluídos no arquivo LCDPR no momento de digitação.  
C = Compensação, títulos do tipo RA serão incluídos no arquivo LCDPR no momento de Compensação.

**MV\_LCDPRPA**Conteúdo:  
D = Digitação, títulos do tipo PA serão incluídos no arquivo LCDPR no momento de digitação.  
C = Compensação, títulos do tipo PA serão incluídos no arquivo LCDPR no momento de Compensação.
