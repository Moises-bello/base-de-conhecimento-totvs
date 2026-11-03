---
content_hash: 7c0a92f1b9fa43ca77f022b95bc6ad6b340100a471dccac5e06eb2e5fcd56a37
fetched_at: '2026-06-29T00:10:01.497243+00:00'
page_id: '452718755'
product: rm
source: tdn-rm
title: Rateio Fixo
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+Fixo
version: 3
---

A informação dos percentuais ou valores de rateios fixos conforme parametrização "Utiliza Cálculo por Centro de Custo" para cada centro de custo onde o funcionário trabalhou durante o mês será utilizada para que o sistema faça o rateio durante o cálculo por centro de custo.  
   
Deve-se informar o percentual de rateio fixo no qual o funcionário trabalhou em determinado centro de custo. A soma dos percentuais deverá ser igual a 100%, já que, para o cálculo o sistema dividirá por 100.   
   
Caso o parâmetro "Rateio fixo por valor" estiver marcado, o campo acima será renomeado para "Valor" e deverão ser informados valores brutos para se chegar aos percentuais usados no rateio.   
   
**Exemplo:**  
O rateio fixo do funcionário está preenchido com os seguintes dados:  
   
Centro de Custo Valor  
XXXX   54,00  
YYYY   66,00  
Total do Rateio  120,00  
   
Ao ratear um evento com o valor de R$29,68, o sistema fará o seguinte cálculo:  
Centro de custo XXXX = R$29,68 \* 54 / 120 = 13,36  
Centro de custo YYYY = R$29,68 \* 66 / 120 = 16,32  
   
**Observação:**  
1) O sistema somente fará consistência na soma dos percentuais dos rateios fixos para ser igual a 100%, caso o parâmetro "Rateio fixo por valor" NÃO estiver marcado.

2) Os Centros de Custos que tiverem a opção 'Ativo', desmarcado, ou seja, que estejam inativos não serão apresentados na tela de cadastro de 'Rateios Fixos'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
