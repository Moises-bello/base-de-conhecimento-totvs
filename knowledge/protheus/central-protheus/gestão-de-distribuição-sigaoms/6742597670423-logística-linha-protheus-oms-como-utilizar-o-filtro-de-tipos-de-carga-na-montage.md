---
article_id: 6742597670423
category: Gestão de Distribuição (SIGAOMS)
content_hash: 080e6929f342a9df410c58114ff115f8751af69c9d720e632fe93aa5376abac9
fetched_at: '2026-06-28T22:45:49.763812+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como utilizar o Filtro de Tipos de Carga
  na Montagem de Carga - OMSA200
type: support-article
updated_at: '2022-06-17T18:31:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6742597670423-Log%C3%ADstica-Linha-Protheus-OMS-Como-utilizar-o-Filtro-de-Tipos-de-Carga-na-Montagem-de-Carga-OMSA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:42 min** **Dúvida**Como utilizar o **Filtro de Tipos de Carga** na **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**No **TOTVS OMS - Order Management System**, disponibilizamos o cadastro de **Modelos de Carga - OMSA180 - tabela DB0**. Essa rotina é um recurso extra para filtragem dos **Pedidos de Vendas** e **Produtos** que serão alocados em uma carga.   
  
Com o cadastro de **Modelos de Carga** realizado, possibilitará que sejam montadas **Cargas Exclusivas** para determinados tipos de produtos, como por exemplo **produtos secos**, **produtos químicos** ou **perecíveis**. Facilitando o direcionamento desses produtos a veículos especiais de acordo com o **Modelo de Carga selecionado**.  
  
Além disso, poderá ser utilizado para facilitar a **visualização** dos **Pedidos de Vendas** na rotina de **Montagem da Carga - OMSA200** apresentando somente os **Pedidos de Vendas** que contém determinados **Produtos**.  
  
O **Modelo de Carga** deve estar vinculado a um **Tipo de Carga**, correspondente a um registro da **tabela** **DU**, do arquivo de **Tabelas Genéricas - SX5**. Para que o filtro seja efetivo na rotina de **Montagem da Carga - OMSA200**, é necessário vincular um **Modelo de Carga** ao **Cadastro de Produto - MATA010 - Aba Outros, campo Tipo Carga - B1\_TIPCAR.**

**![MODELOS.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6764220243607/MODELOS.jpg)**

**![mata010.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6762480582807/mata010.png)**

**![FILTRO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6762695591191/FILTRO.jpg)**

**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Modelos de Carga - OMSA180](https://tdn.totvs.com/pages/viewpage.action?pageId=572493333)[Logística - Linha Protheus - OMS - Quais são os cadastros básicos para utilização da rotina de Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009375522-Log%C3%ADstica-Linha-Protheus-OMS-Quais-s%C3%A3o-os-cadastros-b%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-da-rotina-de-Montagem-de-Carga-OMSA200)
