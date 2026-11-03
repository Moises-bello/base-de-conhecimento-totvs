---
article_id: 5168158696343
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 049fe639934190808dbd93e102b13a4de15bc47921eef60b3ad19a2ede17591e
fetched_at: '2026-06-28T22:39:47.744838+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro AVREPLACE
  referenciando o RUP_EIC ao atualizar o TAF
type: support-article
updated_at: '2022-04-01T14:47:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5168158696343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-AVREPLACE-referenciando-o-RUP-EIC-ao-atualizar-o-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Erro AVREPLACE referenciando o RUP\_EIC ao atualizar o TAF, como corrigir?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5167934414359/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Solução**Deve ser baixado o dicionário completo e diferencial no Portal do Cliente e após executar o ***UPDDISTR:***  
Completo: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_compl>  
Diferencial: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_dif>  
  
Após a finalização do ***UPDDISTR***, rode o atualizador do ***TAF*** novamente.  
  
**Saiba mais**  
[Como atualizar dicionários (UPDDISTR)](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468)  
[OINF0011.2 - Atualizações Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596)
