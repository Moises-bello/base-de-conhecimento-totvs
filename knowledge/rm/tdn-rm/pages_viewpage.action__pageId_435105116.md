---
content_hash: 706994bb745aa3b4551cd85dd8f9ac435c8b462cf3aaeeb0e855c832fce8a1c6
fetched_at: '2026-06-29T00:09:47.986463+00:00'
page_id: '435105116'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Exemplos da aplicação do cálculo pro rata
  para aditivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105116
version: 4
---

**Exemplos da aplicação do Cálculo Pro Rata para Aditivos**    
Para utilizar o Rateio (Pró Rata) no Aditivo é necessário que o campo Modelo de Cálculo esteja com a opção "Utiliza Cálculo Pro Rata".   
Para os períodos de parcelas **Inicial**e **Final**o sistema utilizará **Mês Civil** e para os períodos das outras parcelas será usado o **Mês Comercial**.  
**Qual a diferença entre Mês Civil e Mês Comercial?**  
**Mês Civil:** Expressão existente no mercado financeiro e administrativo que considera todos os dias do mês, da forma real mesmo. Por exemplo, em fevereiro teremos 28 ou 29 dias. Sendo assim, o **Ano Civil** é considerado com 365 dias.  
**Mês Comercial:** Considera que todos os meses tenham 30 dias, com isso, o **Ano Comercial**é considerado com 360 dias.  
Nos parâmetros gerais do TOTVS Incorporação, temos o parâmetro "**Considerar para o cálculo Pro Rata o dia após a data do aditivo".** Quando desmarcado ele considera que a ação do aditivo no Contrato de Locação acontece no dia da data do aditivo. Segue um exemplo:   
**Exemplo de Aditivo:**  
Pra facilitar a conta vamos considerar um aluguel de R$30.000,00 ( do dia 1 a 30) (30.000,00/30 = 1.000,00 por dia). Com período de vigência de 01/01/2018 até 31/12/2018  
Se tiver um aditivo no dia 15/09/2018  alterando o valor de locação para 35.000,00 (35.000,00/30 = 1.166,66 por dia) De 01 a 14/09 = (14 \* 1.000,00) = R$14.000,00 De 15 a 30/09 = (16 \* 1.166,66) = R$18.666,56 Aluguel total no período de 01 a 30/09/2018 = R$15.000,00 +  R$18.666,56 = R$ 32.666,56  
As demais parcelas terão o valor de R$ 35.000,00, conforme definido no aditivo.   
Quando o parâmetro estiver marcado, a ação do aditivo no Contrato de Locação acontece no um dia após a data do aditivo. Segue um exemplo:   
Pra facilitar a conta vamos considerar um aluguel de R$30.000,00 ( do dia 1 a 30) (30.000,00/30 = 1.000,00 por dia). Com período de vigência de 01/01/2018 até 31/12/2018  
Se tiver um aditivo no dia 15/09/2018  alterando o valor de locação para 35.000,00 (35.000,00/30 = 1.166,66 por dia) De 01 a 15/09 = (15 \* 1.000,00) = R$15.000,00 De 15 a 30/09 = (15 \* 1.166,66) = R$17.499,90 Aluguel total no período de 01 a 30/09/2018 = R$15.000,00 + R$17.499,90 = R$ 32.499,90  
Quando o valor cobrado no mês é dividido por 30 dias significa que está sendo considerado Mês Comercial ("Chama-se ano comercial o período de tempo em que se considera que o ano tem 360 dias e cada um dos meses 30 dias, indistintamente. É utilizado na contabilidade e também na matemática financeira com o objetivo de simplificar os cálculos com datas.")  Quando o cálculo é feito usando exatamente a quantidade de dias do mês chamado Mês Civil ("Mês civil é uma expressão usada no mercado financeiro e administrativo. Considera todos os dias existentes no mês em questão (por exemplo: se estamos em fevereiro, teremos 28 ou 29 dias, etc.).  
Para ver o log do  aditivo realizado, basta acessar o **Contrato de Locação / Parcelas do Contrato de Locação** e abrir a parcela com um clique duplo. Na Memória de cálculo serão mostrados todos os detalhes do cálculo realizado

|  |  |
| --- | --- |
|  | Veja Também |

---

Parcelas do Contrato Aditivos
