---
content_hash: 16f9d86927a4e230c0e2f2651b6af98933172cc5763f54834756e51876b5abfb
fetched_at: '2026-06-29T00:10:09.443114+00:00'
page_id: '452719669'
product: rm
source: tdn-rm
title: Código de Cálculo 212 - Base IRRF RRA 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719669
version: 2
---

É a soma das Bases de IRRF 13º Salário sobre a diferença de 13º Salário processada, somente quando a diferença for referente ao ano anterior, considerando que o cálculo é executado no ano atual.   
 Este evento é do tipo base de cálculo, valor e com incidência de desconto em "Estorna IRRF 13º".  
    
 **Exemplo**  
 Em Junho de 2018 o Funcionário teve um aumento de salário retroativo ao mês 10/2017  
 Executando o processo de Cálculo de Diferença de 13º Salário referente ao período de 2017  
 O sistema calculou os eventos abaixo:  
 CC 180 - R$ 3.200,88  
 CC 212 - R$ 3.200,88  
    
 **Observação**  
 É necessário que o parâmetro "Utiliza Cálculo RRA" esteja marcado no Parametrizador em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Folha Normal | Geral para que o sistema calcule a base de IRRF RRA de 13º Salário.  
 Quando calculado a diferença utilizando o Cálculo de RRA, é somado no histórico de RRA vinculado ao funcionário, o valor do evento no campo Valor Total Rend. Tributável, que é informado na DIRF no campo correspondente e deduzido base de rendimentos sujeitos a tributação exclusiva.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
