---
content_hash: 4b32aee6c27f2a11e32f1d8d8032af25f1dab24bd5e68e393b9b2a75912ac919
fetched_at: '2026-06-29T00:10:53.102655+00:00'
page_id: '576599977'
product: rm
source: tdn-rm
title: Período de Competência Contábil na Bolsa - Exemplo 2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=576599977
version: 7
---

---

Contabilização de bolsa em que uma das bolsas possua período de competência contábil diferenciada da competência do contrato

**1º Passo:**O contrato possui 12 parcelas financeiras de 1.000,00 cada  
Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
  
**BOLSA A** de 50% aplicada somente na 2ª parcela = **500,00**  
**BOLSA B**de 40% aplicada em todas as parcelas = **400,00 \* 12 = 4.800,00**

**2º Passo:**O sistema fará o cálculo do valor *total* de cada bolsa conforme parcelas atribuídas.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Competência Inicial** | **Competência**  **Final** | **Quant. C****ompetência** | **Vr. Total** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 03/2021 | 2 | 500,00 |
| Comp. da Bolsa **BOLSA B** | Competência do contrato | Competência do contrato | 12 | 4.800,00 |

Quando a competência da bolsa do contrato do aluno não é informada, será mantido o comportamento anterior que é buscar o período de competência contábil no contrato / período letivo / parametrização por curso, conforme definido na parametrização do sistema.

**3º. Passo:**O sistema fará o cálculo do valor da Bolsa para ser contabilizado em cada *competência* contábil:

Neste exemplo, a **BOLSA A e BOLSA B**possui competência informada no contrato do aluno, então essas bolsas serão apropriada somente nesses períodos.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Competência**  **Inicial** | **Competência**  **Final** | **Quant.**  **Competência** | **Vr. Total** | **Mensal** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 03/2021 | 2 | 500,00 | 250,00 |
| Comp. da Bolsa **BOLSA B** | Competência do contrato | Competência do contrato | 12 | 4.800,00 | 400,00 |

Contabilização do contrato com **BOLSA A** apropriada na competência 02/2021 á 03/2021 é **BOLSA B**apropriada de acordo com a competência do contrato.

Memória de cálculo

A memoria de cálculo do log de contabilização também foi evoluído para a bolsa que for definida o período de competência contábil.

* Apropriação da primeira competência do contrato, essa competência não pertence a competência das bolsas (exemplo acima), apresentaremos a memória de cálculo conforme abaixo:

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 01/2021

[Valor provisionado] / [Num. meses a contabilizar]  
Valor total de serviços: (12000,00) / (12) => R$ 1000,00  
Valor total de descontos: (0,00) / (12) => R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | parcela 2 a 2 | total:R$500,00 | Mês/Ano Base:01/2021  
Competência bolsa: 02/2021 a 03/2021  
Valor calculado para bolsa..: R$250,00 -> Cálculo R$500,00/2  
\*\*\* O valor desta bolsa não será considerado nessa competência \*\*\*  
---------------------------------------------------------------------------

Valor total bolsa por competência no mês: R$0,00  
Valor total demais bolsas...............: (R$4800,00) / (12) => R$400,00  
Valor total bolsa processado para o mês: R$400,00

* Já na competência que a bolsa será apropriada, apresentamos a memória de cálculo conforme abaixo:

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 02/2021

\*Valores abaixo copiados da primeira apropriação mensal:[01/2021]  
Valor total de serviços: R$ 1000,00  
Valor total de descontos: R$ 0,00  
Valor total bolsas que seguem a competência do contrato: R$ 400,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | parcela 2 a 2 | total:R$500,00 | Mês/Ano Base:02/2021  
Competência bolsa: 02/2021 a 03/2021  
Valor calculado para bolsa..: R$250,00 -> Cálculo R$500,00/2  
---------------------------------------------------------------------------  
Valor total bolsa por competência no mês: R$250,00  
Valor total demais bolsas...............: R$400,00  
Valor total bolsa processado para o mês: R$650,00
