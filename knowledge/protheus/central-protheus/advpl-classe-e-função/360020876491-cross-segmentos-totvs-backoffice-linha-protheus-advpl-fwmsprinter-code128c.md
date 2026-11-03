---
article_id: 360020876491
category: ADVPL - Classe e Função
content_hash: 23cbea2bd16cb3e964ae2f0db8bc77915d59557b1bd2dd2bb0d5fbdde7837c1d
fetched_at: '2026-06-28T22:40:19.507663+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FWMsPrinter CODE128C
type: support-article
updated_at: '2022-01-11T14:42:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020876491-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWMsPrinter-CODE128C
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao utilizar uma sequencia de caracteres, e utilizando o método code128c não está trazendo a numeração correta:

```
oPrinter:Code128C(500, 10, '223680010001', 40)
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Causa**De acordo com as normas técnicas o code128C (Conjunto de Códigos C) - 00-99 (codifica dois dígitos com um único ponto de código) e FNC1 , ou seja quando um numero não tiver um par será acrescentado um digito.  
  
**Solução**Neste caso para utilização de 11 caractere utilize um método Code128:

```
Exemplo  
 oPrinter:Code128(470/*nRow*/ ,30/*nCol*/,'22368001001'/*cCode*/,1/*nWidth*/,50/*nHeigth*/,.T./*lSay*/,,250)
```

**Saiba mais**  
[FWMsPrinter](http://tdn.totvs.com/display/PROT/FWMsPrinter)  
[GS1 Brasil](https://www.gs1br.org/codigos-e-padroes/codigo-de-barras/gs1-128)
