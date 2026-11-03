---
content_hash: 25374b85dfb00b7aeae69fbf1f076988ef273ee344d833d11bffebebf5cd751b
fetched_at: '2026-06-29T00:11:39.853148+00:00'
page_id: '790630730'
product: rm
source: tdn-rm
title: Escrituração de Lançamento Fiscais - ICMS Diferido Total
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790630730
version: 1
---

O diferimento é um benefício fiscal onde a cobrança do imposto e postergada conforme determinado pela legislação que define: quando ocorrerá; em que momento será cobrado; quem será o responsável pelo seu recolhimento posterior e quando será encerrado.

Vamos abordar dois exemplos, o diferido 100% e o diferimento parcial. Em ambas as situações, deve ser preenchido o % do diferimento no cadastro do produto em Anexo | Dados Fiscais por UR no campo “Diferimento Parcial ICMS”.

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

**Situação Tributária**

Todos os campos do Lançamento Fiscal incluído através do processo Escrituração de Lançamentos serão gravados automaticamente visto que essas informações já foram inseridas no módulo TOTVS Gestão de Estoque, Compra e Faturamento.

Nesse tipo de operação o valor total da mercadoria e carregado no campo "Outros ICMS".

**Item**

* **Valores ICMS**

|  |  |
| --- | --- |
| Outros ICMS | 20.000,00 |

* **%Diferimento Parcial**

No item do Lançamento Fiscal será apresentado o percentual do diferimento no campo "% Diferimento Parcial ICMS" conforme informado no cadastro do produto citado anteriormente.

Figura
