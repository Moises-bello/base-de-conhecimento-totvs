---
article_id: 11903788666775
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 40c43989835d63ff97c166b9a0e1b56ddc83a54ff351a8c52336be4118f4adbc
fetched_at: '2026-06-28T22:42:09.024476+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 44 da DAPI?
type: support-article
updated_at: '2023-01-24T18:08:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11903788666775-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-44-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a linha **44 - Vendas**  da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 44 - Vendas** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 44,** no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5101/5102/5103/5104/5105/5106/5111/5112/5113/5114/5115/5116/5117/5118/5119/5120/5122/5123/5124/5125/5401/5402/5403/5405/5501/5502/5651/5652/5653/5654/5655/5656/5933**
