---
article_id: 360026667774
category: Call Center - Help Desk
content_hash: ca6f56b05d4b35d51dc257097ad985b2f0d493ac4543187dc7830cb55f968753
fetched_at: '2026-06-28T22:41:27.657555+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-array out of bounds
  ( 0 of 11 )  on TK503ADELOK(TMKA503A.PRW)
type: support-article
updated_at: '2022-06-22T17:12:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026667774-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-array-out-of-bounds-0-of-11-on-TK503ADELOK-TMKA503A-PRW
---

**Ocorrência**

Ao realizar um cancelamento de um Teleatendimento, é gerado o seguinte error log: 

**array out of bounds ( 0 of 11 ) on TK503ADELOK(TMKA503A.PRW) 02/06/2017 09:46:05 line : 2072**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- a partir da versão 11.80.

**Causa**O erro de array out of bounds ocorre quando o campo não existe no banco ou no dicionário de dados, quando não está como usado ou teve seu nível de campo alterado.

O sistema está requerendo dentro do array, o campo **ADF\_CODSUQ** e não está encontrando.

**Solução**

Para solucionar essas ocorrências, realize os seguintes passos:

1. Verifique se o campo existe na tabela SX3;

2. Verifique se o campo existe dentro da tabela **ADF**;

3. Verifique se via configurador, se o campo está em uso e com o nível igual a 1;

4. Após as verificações e ajustes, reinicie o smartclient e refaça o processo de cancelamento.
