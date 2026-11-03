---
article_id: 5099776475927
category: Faturamento - Cadastros
content_hash: a958088afe646750374d97f3ae1bc8ed16e4871925fe708dde2fd4fed4a02251
fetched_at: '2026-06-28T22:38:35.333258+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Reference counter
  overflow ( over 32700 )  na exportação da consulta genérica da SA1 em MVC
type: support-article
updated_at: '2022-03-29T17:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5099776475927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reference-counter-overflow-over-32700-na-exporta%C3%A7%C3%A3o-da-consulta-gen%C3%A9rica-da-SA1-em-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Após mudar a chamada do cliente para mvc, usando crma980, ao exportar uma consulta genérica da SA1, ocorre o erro:

Reference counter overflow ( over 32700 ) on tLocalEnv::IncRefs() in file C:\bamboo\xml-data\build-dir\TP11-OF19310-TECXWIN64\advpl\localenv.cpp at line 357 on FWFORMMODELSTRUCT:LOADTRIGGERS(FWFORMMODELSTRUCT.PRX) 22/03/2022 15:52:11 line : 516  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.27.  
  
**Causa**O problema ocorria por conta da leitura da função **PICCLI** , usada para tratar CNPJ do cliente, quando buscado via crma980, onde foi ajustado para o carregamento dentro do Modelo MVC CRMA980.

Por conta desta função, também eram gerados lentidão na extração da consulta e travamento da consulta da tabela Sa1, corrigidos com este ajuste.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Baixe o último pacote de expedição continua do módulo Faturamento: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**  
2.Via VS-CODE, efetue a aplicação da atualização;  
3. Reinicie o smartclient e refaça o processo.

Obs: O fonte **MATV030** deverá estar com data igual ou superior a **08/03/2022** para que a correção ocorra.
