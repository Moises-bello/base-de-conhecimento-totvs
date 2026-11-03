---
article_id: 11937711116183
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 9af7bbafda0cb44cb3e14d7211e88aa42ee7a397a09bfee4a48ca7fa11af9869
fetched_at: '2026-06-28T22:42:09.056163+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 52 da DAPI?
type: support-article
updated_at: '2024-06-13T17:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11937711116183-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-52-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a linha **52 - Vendas** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 52** **- Vendas** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 52**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**6101/6102/6103/6104/6105/6106/6107/6108/6109/6110/6111/6112/6113/6114/6115/6116/6117/6118/6119/6120/6122/6123/6124/6125/6401/6402/6403/6404/6501/6502/6651/6652/6653/6654/6655/6656**
