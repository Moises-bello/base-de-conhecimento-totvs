---
article_id: 11937442764695
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c130967505926540a05db31dd1989fb831ea6bc67ceaf718b3e5d2a97557e9c7
fetched_at: '2026-06-28T22:42:09.046080+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 49 da DAPI?
type: support-article
updated_at: '2024-06-13T17:44:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11937442764695-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-49-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Linha** **49 - Transporte** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha** **49 - Transporte**é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 49**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5351/5352/5353/5354/5355/5356/5357/5359/5360**
