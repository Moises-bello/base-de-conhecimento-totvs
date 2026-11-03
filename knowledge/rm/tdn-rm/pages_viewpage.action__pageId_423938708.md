---
content_hash: b71cf651c08ff0d55b65169e604a44ecee21e1fcfc3442e3765b6f692d4290f6
fetched_at: '2026-06-29T00:09:28.564758+00:00'
page_id: '423938708'
product: rm
source: tdn-rm
title: 'Exemplos de Recálculo do 2º Valor:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938708
version: 2
---

O 2º Valor é calculado levando-se em consideração o Valor do Lançamento, a Data e a Cotação cadastrada para a Moeda utilizada no processo.  
A seguir, alguns cenários para exemplificar o Recálculo do 2º Valor:

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
Data do lançamento:   20/01/2012  
Valor do Lançamento: R$ 1.000,00  
Data 2ª Moeda:          01/01/2012  
   
Cotação da Moeda:   
01/01/2012 = 1,02  
15/01/2012 = 1,05  
30/01/2012 = 1,08  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **marcada**:   
2º Valor = (1.000,00 / 1,05) = **952,38**  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **desmarcada**:   
2º Valor = (1.000,00 / 1,02 'data 2ª moeda') = **980,39**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
   
Data do lançamento:   20/01/2012  
Valor do Lançamento: R$ 1.000,00  
Data 2ª Moeda:          01/01/2012  
   
Cotação da Moeda:   
31/12/2011 = 1,07  
30/01/2012 = 2,01  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **marcada**:   
2º Valor = (1.000,00 / 1,07) = **934,58**  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **desmarcada**:   
2º Valor = (1.000,00 / 1,07 'data 2ª moeda') = **934,58**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
   
Data do lançamento:   20/01/2012  
Valor do Lançamento: R$ 1.000,00  
Data 2ª Moeda:          01/01/2012  
   
Cotação da Moeda:   
30/01/2012 = 2,05  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **marcada**:   
2º Valor = (1.000,00 / 2,05) = **487,80**  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **desmarcada**:   
2º Valor = (1.000,00 / 2,05 'data 2ª moeda') = **487,80**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
   
Data do lançamento:   20/01/2012  
Valor do Lançamento: R$ 1.000,00  
Data 2ª Moeda:              
   
Cotação da Moeda:   
15/01/2012 = 1,09  
30/01/2012 = 2,05  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **marcada**:   
2º Valor = (1.000,00 / 1,09) = **917,43**  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **desmarcada**:   
2º Valor = (1.000,00 / 1,09 'data do lançamento') = **917,43**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
   
Data do lançamento:   20/01/2012  
Valor do Lançamento: R$ 1.000,00  
Data 2ª Moeda:              
   
Cotação da Moeda:   
30/01/2012 = 2,05  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **marcada**:   
2º Valor = (1.000,00 / 2,05) = **487,80**  
   
Recálculo do 2º Valor com a opção 'Usa cotação da data do lançamento' **desmarcada**:   
2º Valor = (1.000,00 / 2,05 'data do lançamento') = **487,80**
