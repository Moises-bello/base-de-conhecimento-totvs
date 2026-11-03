---
content_hash: f62e101ee12402432f285930121931b3692dc01732ad96e10166d084a2106920
fetched_at: '2026-06-29T00:09:59.967434+00:00'
page_id: '452718468'
product: rm
source: tdn-rm
title: Fórmulas para Cálculo das Separatrizes na Análise Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718468
version: 30
---

Quando o total de amostras é um número par, o cálculo será:

1o. Quartil:   
(total amostras + 3) / 4 -> Extrai a parte inteira (INT = parte inteira do resultado)  
-> Extrai a parte fracionária (FRAC = parte fracionária)   
Valor 1o. Quartil: VAL\[INT\] + (FRAC\*(VAL\[INT+1\] - VAL\[INT\]))  
   
Mediana:   
Q2 = Total de amostras / 2  
Valor da Mediana: (VAL\[Q2\] + VAL\[Q2+1\]) / 2

3o. Quartil:   
 ((3 \* total de amostras) + 1) / 4 -> Extrai a parte inteira (INT = parte inteira do resultado)  
-> Extrai a parte fracionária (FRAC = parte fracionária)   
Valor 3o. Quartil: VAL\[INT\] + (FRAC\*(VAL\[INT+1\] - VAL\[INT\]))

Quando o total de amostras é um número ímpar, o cálculo será:  
1o. Quartil: (total amostras + 3) / 4  
Mediana : (Total de amostras + 1) / 2  
3o. Quartil: ((3 \* total de amostras) + 1) / 4
