---
article_id: 360042473134
category: Call Center - Dúvidas Gerais
content_hash: f1c79ccdcc41fdce96327416b0138b105cdf6cd88f178d1f6778390d6f68169c
fetched_at: '2026-06-28T22:41:26.977131+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK - AO POSICIONAR
  NA SEGUNDA LINHA DO HISTÓRICO DE LIGAÇÕES O SISTEMA GERA ERROR.LOG
type: support-article
updated_at: '2022-06-17T19:20:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042473134-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-AO-POSICIONAR-NA-SEGUNDA-LINHA-DO-HIST%C3%93RICO-DE-LIGA%C3%87%C3%95ES-O-SISTEMA-GERA-ERROR-LOG
---

**Dúvida**  
Ao posicionar na segunda linha da tela histórico de ligações o sistema gera error.log.  
  
**Ambiente**  
Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK – A partir da release12.1.25.  
  
**Solução**

Quando é posicionado na segunda linha da tela Histórico de ligações, conforme o anexo abaixo:

![Historico_de_liga__o.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057652373/Historico_de_liga__o.png)É apresentado o erro abaixo:

array out of bounds ( 2 of 1 ) on { || TRANSFORM(OGETACG:ACOLS[N][NPOSSIT],TRIM(OGETACG:AHEADER[NPOSSIT][3])) }(TMKA274.PRW) 04/06/2019 16:48:40 line : 202

E para correção é necessário estar com a LIB e a rotina: TMKA274 atualizados conforme os links abaixo:

**Versão LIB 20191122\_P12**  
<https://suporte.totvs.com/portal/p/10098/download?e=849181>

**Rotina: TMKA274**

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=838004> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=838003> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=838002> ;
