---
article_id: 360044225913
category: ADVPL - Classe e Função
content_hash: 1d59114a3c99875983ff8698f87c1d59bd55f451a94b94e5515b7f372ec9b373
fetched_at: '2026-06-28T22:40:16.929943+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão de Código
  de barras Alfanumérico FWMSPrinter
type: support-article
updated_at: '2021-10-01T18:38:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044225913-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-de-C%C3%B3digo-de-barras-Alfanum%C3%A9rico-FWMSPrinter
---

**Dúvida**Qual método para impressão de código de barras Alfanumérico na Classe *FWMSPrinter*, pois o método Code128C só imprime números.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**O método que realiza a geração do código de barras contendo letras e caracteres especiais é a code128B.  
Os parâmetros são os mesmos do método **code128C** já publicado na documentação da *FWMSPrinter* no tdn com o método **code128B**.

Ex.:

Local cCODE128 :="111111111111111111111111111111M111111"

oPrinter := FwMsPrinter():New("code.rel", 6, .F., Nil, .T., NIL, NIL, NIL, NIL, NIL, .F., NIL)

oPrinter:StartPage()

oPrinter:Code128B(500, 10, cCODE128 , 40)

**Saiba mais**[**FWMSPRINTER**](https://tdn.totvs.com/display/public/mp/FWMsPrinter)
