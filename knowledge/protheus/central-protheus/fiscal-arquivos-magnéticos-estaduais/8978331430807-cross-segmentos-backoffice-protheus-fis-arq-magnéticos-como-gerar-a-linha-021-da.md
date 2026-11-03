---
article_id: 8978331430807
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 00c765f600a02b6ff679b372c698ae4a6f135307b44ed22aeb23f67a615a0f10
fetched_at: '2026-06-28T22:42:08.934199+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 021 da DAPIMG?
type: support-article
updated_at: '2022-09-19T17:02:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8978331430807-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-021-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 021** da **DAPIMG**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

A linha **21 - Transporte** da **DAPI MG** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da  **Linha 21**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**: 1351/1352/1353/1354/1355/1356/1360/1931/1932
