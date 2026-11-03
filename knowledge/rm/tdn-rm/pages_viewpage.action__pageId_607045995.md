---
content_hash: 8e9e7065946cbc5fec473a7d12a53fb36a510899d751255a1a8c6d6a9661cf56
fetched_at: '2026-06-29T00:10:58.814773+00:00'
page_id: '607045995'
product: rm
source: tdn-rm
title: BDE - Configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607045995
version: 3
---

**Configuração BDE/ODBC**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007255132-RM-BD-Como-configurar-uma-conex%C3%A3o-ODBC-SQL-Server-2012-e-superiores-?source=search>

**Falhas conhecida PCP vs BDE**

1. Funcionamento anormal do sistema por configuração incorreta BDE/ODBC, ver documentação acima.
2. O BDE tem limite de tamanho de registro e quando esse é ultrapassado por ocorrer erro de "Violação de Acesso" ou fechamento do aplicativo, esse limite é em torno de 8150 caracteres e está comumente associado a tabelas de campo complementar com muitos campos do tipo varchar definidos com 255+ caracteres, se estiver com esse problema tente reduzir a quantidade de campos ou reduzir o tamanho dos campos.  
   1. Falha na entrada de produção pode estar relacionada a isso, veja TMOVCOMPL, TITMMOVCOMPL.
