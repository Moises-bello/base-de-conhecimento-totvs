---
article_id: 11497205126807
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7388c51ed034de43ae618ea1617e82c5ba95cc065d7aa6ac0f4fc6bb0373a4f4
fetched_at: '2026-06-28T22:42:08.964324+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 27 da DAPI?
type: support-article
updated_at: '2023-01-09T12:18:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11497205126807-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-27-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a **linha 027 - Transferência** da **DAPI?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **linha 027 - Transferência** é gerada com base nos valores totais das operações do período lançadas no livro **Registro de Entradas** com as **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 23**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**2151/2152/2153/2154/2408/2409/2658/2659.**
