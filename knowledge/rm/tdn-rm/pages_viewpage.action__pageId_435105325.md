---
content_hash: 62cedcd569d954c07ffcf4ae05df047ee87cc182acc89be5d147ba17eda8b18a
fetched_at: '2026-06-29T00:09:49.577854+00:00'
page_id: '435105325'
product: rm
source: tdn-rm
title: Venda com alguns tipos de Aditivos Em Preparação com Impacto em lançamentos
  financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105325
version: 1
---

**Venda com alguns tipos de Aditivos Em Preparação com Impacto em lançamentos financeiros**   
Na versão de revitalização foi criado o conceito de "bloqueio" de lançamento financeiro que é aplicado aos aditivos de venda ao criarem, alterarem e ou excluírem algum lançamento financeiro antes de ser efetivado. Antes estes lançamentos financeiros eram cancelado. Isso impede que os lançamentos em questão sofram qualquer ação até que sejam liberados, por isso vendas com aditivos em preparação que manipulam o plano de financiamento são impeditivas para a revitalização e precisarão da tomada de decisão por parte do usuário do que deve ser feito com elas antes da conversão.  
   
  
   
   
Para saber exatamente quais são as vendas que possuem aditivos nessa situação a ferramenta faz a seguinte consulta:  
   
SELECT XADIT.CODCOLIGADA, XADIT.NUMVENDA, XADIT.NUMADIT AS NUMADITIVO FROM XADIT WHERE XADIT.CODSITADIT IN (1, 4, 5)                 AND EXISTS (SELECT 1                                       FROM XADITTIPOADITIVO                                           WHERE                                              XADITTIPOADITIVO.CODCOLIGADA = XADIT.CODCOLIGADA                                             AND XADITTIPOADITIVO.NUMVENDA = XADIT.NUMVENDA                                             AND XADITTIPOADITIVO.NUMADIT = XADIT.NUMADIT                                             AND XADITTIPOADITIVO.CODTIPOADIT IN ('A1','A3','A6','A7','A8')) ORDER BY XADIT.CODCOLIGADA, XADIT.NUMVENDA, XADIT.NUMADIT  
   
   
A consulta acima não precisa ser executada pelo usuário pois é feita internamente pelo sistema e tem propósito apenas ilustrativo.  
As vendas com Aditivos que forem resultado da consulta acima serão apresentadas para que o usuário "Cancele" ou "Efetive";
