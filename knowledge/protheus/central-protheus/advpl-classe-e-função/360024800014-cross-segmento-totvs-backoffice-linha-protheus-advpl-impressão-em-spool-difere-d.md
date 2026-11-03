---
article_id: 360024800014
category: ADVPL - Classe e Função
content_hash: 3ed5e7561ed4f41891e462760207c599472e4bcb40a0d3d91bee1c1c9725b8c4
fetched_at: '2026-06-28T22:40:16.946849+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão em spool
  difere do arquivo PDF
type: support-article
updated_at: '2024-03-07T20:02:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024800014-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-em-spool-difere-do-arquivo-PDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao realizar a impressão de um arquivo gerado pela classe FwMsPrinter(), notamos que as proporções do mesmo diferem se comparada a impressão gerado via spool (impressora local) e via gerador de arquivos \*.PDF.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Este incidente ocorre devido ao fato da classe FwMsPrinter() ser homologada apenas para impressões que utilizem o driver da impressora.

Assim sendo, quando são utilizadas impressoras virtuais de \*.PDF, podem ocorrer inconsistências de tamanho.  
  
**Solução**Criar um tratamento interno no fonte, para caso a impressão seja realizada via spool, utilizar as medidas definidas, caso seja via impressora virtual de \*.PDF, utilizar outras medidas.
