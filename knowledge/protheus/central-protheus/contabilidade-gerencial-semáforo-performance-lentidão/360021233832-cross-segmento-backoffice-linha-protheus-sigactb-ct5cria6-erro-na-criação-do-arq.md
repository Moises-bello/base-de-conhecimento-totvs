---
article_id: 360021233832
category: Contabilidade Gerencial - Semáforo, Performance, Lentidão
content_hash: 71f5d65ce373352920ca5c26acb1b949acd9848ea523b38c513a2bf2a7765e80
fetched_at: '2026-06-28T22:41:02.611434+00:00'
product: protheus
section_id: 1500001537321
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CT5CRIA6 - Erro na criação
  do arquivo semáforo de processamentos concorrentes
type: support-article
updated_at: '2021-12-10T18:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021233832-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CT5CRIA6-Erro-na-cria%C3%A7%C3%A3o-do-arquivo-sem%C3%A1foro-de-processamentos-concorrentes
---

**Ocorrência**

Ao tentar contabilizar movimento, apresenta mensagem:CT5CRIA6 - Erro na criação do arquivo semáforo de processamentos concorrentes  
  
**Ambiente**Protheus – A partir da versão 11.80  
  
**Causa**

O erro é ocasionado por falha ao abrir os arquivos  \_CTBProc\*.\* ou \_TBProc\*.\*  dentro do diretório system, seja por corrompimento dos arquivos ou por limite de tamanho.

**Solução**Para solucionar o incidente basta realizar um backup destes arquivos, deleta-los e permitir que o sistema o recrie.
