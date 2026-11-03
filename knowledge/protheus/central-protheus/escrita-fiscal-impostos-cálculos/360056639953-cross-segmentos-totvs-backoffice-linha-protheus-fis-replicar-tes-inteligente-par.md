---
article_id: 360056639953
category: Escrita Fiscal - Impostos - Cálculos
content_hash: f5bf2e530ee9cff5e89546fce99192e8cb86f25e73dfc1a9ebab52348a3e7d27
fetched_at: '2026-06-28T22:39:30.462148+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Replicar TES Inteligente
  para os itens na classificação do documento de entrada'
type: support-article
updated_at: '2026-06-19T19:40:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056639953--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Replicar-TES-Inteligente-para-os-itens-na-classifica%C3%A7%C3%A3o-do-documento-de-entrada
---

**Dúvida**Como replicar o tipo de operação (**D1\_OPER**) para todos os itens na classificação do documento de entrada?  
  
**Ambiente**Protheus – Compras/Fiscal – A partir da versão 11.80  
  
**Solução**Para que o Tipo de Operação seja replicado para os demais itens é necessário configurar a pergunta, conforme abaixo, pressionando **F12** ao abrir a rotina **MATA103** antes de acionar a funcionalidade de classificação:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092666114/mceclip0.png)  
  
Com esta configuração, ao preencher o campo **D1\_OPER** do primeiro item a ser classificado ,o mesmo tipo de operação será carregado para os itens abaixo.
