---
content_hash: 53ece5af40c104ba643afb5d01165cc612b1e9036e16b64dec7c9d02134a872a
fetched_at: '2026-06-29T00:09:10.840901+00:00'
page_id: '403048940'
product: rm
source: tdn-rm
title: Planilha_Exemplo_Medição_Consumo_Reajuste_Discriminado_Preço_Inicial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403048940
version: 12
---

Segue abaixo um exemplo da utilização do reajuste discriminado na Medição/Consumo a Preço Inicial.

|  |  |  |  |
| --- | --- | --- | --- |
| **CONTRATO** | | | |
| **Insumo** | **Quantidade Contratada** | **Preço Unitário** | **Valor Total Contratado** |
| A - Insumo A | 1,0000 | R$ 5.000.000,00 | R$ 5.000.000,00 |
| B - Insumo B | 60,0000 | R$ 274.367,29 | R$ 16.462.037,40 |
|  |  | **VALOR TOTAL CONTRATADO** | R$ 21.462.037,40 |

|  |  |  |
| --- | --- | --- |
| **REAJUSTES** | | |
| **Insumo** | **Vigência (A partir de)** | **Percentual de Reajuste** |
| Insumo A | 01/02/2019 | 0,28970% |
| Insumo B | 01/02/2019 | 1,36470% |
| Insumo A | 01/03/2019 | 2,73730% |
| Insumo B | 01/03/2019 | 3,37820% |

|  |  |
| --- | --- |
| **PERIODOS** | |
| 001 | 01/01/2019 |
| 002 | 01/02/2019 |
| 003 | 01/03/2019 |
| 004 | 01/04/2019 |

**RESUMO RESULTADOS MEDIÇÕES:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Período** | **Insumo** | **Quantidade\_Contratada** | **Valor\_Inicial\_Contratado** | **Total\_Contratado** | **Percentual\_Medido** | **Quantidade\_Medida** | **Valor\_Medido\_Preço\_Inicial** | **Percentual\_de\_Reajuste** | **Valor\_Medido\_Reajuste** | **Valor\_Calculado\_Reajuste** | **Saldo\_Reajuste** |
| 1 | A | 1 | R$5.000.000,00 | R$5.000.000,00 | 0,00002 | 0,0000001 | R$1,00 | 0,00% | R$0,00000 | R$0,01000 | R$0,00000 |
| B | 60 | R$274.367,29 | R$16.462.037,40 | 0,843109493 | 3,5759057 | R$138.793,00 | 0,00% | R$0,00000 | R$19.834,94000 | R$0,00000 |
| TOTAL |  |  |  |  |  | R$138.794,00 |  |  |  |  |
| 2 | A | 1 | R$5.000.000,00 | R$5.000.000,00 | 0 | 0 | R$0 | 0,28970% | R$724,25000 | R$724,25000 | R$0,00000 |
| B | 60 | R$274.367,29 | R$16.462.037,40 | 0,117099722 | 0,0821809 | R$19.277,00 | 1,36470% | R$0,00000 | R$263,07322 | R$263,07322 |
| TOTAL |  |  |  |  |  | R$269.277,00 |  |  |  |  |
| 3 | A | 1 | R$5.000.000,00 | R$5.000.000,00 | 1,7589088 | 0,0087945 | R$87.945,44 | 2,73730% | R$2.000,00000 | R$2.407,33053 | R$407,33053 |
| B | 60 | R$274.367,29 | R$16.462.037,40 | 0,00275786 | 0,0019355 | R$454,00 | 3,37820% | R$10,00000 | R$15,33703 | R$268,41025 |
| TOTAL |  |  |  |  |  | R$88.399,44 |  |  |  |  |
| 4 | A | 1 | R$5.000.000,00 | R$5.000.000,00 | 93,2410712 | 0,0087945 | R$4.912.053,56 | 2,73730% | R$128.021,72263 | R$127.614,39210 |  |
| B | 60 | R$274.367,29 | R$16.462.037,40 | 99,03703293 | 0,0019355 | R$16.303.513,40 | 3,37820% | R$551.033,69993 | R$550.765,28968 |  |
| TOTAL |  |  |  |  |  | R$21.462.037,40 |  |  |  |  |

**Observações:**

* É permitido medir valor reajuste com valor medido inicial zerado. Exemplo: Medição de reajuste no período final do contrato.
* O Saldo de Reajuste é gerado a partir da medição do item, já no próprio item de medição.
* É sugerido o valor calculado de reajuste como valor medido de reajuste, mas pode ser zerado o mesmo de forma a gerar saldo de reajuste.

**DETALHAMENTO DE CAMPOS:**

****Consumo de Objetos****

|  |  |
| --- | --- |
| **CONTRATO:** 0001/2018 **VALOR CONSUMIDO:** R$ 898.752,01 **SALDO:** R$ 20.563.285,39 | **PERÍODO:** 0001 **VALOR CONSUMIDO:** R$ 898.752,01 **SALDO REAJUSTE:** R$ 0 |

**CONTRATO - SALDO:** Saldo Valor Inicial + Saldo Reajuste

**PERÍODO -** **VALOR CONSUMIDO:** Valor Medido Preço Inicial + Valor Medido Reajuste

**Objetos Associados ao Contrato:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Numero\_Aditivo** | **Código\_do\_Insumo** | **Quantidade\_Contratada** | **Quantidade\_Consumida** | **Percentual\_Consumido\_(%)** | **Valor\_Inicial\_Contratado** | **Valor\_Medido\_Preço\_Inicial** | **Saldo\_Valor\_Total** | **Valor\_Medido\_Total** | **Percentual\_Reajuste\_do\_Período\_(%)** | **Acumulado\_Calculado\_de\_Reajuste** | **Acumulado\_Medição\_de\_Reajuste** | **Saldo\_Reajuste** |
|  | A | 1,0000 | 0,5000 | 50% | R$5.000.000,00 | R$ 898.752,01 | R$ 0,00 | R$ 898.752,01 | 0 | 0 | 0 |  |
|  | B | 60,0000 | 20,0000 | 33,33% | R$ 274.367,29 | R$ 0 | R$ 0,00 | 0 | 0 | 0 | 0 |  |

**Valor Medido Preço Inicial:**MOBJCNTMED**.**VALORMEDIDO

**Acumulado Medição de Reajuste: sum(**MOBJCNTMED**.**VALORMEDIDOREAJUSTE )

**Acumulado Calculado de Reajuste: **sum(****MOBJCNTMED**.**VALORCALCULOREAJUSTE )

**Saldo Reajuste:** Acumulado Calculado de Reajuste - Acumulado Medição de Reajuste

****Saldo Valor Total:****Saldo Total a Preço Inicial + Saldo de Reajuste

**Valor Medido Total:** Valor Medido Preço Inicial Acumulado + Valor Medido Reajuste Acumulado

**Percentual\_Reajuste:** Percentual de Reajuste vigente no período

**Objetos a Consumir:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código\_do\_Insumo** | ****Código\_da\_Tarefa**** | ****Quantidade\_Contratada**** | ****Valor\_Inicial\_Contratado**** | **Percentual\_Consumido\_(%)** | **Quantidade\_Consumida** | **Valor\_Medido\_Preço\_Inicial** | **Percentual\_Reajuste\_Período\_(%)** | ****Valor\_Calculado\_de\_Reajuste**** | ******Valor\_Medido\_Reajuste****** | **Saldo\_do\_Reajuste** | **Valor\_Medido\_Total** | **Acumulado\_Medição\_de\_Reajuste** |
| A | 001.01.01 | 1 | R$5.000.000,00 | 50% | 0,5 | R$ 2.500.000,00 | 0,28970% | R$ 7242,50 | R$ 100,00 | R$  7142,50 | R$ 2.500.100,00 | R$ 0,00 |

* **Percentual Consumido, Quantidade Consumida são sobre o Valor Medido Preço Inicial**
* **Percentual de Reajuste Período:** Percentual de reajuste vigente no período.
* **Valor Calculado Reajuste:** Valor Medido Preço Inicial x Percentual Reajuste Período
* **Valor Medido Reajuste:** Sugerido o Valor Calculado Reajuste
* **Saldo do Reajuste:** Saldo de Reajuste Anterior Acumulado + Valor Calculado Reajuste - Valor Medido Reajuste
