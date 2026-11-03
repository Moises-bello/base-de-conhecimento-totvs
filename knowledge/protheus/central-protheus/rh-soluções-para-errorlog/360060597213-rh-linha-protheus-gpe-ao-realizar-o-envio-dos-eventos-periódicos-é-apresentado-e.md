---
article_id: 360060597213
category: RH - Soluções para error.log
content_hash: 9cbfd89c0ed8d418970ab58c42a3972aa925cdb9ac50c80f188a8e79c8ff16d6
fetched_at: '2026-06-28T22:44:08.779845+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao realizar o envio dos Eventos Periódicos é apresentado
  error log - RJ5XX0: SetOrder - Index not found. on FRJ5FILT(GPEM017C.PRW)'
type: support-article
updated_at: '2022-08-30T17:50:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060597213-RH-Linha-Protheus-GPE-Ao-realizar-o-envio-dos-Eventos-Peri%C3%B3dicos-%C3%A9-apresentado-error-log-RJ5XX0-SetOrder-Index-not-found-on-FRJ5FILT-GPEM017C-PRW
---

**Ocorrência**Ao tentar enviar os **eventos periódicos S-1200** do módulo de GPE ao TAF é gerado o ***error log:*** "**RJ5XX0: *SetOrder* - *Index not found. on* FRJ5FILT(GPEM017C.PRW)**"**Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.1.17  
  
**Causa**O erro ocorre por falta de **índice** na tabela **RJ5**  
  
**Solução**Para correção do erro é necessário efetuar a atualização do ambiente juntamente com atualização de dicionários (UPDDISTR) do pacote abaixo:  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)
