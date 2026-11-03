---
content_hash: 66463d785308a99c8653afb7bcdd68c6b96e69c5ad1ad2797bc50feabc2b914a
fetched_at: '2026-06-29T00:10:53.113672+00:00'
page_id: '576600034'
product: rm
source: tdn-rm
title: Período de Competência Contábil na Bolsa - Exemplo 3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=576600034
version: 16
---

---

Contabilização de contrato com as seguintes cenários:

* Uma bolsa com compendia informada período 02/2021
* Uma bolsa que busca competência do contrato

Após a contabilização da segunda competência do contrato, fiz um aumento de bolsa com competência inicial 04/2021 á final 05/2021.

**1º Passo:**O contrato possui 12 parcelas financeiras de 1.000,00 cada  
Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
  
**BOLSA A** de 50% aplicada somente na 2ª parcela = **500,00**  
**BOLSA B**de 40% aplicada em todas as parcelas = **400,00 \* 12 = 4.800,00**

**2º Passo:**O sistema fará o cálculo do valor *total* de cada bolsa conforme parcelas atribuídas.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Competência Inicial** | **Competência**  **Final** | **Quant. C****ompetência** | **Vr. Total** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 02/2021 | 1 | 500,00 |
| Comp. da Bolsa **BOLSA B** | 01/2021 | 12/2021 | 12 | 4.800,00 |

**3º. Passo:**O sistema fará o cálculo do valor da Bolsa para ser contabilizado em cada *competência* contábil:

Neste exemplo, a **BOLSA A e BOLSA B**possui competência informada no contrato do aluno, então essas bolsas serão apropriada somente nesses períodos.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Competência**  **Inicial** | **Competência**  **Final** | **Quant.**  **Competência** | **Vr. Total** | **Mensal** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 02/2021 | 1 | 500,00 | 500,00 |
| Comp. da Bolsa **BOLSA B** | 01/2021 | 12/2021 | 12 | 4.800,00 | 400,00 |

Contabilização do contrato com **BOLSA A** apropriada na competência 01/2021 á 02/2021 é **BOLSA B**apropriada na competência 01/2021 á 12/2021

Memória de cálculo

A memoria de cálculo do log de contabilização também foi evoluído para a bolsa que for definida o período de competência contábil.

* Na apropriado a primeira competência do contrato, mas essa competência não pertence a competência de uma bolsa (exemplo acima), apresentaremos a memória de cálculo conforme abaixo:

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 01/2021

[Valor provisionado] / [Num. meses a contabilizar]  
Valor total de serviços: (12000,00) / (12) => R$ 1000,00  
Valor total de descontos: (0,00) / (12) => R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 50 | parcela 1 a 12 | total:R$4800,00 | Mês/Ano Base:01/2021  
Competência bolsa: 01/2021 a 12/2021  
Valor calculado para bolsa..: R$400,00 -> Cálculo R$4800,00/12  
---------------------------------------------------------------------------

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | parcela 2 a 2 | total:R$500,00 | Mês/Ano Base:01/2021  
Competência bolsa: 02/2021 a 02/2021  
Valor calculado para bolsa..: R$500,00 -> Cálculo R$500,00/1  
\*\*\* O valor desta bolsa não será considerado nessa competência \*\*\*  
---------------------------------------------------------------------------

Valor total bolsa por competência no mês: R$400,00  
Valor total demais bolsas...............: (R$0,00) / (12) => R$0,00  
Valor total bolsa processado para o mês: R$400,00

* Já na competência que a bolsa será apropriada, apresentamos a memória de cálculo conforme abaixo:

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 02/2021

\*Valores abaixo copiados da primeira apropriação mensal:[01/2021]  
Valor total de serviços: R$ 1000,00  
Valor total de descontos: R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 50 | parcela 1 a 12 | total:R$4800,00 | Mês/Ano Base:02/2021  
Competência bolsa: 01/2021 a 12/2021  
Valor calculado para bolsa..: R$400,00 -> Cálculo R$4800,00/12  
---------------------------------------------------------------------------  
=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | parcela 2 a 2 | total:R$500,00 | Mês/Ano Base:02/2021  
Competência bolsa: 02/2021 a 02/2021  
Valor calculado para bolsa..: R$500,00 -> Cálculo R$500,00/1  
---------------------------------------------------------------------------  
Valor total bolsa por competência no mês: R$900,00  
Valor total demais bolsas...............: R$0,00  
Valor total bolsa processado para o mês: R$900,00

Após contabilizar a competência do mês 02/2021 fiz uma inclusão de bolsa para parcela 4 e 5 (aumento de bolsa), informando a competência 04/2021 á 05/2021 e contabilizei o restante do contrato.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Competência**  **Inicial** | **Competência**  **Final** | **Quant.**  **Competência** | **Vr. Total** | **Mensal** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 02/2021 | 1 | 500,00 | 500,00 |
| Comp. da Bolsa **BOLSA B** | 01/2021 | 12/2021 | 12 | 4.800,00 | 400,00 |
| Comp. da **BOLSA A**  Parcela 4 á 5 | 04/2021 | 05/2021 | 2 | 1000,00 | 500,00 |

Contabilização do contrato com o aumento da **BOLSA A** apropriada na competência 04/2021 á 05/2021.

Memória de cálculo

Na apropriado a primeira competência do aumento da bolsa no contrato, apresentaremos a memória de cálculo conforme abaixo:

Apropriação mensal de aumento:

Competência processada: 04/2021  
Última competência: 12/2021

[Valor provisionado] - [Valor já contabilizado] / [Num. meses a contabilizar]  
Valor total de serviços: (0,00 - 0,00)/(9) => R$ 0,00  
Valor total de descontos: (0,00 - 0,00)/(9) => R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | Aumento | total:R$1000,00 | Mês/Ano Base:04/2021  
Competência bolsa: 04/2021 a 05/2021  
Valor calculado para bolsa..: R$500,00 -> Cálculo R$1000,00/2  
---------------------------------------------------------------------------  
Valor total bolsa por competência no mês: R$500,00  
Valor total demais bolsas...............: (R$0,00) / (9) =>R$0,00  
Valor total bolsa processado para o mês: R$500,00

Processo de contabilização com aumento e redução do valor da bolsa que foi definida período de competência contábil

* Se todas as competências foram contabilizadas e houver uma redução no valor da bolsa, o valor restante deve deve ser reconhecido na próxima competência a ser contabilizada.
* Se todas as competências foram contabilizadas e houver uma aumento no valor da bolsa, o valor restante deve deve ser reconhecido na próxima competência a ser contabilizada.
