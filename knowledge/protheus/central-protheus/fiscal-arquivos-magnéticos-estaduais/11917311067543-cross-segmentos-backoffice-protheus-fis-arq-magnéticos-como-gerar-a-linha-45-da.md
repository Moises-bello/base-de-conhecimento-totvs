---
article_id: 11917311067543
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1932d64edd99b34c3ac919475fee08d84a79e468dbd1a2ee991470df96a72565
fetched_at: '2026-06-28T22:42:09.028916+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 45 da DAPI?
type: support-article
updated_at: '2023-01-25T12:38:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11917311067543-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-45-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha** **45 - Transferência** da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha****45 - Transferência** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 45,**no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5151/5152/5153/5155/5156/5408/5409/5552/5557/5658/5659**
