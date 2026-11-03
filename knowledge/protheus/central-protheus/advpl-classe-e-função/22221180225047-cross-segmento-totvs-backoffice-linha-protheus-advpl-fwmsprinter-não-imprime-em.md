---
article_id: 22221180225047
category: ADVPL - Classe e Função
content_hash: cb19a4952f34872bca3556f620873b561a351c7818fcc9cb98d4db0ff3390f68
fetched_at: '2026-06-28T22:40:14.180740+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - FWMsPrinter não
  imprime em paisagem
type: support-article
updated_at: '2024-03-20T20:14:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22221180225047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWMsPrinter-n%C3%A3o-imprime-em-paisagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22221153425559) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**A classe FWMsPrinter não está imprimindo em paisagem

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão P12

**Solução**

Para que a classe FWMsPrinter imprima em paisagem é necessário que não tenha um tamanho customizado na folha, ou seja, *SetPaperSize* diferente de 0, feito isso basta utiliza o método *SetLandScape* e antes de iniciar a impressão utilizar o método *StartPage* e ao finalizar a página o método *EndPage.*

Nos casos em que utilizar o *SetPaperSize* como 0 deve definir a orientação da folha no próprio tamanho customizado, pois os métodos *SetPaperSize* e*SetPortrait* são ignorados*.*

**Saiba mais**  
[FWMsPrinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter)

[Erros Comuns Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21711171003031)
