---
article_id: 11551508074903
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: acad19d6cff117d49a81fc950ffdfecbbdb21b9aebe0f8c4560b45062335dd6c
fetched_at: '2026-06-28T22:42:08.976595+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 30 da DAPI?
type: support-article
updated_at: '2023-01-10T12:14:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11551508074903-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-30-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **L****inha 30 - Comunicação** da **DAPIMG?**  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 30 - Comunicação** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha 30**, no campo **Cod. Fiscal - D1\_CF**do lançamento deve conter uma das seguintes **CFOPs**:

**2301/2302/2303/2304/2305/2306**
