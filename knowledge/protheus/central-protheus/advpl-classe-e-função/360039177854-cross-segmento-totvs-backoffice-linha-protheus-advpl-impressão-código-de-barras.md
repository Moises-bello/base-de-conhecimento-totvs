---
article_id: 360039177854
category: ADVPL - Classe e Função
content_hash: 3a8070a2926a2ad725b9f0478a5e755e8ddce70a36476f2ab9857488c221d9c0
fetched_at: '2026-06-28T22:40:16.927173+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão código
  de barras classe FWMSPrinter e TMSPrinter
type: support-article
updated_at: '2021-09-30T21:15:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039177854-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-c%C3%B3digo-de-barras-classe-FWMSPrinter-e-TMSPrinter
---

**Ocorrência**Utilização das classes TMSPrinter e FWMSPrinter para impressão de códigos de barras.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23

**Solução**A classe **TMSPrinter**(classe do binário) esta depreciada, a partir do release 12.1.23 em seu lugar foi inclusa a classe **FwMsPrinter**(classe de Framework).

A nova classe **FwMsPrinter**() contém algumas melhorias como ajustes para melhor posicionamento e impressão dos dados, vale destacar também que a classe **FwMsPrinter** não herda da classe **TmsPrinter**.

Como são classes distintas, o comportamento não é exatamente mesmo, o que pode levar a diferenciações na impressão como dimensionamento de códigos de barras diferentes entre as classes.  
uma observação importante é que as classes FwMsPrinter e TmsPrinter não são homologadas para impressão em impressoras térmicas para impressoras deste tipo deve-se utilizar [MSCBPrinter](https://tdn.totvs.com/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557).

**Saiba mais**[MSCBPrinter](https://tdn.totvs.com/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557)
