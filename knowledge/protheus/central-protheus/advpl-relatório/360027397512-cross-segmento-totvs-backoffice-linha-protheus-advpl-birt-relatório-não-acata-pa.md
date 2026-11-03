---
article_id: 360027397512
category: ADVPL - Relatório
content_hash: 8ab65c37a581cee84c6d2edaab6e198a211c345a95982516251965982a8efe62
fetched_at: '2026-06-28T22:40:22.748474+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - BIRT relatório
  não acata parâmetros '
type: support-article
updated_at: '2021-12-29T13:47:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027397512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-BIRT-relat%C3%B3rio-n%C3%A3o-acata-par%C3%A2metros
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:20:00 min*****Dúvida**Ao criar um Data Set com query com o carácter "?" não é acatado pelo relatório.

exemplo select \* FROM ZA1990 where ZA1\_MUSICA >= ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027228311/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Esse formato de query com **"?"** não é suportado pelo Birt no Protheus, pois não é possível vincular com os parâmetros do Data Set.

Mas pode ser criado sua query através do Dataset - ADVPL ou utilizando filtros dinâmico, segue passo a passo nos artigos abaixo.

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Relatório Birt utilizando SX1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016127131)

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Filtros dinâmicos no Birt](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018246551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027224272/mceclip1.png)
