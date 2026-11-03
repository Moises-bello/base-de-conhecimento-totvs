---
article_id: 1500002651562
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8285af45da9d89b4ae5c6910d8e3480b26e34b0e33b2757fabc9f3a43b62cbc0
fetched_at: '2026-06-28T22:39:58.614645+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - type mismatch
  on compare on U_NFSEXMLENV(NFSEXMLENV.PRW)
type: support-article
updated_at: '2025-08-22T17:30:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002651562-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-type-mismatch-on-compare-on-U-NFSEXMLENV-NFSEXMLENV-PRW
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre o error.log *"**type mismatch on compare on U\_NFSEXMLENV(NFSEXMLENV.PRW) DD/MM/AAAA HH:MM:SS line : XXX".***  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse erro ocorre por conta de algumas alterações de variáveis (inclusão e ordem) que foram realizadas no fonte do Protheus (FISA022), incluindo também o rdmake NFSEXMLENV **a partir da data de 09/07/2020.**  
  
**Solução**Geralmente nesses casos o FISA022 já está atualizado no ambiente, portanto para correção do problema o rdmake NFSEXMLENV também deverá estar para funcionar corretamente.  
Sendo assim se faz necessário que seja utilizado a última versão **através do link abaixo:**- *[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152109)*
