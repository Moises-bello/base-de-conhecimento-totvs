---
article_id: 20760770348951
category: ADVPL - Classe e Função
content_hash: a1cd9981a4a3faf6b25ad58c0eadc10d684a0300cfa361310ff57762d8cc8cb0
fetched_at: '2026-06-28T22:40:20.637311+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  É possível alterar
  orientação em tempo de execução FWMSPrinter ??
type: support-article
updated_at: '2024-01-22T14:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20760770348951-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-alterar-orienta%C3%A7%C3%A3o-em-tempo-de-execu%C3%A7%C3%A3o-FWMSPrinter
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20760770321047) Tempo aproximado para leitura: **01:00:00 min**

**Dúvida**É possível alterar a orientação do relatório (paisagem, retrato) em tempo de execução?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as Versões  
  
**Solução**

Não é possível efetuar este tipo ação, uma vez definido a propriedade de orientação através dos métodos **SetPortrait** ou **SetLandscape** são definidas por impressão e não por página.

**Observação**

Caso utilize o **SetPaperSize** como 0, ele irá desconsiderar os **metódos (SetPortrait, SetLandscape),** e a impressão será pelo tamanho definido pelo usuário, o tamanho será customizável informando em nHeigth/nWidth.

**Saiba Mais:  
[FWMsPrinter](https://tdn.totvs.com/display/PROT/FWMsPrinter)**
