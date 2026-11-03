---
article_id: 17184149287703
category: Materiais - Compras (SIGACOM)
content_hash: 80f7ecd4dcce6772aa92ba70575c560e154a5a163029af2adb6d80d4142b86ca
fetched_at: '2026-06-28T22:41:20.213088+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Motivo da ocorrência
  do Help A12020
type: support-article
updated_at: '2023-08-31T18:34:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17184149287703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Motivo-da-ocorr%C3%AAncia-do-Help-A12020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17184109680791) Tempo aproximado para leitura: 00**:02:00 min****Ocorrência**Ao digitar o código do produto no pedido de compras, o sistema gera o help A12020.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Causa**Para gerar o help A12020, o sistema valida as informações abaixo  
  
Se o campo **B1\_MONO = S**, verifica se o **B1\_PROC = C7\_FORNECE.**  
  
Ou seja, quando o campo **B1\_MONO = S,** significa que o fornecimento de um produto será feito por apenas um fornecedor com base na informação do campo **Fornecedor Padrão (B1\_PROC).** O fornecedor responsável por realizar o fornecimento (B1\_PROC) deve ser o mesmo fornecedor para o qual o pedido de compras em questão foi emitido, que é armazenado no campo **C7\_FORNECE.**  
  
**Solução**

Dessa forma, verifique se o fornecedor para o qual está sendo lançado o pedido de compras em questão (**C7\_FORNECE**) é o mesmo que o fornecedor que consta no campo **B1\_PROC** do produto que está sendo digitado.

***Saiba Mais :***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
