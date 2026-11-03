---
content_hash: ae59f625e412aec998da0eae13be1de925af977bfb9309069e9c535b0f29268d
fetched_at: '2026-06-29T00:10:09.490278+00:00'
page_id: '452719681'
product: rm
source: tdn-rm
title: Código de Cálculo 213 - INSS Descontado RRA 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719681
version: 2
---

É o valor do evento com o código de cálculo 108 - INSS DE DIF SALÁRIAL 13º SALARIO referente as diferenças do ano anterior a competência atual.   
 Este evento é do tipo base de cálculo, sem incidência.   
 Internamente, o sistema considera este código de cálculo no cálculo de IRRF RRA 13º Salário. Tratamento semelhante aos demais INSS quanto ao cálculo de IRRF, ou seja, não precisa incidir para deduzir.  
    
 **Exemplo**  
 Em Junho de 2018 o Funcionário teve um aumento de salário retroativo ao mês 10/2017  
 Executando o processo de Cálculo de Diferença de 13º Salário referente ao período de 2017, com o parâmetro Dissídio 'Sim' marcado.  
 O sistema calculou o evento abaixo:  
 CC 108 - R$ 211,39  
 CC 213 - R$ 211,39  
    
 **Observação**  
 Quando calculada a diferença utilizando o Cálculo de RRA, o valor do evento no campo Valor da Contribuição Prev. Oficial é somado no histórico de RRA vinculado ao funcionário. Esse valor é informado na DIRF, no campo correspondente, e estornando do valor da Contribuição Previdência oficial dos rendimentos sujeitos a tributação exclusiva.   
    
 **Atenção**  
 O sistema somente lança este evento quando a diferença for por dissídio.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
