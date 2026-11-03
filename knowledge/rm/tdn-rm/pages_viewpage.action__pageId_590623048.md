---
content_hash: a58df11c68327ccf46c0a2005bc8128022b7741ed850d2af0f665d66913d19ed
fetched_at: '2026-06-29T00:10:56.092786+00:00'
page_id: '590623048'
product: rm
source: tdn-rm
title: Parcela fixa em contrato com parcelas calculadas por crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590623048
version: 20
---

---

Na rematrícula dos alunos, é muito comum que as instituições não saibam em quantas disciplinas o aluno irá se matricular, porém a instituição já deve cobrar do aluno um valor para “garantir” essa rematrícula. Para isso, elas criam uma parcela fixa no contrato, com um determinado valor, e mandam para todos os seus alunos efetuarem o pagamento.  
  
Depois da matrícula e o valor total do contrato de acordo com os créditos forem conhecidos, é possível parametrizar para que esse valor seja abatido no valor total do contrato, e o novo valor seja dividido entre as parcelas restantes.  
  
Exemplo: O contrato do aluno possui 6 parcelas. A 1º parcela será fixa em um valor de R$500,00. O aluno se matricula em 5 disciplinas, todas possuem 5 créditos de R$ 100,00.

**Valor total do contrato: 5 (Nº de Créditos por disciplina) x R$100 x 5 (disciplinas) = R$2.500**

Porém o aluno já pagou R$ 500,00, então o sistema deverá abater este valor nos R$ 2.500,00, deixando R$2000,00 para ser dividido entre as 5 parcelas restantes.

Calculando 5 parcelas no valor de R$ 400,00.

Para que o sistema faça isto, o parâmetro “Considerar parcelas fixas na divisão de créditos financeiros entre as parcelas do contrato” deverá ser marcado.

*Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2*

O contrato que possui parcelas com **valor fixo** e parcelas **calculadas por crédito,** e no serviço o parâmetro "Considera parcelas fixas do serviço no cálculo de parcelas por crédito" esteja marcado, o calculado das parcelas por crédito é da seguinte forma:

* **(( Número de crédito da disciplina x Valor de crédito da disciplina ) / ( Total de parcelas calculadas por crédito ) \* Número de disciplinas) - ( Valor da parcela fixa / Total de parcelas calculadas por crédito)**

Perceba que os valores de créditos das disciplinas são cobrados dividindo somente pelas parcelas **calculadas por crédito.**

O cálculo do valor da disciplina por parcela por crédito e parcela fixa, é da seguinte forma:

* Parcelas com valor fixo:
  + **Valor da parcela fixa / Total de parcelas calculadas por crédito**
* Parcelas calculadas por crédito:
  + **( Número de crédito da disciplina x Valor de crédito da disciplina ) / ( Total de parcelas calculadas por crédito )**

**Exemplo 1:**

Contrato com 5 parcelas sendo que 1 parcela com valor fixo e as 4 parcelas por crédito e a disciplina 6 é cancelada.

| Disciplinas | Número de Créditos | Valor de Créditos (R$) | Valor Total da Disciplina (R$) | Valor da Disciplina para a Parcela por Crédito (R$) |
| --- | --- | --- | --- | --- |
| Disciplina 1 | 2 | 99,00 | 198,00 | 49,50 |
| Disciplina 2 | 2 | 99,00 | 198,00 | 49,50 |
| Disciplina 3 | 2 | 99,00 | 198,00 | 49,50 |
| Disciplina 4 | 2 | 99,00 | 198,00 | 49,50 |
| Disciplina 5 | 2 | 99,00 | 198,00 | 49,50 |
| Disciplina 6 | 2 | 99,00 | 198,00 | 49,50 |

| Parcela Fixa | Valor Total da Disciplina (R$) | Número de Parcelas por Crédito | Valor da Disciplina para a Parcela por Crédito (R$) |
| --- | --- | --- | --- |
| 237,60 | 4 | 59,4 |

| Parcela | Valor da parcela (R$) | Tipo da parcela |
| --- | --- | --- |
| 1 | 237,60 | Fixa |
| 2 | 237,60 | Por crédito |
| 3 | 237,60 | Por crédito |
| 4 | 237,60 | Por crédito |
| 5 | 188,10 | Por crédito |

Com o cancelamento da disciplina 6 o valor da parcela 5 será calculada da seguinte forma:

* Valor da parcela - (( Número de crédito da disciplina x Valor de crédito da disciplina ) / (Total de parcelas calculadas por crédito ))

Desta forma, o valor da parcela 5 será:

    237,60 - ((2 x 99) / 4)   
    237,60 - (198 / 4)  
    237,60 - 49,50 = 188,10

**Exemplo 2:**

Contrato com 5 parcelas sendo que as 5 parcelas são9 por crédito e a disciplina 6 é cancelada.

| Disciplinas | Número de Créditos | Valor de Créditos (R$) | Valor Total da Disciplina (R$) | Valor da Disciplina para a Parcela por Crédito (R$) |
| --- | --- | --- | --- | --- |
| Disciplina 1 | 2 | 99,00 | 198,00 | 39,60 |
| Disciplina 2 | 2 | 99,00 | 198,00 | 39,60 |
| Disciplina 3 | 2 | 99,00 | 198,00 | 39,60 |
| Disciplina 4 | 2 | 99,00 | 198,00 | 39,60 |
| Disciplina 5 | 2 | 99,00 | 198,00 | 39,60 |
| Disciplina 6 | 2 | 99,00 | 198,00 | 39,60 |

| Parcela | Valor da parcela (R$) | Tipo da parcela |
| --- | --- | --- |
| 1 | 237,00 | Por crédito |
| 2 | 237,00 | Por crédito |
| 3 | 237,00 | Por crédito |
| 4 | 237,00 | Por crédito |
| 5 | 198,00 | Por crédito |

Com o cancelamento da disciplina 5 o valor da parcela 5 será calculada da seguinte forma:

* Valor da parcela -  (( Número de crédito da disciplina x Valor de crédito da disciplina ) / ( Total de parcelas calculadas por crédito ))

Desta forma, o valor da parcela 5 será:  
       237,60 - ((2 x 99) / 5)  
       237,60 - (198 / 5)  
       237,60 - 39,60 = 198,00

Quando existe abatimento ou aumento em alguma disciplina, a parcela fixa não é somada ao número de parcelas para cálculo e divisão do valor a ser abatido, pois o valor da disciplina não influência no valor da parcela fixa, somente em parcelas calculadas por crédito.
