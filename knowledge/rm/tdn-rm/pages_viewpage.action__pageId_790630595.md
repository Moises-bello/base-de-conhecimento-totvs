---
content_hash: afc4b6120393d30e3d045ebeca0c87af3b04e5709e8c5dd3405a455655aab16e
fetched_at: '2026-06-29T00:11:39.849313+00:00'
page_id: '790630595'
product: rm
source: tdn-rm
title: Escrituração de Lançamento Fiscais - ICMS Diferido Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790630595
version: 1
---

Para o Diferimento parcial, será necessário informar o percentual a ser aplicado no cadastro do produto conforme a legislação pertinente.

Importante

O ICMS Diferido é a diferença entre o valor da operação própria do ICMS (aquela que seria devida no caso de não haver diferimento) e o valor do ICMS Diferido.

42Parametrização Regra de ICMSParametrização Regra de ICMS / IPI

O CFOP deverá ser configurado da seguinte maneira:

* **Regra de ICMS**

**Aba Identificação**

Tipo de Tributação: Tributado

Operação Tributária: Não se Aplica

Figura

**Aba Dados ICMS**

Alíquota do ICMS: Preencher de acordo com a operação

2Exemplo do MovimentoExemplo do Movimento

Na inclusão do movimento no TOTVS Gestão de Estoque, Compra e Faturamento tanto no TOTVS Gestão Fiscal o valor do diferimento será calculado automaticamente pelo sistema.

Para este cálculo faz-se necessário o preenchimento do percentual do diferimento no cadastro do produto em Anexos | Dados Fiscais por UF

Figura

Ao selecionar o código do produto no item do movimento ( TOTVS Gestão de Estoque, Compra e Faturamento) o percentual será preenchido automaticamente.

Figura

Todos os campos do lançamento incluído através do processo Escrituração de Lançamentos serão gravados automaticamente visto que essas informações já foram inseridas no módulo TOTVS Gestão de Estoque, Compra e Faturamento.

**Valor da Mercadoria**

|  |  |
| --- | --- |
| Valor da Mercadoria | 20.000,00 |

**ICMS e IPI**

* + **ICMS: Tributado**

|  |  |
| --- | --- |
| Base ICMS | 20.000,00 |
| Base Tributada ICMS | 20.000,00 |
| Alíquota do ICMS | 18% |
| Valor do ICMS | 3.600,00 |
| % do diferimento | 60% |
| Valor do ICMS Diferido | 2.160,00 |
| Valor do ICM devido neste exemplo | 1.440,00 (3.600,00 - 2.600,00) |

**Valor Total da Situação Tributária: 20.000,00**

Observação

Quando se tratar de ICMS Diferido o valor do percentual será preenchido na item do Lançamento Fiscal.

Figura
