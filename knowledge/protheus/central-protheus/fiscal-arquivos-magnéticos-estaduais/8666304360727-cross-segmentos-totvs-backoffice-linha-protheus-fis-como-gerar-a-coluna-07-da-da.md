---
article_id: 8666304360727
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 535153d2ae94ceed22541f7f37c6d1f5460cade7b9e0200f4cafa57d840bdade
fetched_at: '2026-06-28T22:42:11.882129+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar a coluna
  07 da DAPIMG? '
type: support-article
updated_at: '2022-09-05T20:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8666304360727-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-a-coluna-07-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min****Dúvida**Como gerar a **coluna 07 da DAPIMG**?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**

O sistema verifica a configuração da **TES**, através dos campos:

* **Sit.Trib.ICM (F4\_SITTRIB)** = 20 - Isentas
* **% Red. do ICMS (F4\_BASEICM)**= Preenchido

O Valor considerado é o valor gravado**, Vlr Isen ICM (FT\_ISENICM)**, na tabela **LIVRO FISCAL POR ITEM DE NF.**
