---
content_hash: 61e3ec0af048fe18d2458675f1fb50692c568b18c0ab0cf9b745b07025a1bac8
fetched_at: '2026-06-29T00:10:53.094441+00:00'
page_id: '576599918'
product: rm
source: tdn-rm
title: Período de Competência Contábil na Bolsa - Exemplo 1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=576599918
version: 15
---

---

Contabilização de bolsa em que seja informado período de competência contábil e que seja um período diferente entre elas.

**1º Passo:**O contrato possui 12 parcelas financeiras de 1.000,00 cada  
Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
  
**BOLSA A** de 50% aplicada somente na 1ª parcela = **500,00**   
**BOLSA B**de 80% aplicada somente na 5ª parcela = **800,00**

**2º. Passo:**O sistema fará o cálculo do valor da Bolsa para ser contabilizado em cada *competência* contábil:

Neste exemplo, a **BOLSA A e BOLSA B**possui competência informada no contrato do aluno, então essas bolsas serão apropriada somente nesses períodos.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Competência**  **Inicial** | **Competência**  **Final** | **Quant.**  **Competência** | **Vr. Total** | **Mensal** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 |
| Comp. da **BOLSA A**  Parcela 2 | 02/2021 | 03/2021 | 2 | 500,00 | 250,00 |
| Comp. da Bolsa **Bolsa B** Parcela 5 | 05/2021 | 05/2021 | 1 | 800,00 | 800,00 |

Contabilização do contrato com **BOLSA A** apropriada na competência 02/2021 á 03/2021 é **BOLSA B**apropriada na competência 05/2021.

Memória de cálculo

A memória de cálculo do log de contabilização também foi evoluído para a bolsa que for definida o período de competência contábil.

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

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 50 | parcela 5 a 5 | total:R$400,00 | Mês/Ano Base:01/2021  
Competência bolsa: 05/2021 a 05/2021  
Valor calculado para bolsa..: R$400,00 -> Cálculo R$400,00/1  
\*\*\* O valor desta bolsa não será considerado nessa competência \*\*\*  
---------------------------------------------------------------------------

Valor total bolsa por competência no mês: R$0,00  
Valor total demais bolsas...............: (R$0,00) / (12) => R$0,00  
Valor total bolsa processado para o mês: R$0,00

* Já na competência que a bolsa será apropriada, apresentamos a memória de cálculo conforme abaixo:

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 02/2021

\*Valores abaixo copiados da primeira apropriação mensal:[01/2021]  
Valor total de serviços: R$ 1000,00  
Valor total de descontos: R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 48 | parcela 2 a 2 | total:R$500,00 | Mês/Ano Base:02/2021  
Competência bolsa: 02/2021 a 03/2021  
Valor calculado para bolsa..: R$250,00 -> Cálculo R$500,00/2  
---------------------------------------------------------------------------  
Valor total bolsa por competência no mês: R$250,00  
Valor total demais bolsas...............: R$0,00  
Valor total bolsa processado para o mês: R$250,00

Apropriação mensal:  
Período de competência: 01/2021 - 12/2021  
Competência processada: 05/2021

\*Valores abaixo copiados da primeira apropriação mensal:[01/2021]  
Valor total de serviços: R$ 1000,00  
Valor total de descontos: R$ 0,00

=> Bolsa(s) com competência(s) diferenciada(s)  
Bolsa............: 50 | parcela 5 a 5 | total:R$400,00 | Mês/Ano Base:05/2021  
Competência bolsa: 05/2021 a 05/2021  
Valor calculado para bolsa..: R$400,00 -> Cálculo R$400,00/1  
---------------------------------------------------------------------------  
Valor total bolsa por competência no mês: R$400,00  
Valor total demais bolsas...............: R$0,00  
Valor total bolsa processado para o mês: R$400,00
