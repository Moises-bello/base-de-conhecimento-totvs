---
article_id: 360020165032
category: Materiais - Compras (SIGACOM)
content_hash: 46f8a1229478dfc1b7843bc1d1a53ad7417d80d3c12daec026a91cdc4bad4d77
fetched_at: '2026-06-28T22:41:07.399708+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - "Help: FWNOWIDTH"'
type: support-article
updated_at: '2022-05-16T22:05:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020165032-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-FWNOWIDTH
---

**Ocorrência**"Help: FWNOWIDTH

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016290451/mceclip0.png)

**Ambiente**  
Protheus – Materiais  – A partir da versão 11.80  
  
**Causa**O Help é apresentado quando existe diferença  entre o tamanho dos campos da tabela SA2 e os tamanho dos campos das tabelas relacionadas ao cadastro de fornecedor. Geralmente Apresentado pela diferença entre os campos do código do fornecedor.

**Solução**

"Help: FWNOWIDTH"  
Problema: Valor atribuído difere do tamanho do campo "município"  
  
Por gentileza, verificar se existe divergência de tamanho dos campos da tabela SA2 e CC2.  
Para que o erro em questão não seja apresentado, é necessário que os campos citados abaixo tenham o mesmo tamanho entre si:  
  
A2\_COD\_MUN seja igual a CC2\_CODMUN  
A2\_MUN seja igual a CC2\_MUN  
  
OBS: Caso tenha que alterar o tamanho de algum campo, por favor, faça-o via Configurador para que o campo seja alterado também na tabela no banco de dados, além de ser alterada no dicionário SX3.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM)
