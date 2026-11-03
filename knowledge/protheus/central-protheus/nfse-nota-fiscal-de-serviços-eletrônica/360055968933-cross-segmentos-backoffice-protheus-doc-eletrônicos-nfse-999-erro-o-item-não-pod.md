---
article_id: 360055968933
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3408df68cd2d76e6cdcedb1e7ea126063e0dd0efea08a400b088065f71c2442c
fetched_at: '2026-06-28T22:39:56.268523+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 999 Erro:
  O item não pode ser acrescentado, há mais itens do que é permitido na nota fiscal
  (Mogi das Cruzes)'
type: support-article
updated_at: '2025-07-14T21:42:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055968933-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-999-Erro-O-item-n%C3%A3o-pode-ser-acrescentado-h%C3%A1-mais-itens-do-que-%C3%A9-permitido-na-nota-fiscal-Mogi-das-Cruzes
---

**Ocorrência**Ao realizar a transmissão de um RPS com vários itens ocorre a seguinte rejeição: **"999 Erro: O item não pode ser acrescentado, há mais itens do que é permitido na nota fiscal".**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**   
Essa rejeição ocorre pois no XML estão sendo informados mais itens do que o máximo permitido pela prefeitura.  
A informação é que **a prefeitura de Mogi das Cruzes aceita até 19 itens por nota**, acima disso ocorre a rejeição.  
  
**Solução**Portanto para a correção deverá informar no máximo 19 itens ao preparar o documento.  
  
*Obs.: Vale lembrar que a prefeitura poderá alterar em qualquer momento essa quantidade máxima e em todos os casos ela será a responsável por informar a quantidade máxima de itens por nota.*
