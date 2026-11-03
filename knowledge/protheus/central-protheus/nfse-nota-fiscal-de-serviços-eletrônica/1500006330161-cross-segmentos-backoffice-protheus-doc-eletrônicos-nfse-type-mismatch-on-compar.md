---
article_id: 1500006330161
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 354632e90510df037f004b23861d5cab2d168ba01ecb711e3c88212d20c046c7
fetched_at: '2026-06-28T22:39:58.612334+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - type mismatch
  on compare  on PREST(NFSEXMLENV.PRW) DD/MM/2021 HH:MM:SS line : XXXX'
type: support-article
updated_at: '2022-01-11T16:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006330161-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-type-mismatch-on-compare-on-PREST-NFSEXMLENV-PRW-DD-MM-2021-HH-MM-SS-line-XXXX
---

**Ocorrência**Ao realizar a transmissão de um RPS, é apresentado o error.log: ***"type mismatch on compare on PREST(NFSEXMLENV.PRW) DD/MM/2021 HH:MM:SS line : XXXX".*****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Causa**O error.log em questão ocorre exclusivamente quando o **rdmake NFSEXMLENV for de data igual ou superior a 24/02/2021.**Isto é causado por conta do rdmake utilizar uma função (fisGetTel) de um fonte fiscal (MATA950), a qual sofreu algumas alterações e o rdmake necessitava desse fonte MATA950 também atualizado (*igual ou superior a data 27/10/2020).*  
  
Após ajustes, foi corrigido o rdmake NFSEXMLENV para que não ocorra o error.log, **independente da data que estiver utilizando no fonte MATA950.**  
  
**Solução**Portanto, para correção deverá utilizar o último rdmake disponível:  
- [Download rdmake NFSEXMLENV](https://suporte.totvs.com/portal/p/10098/download#detail/1031443)
