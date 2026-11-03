---
article_id: 8978813105175
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 90209b8a78c6c15d1ee7af710cfc99ba1477761918cc1727dd200956c8c272c9
fetched_at: '2026-06-28T22:42:08.938446+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 022 da DAPIMG?
type: support-article
updated_at: '2022-09-19T17:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8978813105175-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-022-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 022 - Ativo Permanente** da **DAPIMG**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

A linha **22 - Ativo Permanente** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 22**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**: 1406/1551/1552/1553/1554/1555/1604
