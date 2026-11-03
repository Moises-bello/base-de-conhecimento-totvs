---
article_id: 360025646034
category: Escrita Fiscal - Impostos - Funrural
content_hash: 6d82bf0ed7f0e8d3f39c1797e67015444899454d9e0d90ce35a7d6c5cead1da2
fetched_at: '2026-06-28T22:39:28.169954+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: MP - FIS - Documento de Entrada - FUNRURAL - Gravação dos campos F3_OBSERV
  e FT_OBSERV
type: support-article
updated_at: '2021-04-28T21:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025646034-MP-FIS-Documento-de-Entrada-FUNRURAL-Grava%C3%A7%C3%A3o-dos-campos-F3-OBSERV-e-FT-OBSERV
---

**Dúvida**Ao incluir um Documento de entrada, ref. a produtor rural, quando existe o calculo de FUNRURAL (D1\_VALFUN > 0), não está sendo gravado o texto "CONT.SEG.SOCIAL: 999,99", com o valor do FUNRURAL, nos campos F3\_OBSERV e FT\_OBSERV.   
  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**

Por padrão só é apresentada as informações se tiver os 3 impostos calculados GILRAT/SENAR/INSS, se um dos impostos não for calculado o sistema não leva a informação para o campos F3\_OBSERV e FT\_OBSERV.  
  
A informação do campo CONT.SEC.SOC é a somatória dos 3 impostos GILRAT/SENAR/INSS  
  
A TOTVS entende que, na verdade, mostrar só parte dos valores lá na observação era um erro, por isso a mudança.
