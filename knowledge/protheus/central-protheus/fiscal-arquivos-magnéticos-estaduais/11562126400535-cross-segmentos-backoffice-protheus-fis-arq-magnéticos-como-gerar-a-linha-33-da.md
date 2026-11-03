---
article_id: 11562126400535
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: b202dfa5195f64f58c44415e67ced884b3b14a53e82b50f45112a00ab02de35f
fetched_at: '2026-06-28T22:42:08.989779+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 33 da DAPI?
type: support-article
updated_at: '2023-01-10T18:43:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11562126400535-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-33-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **L****inha 33 - Uso e Consumo** da **DAPIMG?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **Linha 33 - Uso e Consumo** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicos.

Para que o valor de um documento fiscal componha os valores da **Linha 33**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**2406/2551/2552/2553/2554/2555**

ou

O campo **D1\_CF** contenha 2653 e na TES os campos**Credita ICMS** (**F4\_CREDICM**) preenchido com **Não** e o campo**Material de Consumo** (**F4\_CONSUMO**) Preenchido com **Sim.**
