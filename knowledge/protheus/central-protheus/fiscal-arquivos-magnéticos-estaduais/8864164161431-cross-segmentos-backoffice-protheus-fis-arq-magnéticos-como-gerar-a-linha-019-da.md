---
article_id: 8864164161431
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: aa89d800f704dfaca0904b76d9ea7b4f986b7f459e4362d9d201411315669fb2
fetched_at: '2026-06-28T22:42:08.927100+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 019 da DAPIMG?
type: support-article
updated_at: '2022-09-14T12:04:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8864164161431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-019-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 019** da **DAPIMG**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

A linha **19 - Energia Elétrica** da **DAPI MG** é gerada com base nos valores totais das operações do período lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 19**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

1251/1252/1253/1254/1255/1256/1257
