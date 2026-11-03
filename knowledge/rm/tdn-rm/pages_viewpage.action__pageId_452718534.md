---
content_hash: 2a5ee2d307d8d381d8e1f019037ff399247ae5c87ef036d9b0a50d32df031620
fetched_at: '2026-06-29T00:10:00.411298+00:00'
page_id: '452718534'
product: rm
source: tdn-rm
title: 'Exemplo:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718534
version: 1
---

**Exemplo:**   
Para os Funcionários autônomos cadastrados no RM Labore e com categoria 15, o sistema irá calcular automaticamente 2,5% do valor da remuneração paga ou creditada a transportador autônomo pelo carreto no evento de CC46. Porém, o usuário deverá lançar neste evento 20% sobre o valor sujeito à contribuição previdenciária e para terceiros.  
   
**Sugestão:**  
O usuário poderá criar um evento base de cálculo para informar a base do transportador autônomo e lançar na movimentação do funcionário. E no evento com código de cálculo 46 poderá informar a fórmula abaixo para realizar o cálculo automático:  
   
*se c('9999')>0 entao (C('9999')) \* 0.20 senao c('0046') fimse*  
   
Sendo que 9999 é o evento base de cálculo e evento 0046 é o evento de CC46.  
   
**Atenção:**  
Para cálculo da GPS do transportador autônomo, o sistema verifica se a categoria do funcionário é igual a 15 e automaticamente multiplica o valor informado na movimentação do funcionário com código de cálculo 46 por 2,5%.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Rotinas Mensais - Anuais
