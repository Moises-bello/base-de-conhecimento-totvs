---
article_id: 360026233534
category: Gestão de Armazenagem (WMS)
content_hash: 3f762ea0d20e5c0c3dc7016b7682fe6731ca2b2d8e76f328163279989560aae3
fetched_at: '2026-06-28T22:45:47.977940+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Busca da estrutura física nos processos
  WMS
type: support-article
updated_at: '2021-07-19T17:46:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026233534-Log%C3%ADstica-Linha-Protheus-WMS-Busca-da-estrutura-f%C3%ADsica-nos-processos-WMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura:**00:00:42 min**  
**Dúvida**Como é feita a busca da estrutura física nos processos **WMS - *Warehouse Management System***?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) -  A partir da versão 11.80  
  
**Solução**A estrutura física é obtida sempre de acordo com o armazém e com o endereço, visto que esta combinação deve ser única no Sistema.  
  
Os movimentos são gerados de forma que busquem automaticamente a estrutura física de destino, de acordo com o endereço informado. Logo, o Sistema não grava mais informações nos campos de estrutura física das tabelas de itens dos pedidos de venda, pedidos liberados, itens das notas fiscais de entrada e nem de movimentações internas.
