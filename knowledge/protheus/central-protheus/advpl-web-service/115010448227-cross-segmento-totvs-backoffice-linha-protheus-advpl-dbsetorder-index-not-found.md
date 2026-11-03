---
article_id: 115010448227
category: ADVPL - Web Service
content_hash: e5c826a959a6b0a22971da907aa387fc338c8c8d01c430f3e166b6f19da0d000
fetched_at: '2026-06-28T22:40:10.535159+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - DBSetOrder -
  Index not found: Fwschedule Order Number: 1 '
type: support-article
updated_at: '2024-06-03T17:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010448227-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-DBSetOrder-Index-not-found-Fwschedule-Order-Number-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**DBSetOrder - Index not found: FWSCHEDULE Order Number: 1 on FWTABLEDDL:OPENTABLE(FWTABLEDDL.PRX) , como tratar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**  
O erro **DBSetOrder** pode ocorrer quando há dois RPO´s (repositórios) apontando para a mesma pasta de dicionário de dados (*RootPath\StartPath*), onde um RPO (repositório) está mais atualizado que o outro, fazendo com que de divergência na criação dos índices.  
Lembrando que é recomendável, quando utilizar mais de um ambiente, apontar cada RPO (repositório) para uma pasta System diferente, ou seja, no arquivo .ini, utilizar uma pasta "*RootPath*=" diferente para cada ambiente que tiver RPO (repositório) diferente.  
Para corrigir este erro é necessário separar o *SYSTEM* dos ambientes ou efetuar a atualização do RPO (repositório) + UPDATE + LIB da base de produção e base de teste (ambas devem estar com a mesma data).  
Com a atualização da Lib, já existe uma proteção quanto ao cenário acima:  
[Proteção contra libs distintas aplicadas no mesmo ambiente](http://tdn.totvs.com/pages/viewpage.action?pageId=268816127)  
  
Observação:   
Após a correção faça o seguinte:  
- Pare o Protheus;  
- Acesse a pasta protheus\_data e renomeie a pasta semáforo;  
- Entre na pasta System;  
- Renomeie os arquivos xx1, xx2,xx3.dbf ou .dtc;  
- Apague o arquivo xx1,xx2,xx3.cdx;  
- Apague o conteúdo da pasta %TEMP% do sistema OP;  
- Remova da pasta system para uma pasta de backup os arquivos: \_schedtsk.dbf ou .dtc, .fpt e .cdx, sxh.dtc .fpt, .dbf e .cdx;  
- Reinicie o Protheus;  
  
Faça novo teste acessando o Configurador / Schedule;

Destes arquivos que estamos realizando o procedimento, os únicos que precisam ser appendados nas novas tabelas criadas são os arquivos xx1, xx2 e xx3 os demais não são necessários.
