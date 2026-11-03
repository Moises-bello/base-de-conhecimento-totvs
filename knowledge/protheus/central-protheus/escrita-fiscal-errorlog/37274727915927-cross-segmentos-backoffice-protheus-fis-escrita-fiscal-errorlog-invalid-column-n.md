---
article_id: 37274727915927
category: Escrita Fiscal - Error.log
content_hash: cc7da11ac08e625f02261ccac0439be106051912b6514309360c47be218f4678
fetched_at: '2026-06-28T22:39:32.778279+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Escrita Fiscal - ErrorLog Invalid
  column name 'CJ2_MSGCOD'.
type: support-article
updated_at: '2025-12-26T17:18:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37274727915927-Cross-Segmentos-Backoffice-Protheus-FIS-Escrita-Fiscal-ErrorLog-Invalid-column-name-CJ2-MSGCOD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37274727895703) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como corrigir o error log: Invalid column name '**CJ2\_MSGCOD**' ao escriturar nota com cálculo vindo do **FISA170 (Configurador de Tributos)**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.2410**

**Solução**

**1** - Aplique a **expedição contínua** de acordo com sua release no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851#issues-17>

**2** - Pegue o arquivo "**sdfbra**" deste acumulado e adicione na sua **systemload**

**3** - Garanta que não exista arquivos com nome "**mpupddistr.dsk**" na pasta do **appserver**

4 - Execute o **UPDDITR** e reinicie os serviços

Após isso, realize novos testes.
