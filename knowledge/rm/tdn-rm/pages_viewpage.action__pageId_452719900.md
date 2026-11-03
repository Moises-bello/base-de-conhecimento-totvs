---
content_hash: d3d2d8849196e71b99036538fa305f22377ff9bde597b74a45a1cc6d50ff8a3e
fetched_at: '2026-06-29T00:10:10.666193+00:00'
page_id: '452719900'
product: rm
source: tdn-rm
title: Código de Cálculo 209 - INSS Descontado RRA Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719900
version: 2
---

É o valor do evento com o código de cálculo 110 - INSS DE DIF SALÁRIAL DE FÉRIAS referente as diferenças do ano anterior a competência atual.   
 Este evento é do tipo base de cálculo, sem incidência.   
 Internamente, o sistema considera este código de cálculo no cálculo de IRRF RRA de Férias. Tratamento semelhante aos demais INSS quanto ao cálculo de IRRF, ou seja, não precisa incidir para deduzir.  
    
 **Exemplo**  
 Funcionário com cálculo de férias em 01/10/2017 a 30/10/2017  
 Em Junho de 2018 o Funcionário teve um aumento de salário retroativo ao mês 10/2017  
 Executando o processo de Cálculo de Diferença de Férias referente ao período de 2017, com o parâmetro Dissídio 'Sim' marcado.  
 O sistema calculou o evento abaixo:  
 CC 110 - R$ 18,97  
 CC 209 - R$ 18,97  
    
 **Observação**  
 Quando calculada a diferença utilizando o Cálculo de RRA, o valor do evento no campo Valor da Contribuição Prev. Oficial é inserido no histórico de RRA vinculado ao funcionário. Esse valor é informado na DIRF, no campo correspondente, e estornando do valor da Contribuição Previdência oficial dos rendimentos tributáveis.   
    
 **Atenção**

* O sistema somente lança este evento quando a diferença for por dissídio. Isto porque, quando não for por dissídio, consideramos que o usuário optou em calcular o INSS de Férias observando a base da competência atual, assim o Cálculo de IRRF de Férias não será deduzido o valor de INSS de férias.
* Caso o Funcionário tenha dois períodos de gozo de férias para serem recalculados as diferenças e um deles foi calculado no ano atual, mesmo com o parâmetro marcado no parametrizador, não é considerado o valor do desconto de INSS Dif Salarial de férias correspondente ao período de gozo do ano atual.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
