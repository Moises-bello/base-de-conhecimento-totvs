---
article_id: 8864103514775
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ac28d29916cb76f5a01434b0778b63aae18d3f363491254cf1466421956a7618
fetched_at: '2026-06-28T22:42:08.923985+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 018 da DAPIMG?
type: support-article
updated_at: '2022-09-14T12:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8864103514775-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-018-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a linha 018 da DAPIMG?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

A linha 18 - - Devolução da **DAPI MG** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 18**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs:**

1201/1202/1203/1204/1205/1206/1207/1208/1209/1410/1411/1503/1504/1660/1661/1662
