---
content_hash: f20f807ea0fde74af2085247047c12a5c57fc572653d2765785e435995aa4fa4
fetched_at: '2026-06-29T00:10:53.191390+00:00'
page_id: '577896466'
product: rm
source: tdn-rm
title: Período de Competência Contábil na Bolsa - Exemplo 4
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577896466
version: 6
---

---

Contabilização do cancelamento do contrato com as seguintes cenários:

* Uma bolsa com compendia informada período 02/2021
* Uma bolsa que busca competência do contrato

Após a contabilização da segunda competência do contrato, fiz o cancelamento do contrato.

**1º Passo:**O contrato possui 12 parcelas financeiras de 1.000,00 cada  
Valor total dos serviços do contrato a ser contabilizado: 12.000,00 (parcelas 1 e 2 geradas e quitadas)  
  
**BOLSA A** de 30% aplicada somente na 2ª parcela = **300,00**  
**BOLSA B**de 10% aplicada em todas as parcelas = **100,00 \* 12 = 1.200,00**

**2º. Passo:**O sistema fará o cálculo do valor da Bolsa para ser contabilizado em cada *competência* contábil:

Neste exemplo, a **BOLSA A e BOLSA B**possui competência informada no contrato do aluno, então essas bolsas serão apropriada somente nesses períodos.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Competência**  **Inicial** | **Competência**  **Final** | **Quant.**  **Competência** | **Vr. Total** | **Mensal** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 |
| Comp. da **BOLSA A** Parcela 2 | 02/2021 | 02/2021 | 1 | 300,00 | 300,00 |
| Comp. da Bolsa **BOLSA B** | 01/2021 | 12/2021 | 12 | 1.200,00 | 100,00 |

Contabilização do contrato com:

* **BOLSA A** apropriada na competência 02/2021
* **BOLSA B**apropriada na competência 01/2021 é 02/2021, faltando as demais competência para ser apropriadas

**3º. Passo:**Após contabilizar a competência do mês 02/2021 fiz o cancelamento do contrato com data de cancelamento 01/03/2021.

O processo de cancelamento de contrato irá validar quantas competências já foram apropriadas e quais valores de bolsas estavam nessas apropriações, o restante será estornado.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | | | | | |  | **Apropriação** | | |
|  | **Competência Inicial** | **Competência Final** | **Quant. Competência** | **Vr. Total** | **Mensal** | **Jan/21** | **Fev/21** | **Falta apropriar** |
| Competência do Contrato | 01/2021 | 12/2021 | 12 | 12.000,00 | 1.000,00 | 1.000,00 | 1.000,00 | 10.000,00 |
| Comp. da BOLSA A Parcela 2 | 02/2021 | 02/2021 | 1 | 300,00 | 300,00 | 0,00 | 300,00 | 0,00 |
| Comp. da Bolsa BOLSA B | 01/2021 | 12/2021 | 12 | 1200,00 | 100,00 | 100,00 | 100,00 | 1.000,00 |

Contabilização do contrato com o cancelamento de contrato e estorno dos valores restante que não foram apropriados.
