---
article_id: 360060227993
category: NFe - Nota Fiscal Eletrônica
content_hash: 2aee6fbc524cde2058c304190de16be05ad8c563a8fd25a20a7d4331a98676a3
fetched_at: '2026-06-28T22:40:01.809211+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - CONSULTA DE CHAVE  UTILIZANDO
  TOTVS COLABORACAO'
type: support-article
updated_at: '2021-10-11T15:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060227993--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-CONSULTA-DE-CHAVE-UTILIZANDO-TOTVS-COLABORACAO
---

**Ocorrência**Consulta de chave apresentando a mensagem, TSSINATIVO.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098820934/mceclip0.png)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Causa**A integração com Totvs Colaboração esta Ativa,  e o parâmetro MV\_CHVNFE=.T.  
  
**Solução**Totvs Colaboração não utiliza TSS, logo não há consulta direta via webService.  
A consulta de chave é um recurso que necessita exclusivamente de um TSS ativo, sendo assim deve ser desabilitado o parâmetro MV\_CHVNFE=.F.
