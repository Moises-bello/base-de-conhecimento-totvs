---
article_id: 360018880992
category: Contabilidade Gerencial - Semáforo, Performance, Lentidão
content_hash: 40368ddc3fd11b271fbd03f1539b350e53b4f43f7aa362632458ed1a9d18345e
fetched_at: '2026-06-28T22:41:02.616901+00:00'
product: protheus
section_id: 1500001537321
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Gráfico ilustrativo
  - semáforo para processamentos simultâneos de rotinas off-line e on-line'
type: support-article
updated_at: '2021-12-10T18:45:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018880992-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Gr%C3%A1fico-ilustrativo-sem%C3%A1foro-para-processamentos-simult%C3%A2neos-de-rotinas-off-line-e-on-line
---

**Dúvida**Gráfico ilustrativo - semáforo para processamentos simultâneos de rotinas off-line e on-line

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Este recurso garante a consistência das informações durante a gravação e atualização das tabelas de saldos, ao executar as rotinas on-line e processamentos off-line de forma concorrente.

O controle de semáforo por processo ou serialização por processo está definido no Sistema como padrão e atua permitindo que processos de integração e manutenção de lançamentos sejam executados simultaneamente aos processamentos off-line, efetuando a seguinte ação: enquanto houver um processamento off-line em execução, serão bloqueadas as execuções de novos processos on-line ou off-line.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014918232/mceclip0.png)

**Importante:**

Esse controle aplica-se tanto para ambientes configurados com atualização de saldos on-line quanto off-line, independente da configuração dos parâmetros MV\_ATUSAL e MV\_SLDCOMP e do uso de stored procedures no ambiente Contabilidade Gerencial.
