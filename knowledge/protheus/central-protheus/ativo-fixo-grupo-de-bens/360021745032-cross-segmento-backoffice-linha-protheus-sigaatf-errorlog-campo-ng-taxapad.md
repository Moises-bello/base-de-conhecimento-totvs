---
article_id: 360021745032
category: Ativo Fixo - Grupo de Bens
content_hash: e33dfbd6635288f6fddd519326d6bf78d74c1c510d23bf97e2309bdc459eb31a
fetched_at: '2026-06-28T22:41:41.083508+00:00'
product: protheus
section_id: 1500001536521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Error.log campo NG_TAXAPAD
type: support-article
updated_at: '2022-06-08T14:04:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021745032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Error-log-campo-NG-TAXAPAD
---

**Ocorrência**No módulo do Ativo Fixo, ao incluir um novo Bem é gerado o error

"THREAD ERROR ([5008], usuario.totvs, TOT10) 14/01/2019 10:55:50   
O campo NG\_TAXAPAD refira à pasta:3, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW) 23/10/2018 18:06:50 line : 405"

**Ambiente**Microsiga - Protheus - A partir da versão 11.80  
  
**Causa**Este incidente ocorre, pois o campo NG\_TAXAPAD não está marcado como 'Usado', ou o campo não existe no Dicionário de Dados Protheus.

**Solução**Para solucionar essa ocorrência, é necessário atualizar o Dicionário de Dados, efetuando  o download dos dicionários (Completo e Diferencial)

**Veja mais**

[MP -SIGACTB - Como realizar a atualização do ambiente no Microsiga Protheus 12?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006655452-MP-SIGACTB-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ambiente-no-Microsiga-Protheus-12-?source=search)
