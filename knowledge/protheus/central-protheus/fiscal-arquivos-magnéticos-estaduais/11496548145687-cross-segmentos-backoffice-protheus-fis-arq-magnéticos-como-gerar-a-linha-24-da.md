---
article_id: 11496548145687
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8106cd2a78ca150fa6c8b2b3fb19c421cac68feda19ac72f735350a92a18453c
fetched_at: '2026-06-28T22:42:08.956338+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 24 da DAPI?
type: support-article
updated_at: '2023-01-09T13:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11496548145687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-24-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**  
Como gerar a **linha 024 - Outras** da **DAPIMG?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **linha 024 - Outras** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 24**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**1414/1415/1451/1452/1901/1902/1903/1904/1905/1906/1907/1908/1909/1910/1911/1912/1913/1914/1915/1916/1917/1918/1919/1920/1921/1922/1923/1924/1925/1926/1663/1664/1949/1934**
