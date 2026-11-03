---
article_id: 360026471371
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2507475be692ff8d7aec894284e4a549af94f0c3d9915547d3f4c6793e4bd293
fetched_at: '2026-06-28T22:42:10.700169+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DCTF - Valores
  de PCC duplicados no arquivo. '
type: support-article
updated_at: '2022-08-18T14:16:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026471371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DCTF-Valores-de-PCC-duplicados-no-arquivo
---

**Ocorrência**Os valores de PCC estão sendo duplicados no arquivo.   
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.7

**Causa**  
Esta situação ocorre quando é utilizada uma mesma natureza financeira para impostos diferentes.

**Solução**Para solução desta ocorrência, deve-se utilizar uma outra natureza num dos parâmetros **MV\_COFINS**, **MV\_PISNAT** e **MV\_CSLL** para que cada um dos impostos de PCC seja gerado com uma natureza diferente, pois se em seu ambiente possuir mais de um titulo com código de retenção diferente, deverá ser tratado em uma natureza diferente para não ocorrer este problema.

Também é possível, caso tenha PCC no titulo, fazer a aglutinação dos mesmos e assim gerar com uma natureza unica, e não ocorrerá o problema.

A aglutinação do PCC pode por exemplo ser realizada pela rotina **FINA378** ou similar, onde o titulo será gravado com o prefixo tipo **AGP** (**Para IR grava AGL**), no caso só haverá 1 titulo para 1 natureza, pois não se pode ter 2 títulos para 1 natureza. É possível após esse titulo de aglutinação, fazer a **DARF** para os títulos.
