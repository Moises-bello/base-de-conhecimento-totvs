---
article_id: 360022092812
category: Financeiro
content_hash: 7a0c766579ed09f71d740cc7e287c70e26a568c415ec17f73b9fa2219735eb48
fetched_at: '2026-06-28T22:38:03.212140+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA989 - Errorlog
  TCSetField- Alias does not exist SCGN000010 on MNTQRYPAG(FINA989.PRW) '
type: support-article
updated_at: '2022-06-15T01:58:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022092812-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA989-Errorlog-TCSetField-Alias-does-not-exist-SCGN000010-on-MNTQRYPAG-FINA989-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Na rotina **EXTFISXTAF**, ao realizar a geração do extrator fiscal ocorre o erro.log **TCSetField- Alias does not exist SCGN000010 on MNTQRYPAG(FINA989.PRW) 29/12/2018 09:08:05 line : 2515**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA989 - Todas as versões  
  
**Causa**Primeira causa do error.log é por não ter o campo **FKF\_ORIINS** criado na base de dados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019289652/mceclip1.png)  
  
Segunda causa do error.log, essa sendo corrigida na ISSUE **DSERFINP-21741** ocorre quando a configuração do arquivo **appserver.ini** a chave **TOPDataBase** esta com o conteúdo **MSSQL7**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019289532/mceclip0.png)

**Solução**1 - Se não tiver criado o campo **FKF\_ORIINS** na base de dados, deve atualizar o dicionário de dados disponível na pagina do REINF.  
Link: [Pacote de atualização REINF - 2018](http://tdn.totvs.com/pages/releaseview.action?pageId=346489720)   
  
2 - Caso utilize a configuração no **appserver.ini** a chave do **TOPDataBase** com o conteúdo **MSSQL7** uma solução **paliativa** é utilizar o conteúdo **MSSQL**, com essa configuração será possível realizar a geração do extrator fiscal.
