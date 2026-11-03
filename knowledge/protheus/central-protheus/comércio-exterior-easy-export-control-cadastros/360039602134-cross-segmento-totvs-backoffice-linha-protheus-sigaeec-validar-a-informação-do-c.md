---
article_id: 360039602134
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 997df5ccc6eec5bac34a9c0a97d62648ff833188519d50c8470730c9f3ac08d4
fetched_at: '2026-06-28T22:36:57.297032+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC -  Validar a informação
  do campo EXL_MDFR "Moeda do Frete"
type: support-article
updated_at: '2021-08-25T17:47:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039602134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Validar-a-informa%C3%A7%C3%A3o-do-campo-EXL-MDFR-Moeda-do-Frete
---

**Dúvida**Validar a informação do preenchimento do campo EXL\_MDFR "Moeda do Frete".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**Na despesa internacional (frete, como exemplo, mas vale para todas), quando são informados os campos "Valor Desp." (EXL\_VDFR) e "Frete Intl." (EEC\_FRPREV) com o mesmo valor e a "Paridade" (ELA\_PAFR) igual a 1, deixando a "Moeda do Frete" (EXL\_MDFR) vazia, o sistema entende que a moeda da despesa internacional é a mesma do processo, gerando o câmbio com esta moeda para a despesa internacional.

Caso queira validar a informação do campo "Moeda do Frete" (EXL\_MDFR) com o preenchimento do campo "Data do Embarque", sugerimos a customização com a criação de uma validação de usuário para o campo, consistindo esta informação. Caso queira customizar a confirmação final do processo, impedindo que a gravação do embarque com a data de embarque preenchida ocorra, sugirerimos o uso do ponto de entrada EECPEM36 -[EECPEM36 - Embarque de Exportação - Botão OK](https://tdn.totvs.com/pages/releaseview.action?pageId=6808326)
