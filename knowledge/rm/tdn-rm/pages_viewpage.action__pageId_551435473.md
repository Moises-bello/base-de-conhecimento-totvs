---
content_hash: ea8ce669f05636c23565318df559e74793cfa457ad7b5547f44a204b83093415
fetched_at: '2026-06-29T00:10:43.961348+00:00'
page_id: '551435473'
product: rm
source: tdn-rm
title: ICMS - CST 60/CSOSN500
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551435473
version: 9
---

# ICMS60 ou CSOSN500

O Código da Situação Tributária (**CST**) é o valor que identifica a origem da mercadoria e a forma de tributação que deverá incidir sobre a mesma. 

# Cadastros

O Cadastro da Regra de ICMS deve ser parametrizado  no campo Situação tributária o valor **60** ou no campo CSOSN **500 (Filial Optante Pelo Simples Nacional)***,* que é o Código da Situação Tributária do ICMS cobrado anteriormente por substituição tributária.

Preenchimento do campo Tipo Tributação:

* Preencher com **Substituição Tributária**.

# Movimento

Requisitos para que o cálculo seja efetuado conforme a última entrada:

**Movimento de entrada 1.2.XX:**

* Contendo ICMS e ICMS ST

**Movimento de saída 2.2.XX:**

Para carregar o valor do ICMS ST, o movimento deve atender as regras abaixo:

* Natureza com Operação Interna , Interestadual ou Exportação 5.xxx, 6.xxx ou 7.xxx.
* CST da Regra de ICMS deve ser 60 ou  CSOSN 500 (Simples Nacional).
* O campo **Calcula ICMS-ST de saída com CST 60 com base na última entrada do Produto** (Marcado) no tipo do movimento   
  (Parâmetros Movimento ->  Fis - Dados)

O valor do tributo ICMS ST será calculado conforme a última entrada:

Exemplo:

**Entrada:**

1
complete
**ICMS**

|  |  |
| --- | --- |
| Base do ICMS | 1000,00 |
| Alíquota | 12% |
| Valor ICMS | 120,00 |
| Quantidade do Item - Entrada | 5 |

**Cálculos do ICMS - Entrada**

Valor do ICMS = (Base do ICMS \* (Alíquota do ICMS / 100)).

Base Entrada ICMS = Base do ICMS /  Quantidade do Item

Valor Entrada ICMS  = Valor ICMS / Quantidade do Item

3
complete
**ICMS ST**

|  |  |
| --- | --- |
| Base do ICMS ST | 1000,00 |
| Alíquota | 18% |
| Valor ICMS ST | 180,00 |
| Quantidade do Item - Entrada | 5 |

**Cálculos do ICMS ST - Entrada**

*Valor do ICMS ST* = (Base do ICMS ST  \* (Alíquota do ICMS ST / 100)).

*Base Entrada ICMS ST* = Base do ICMS ST /  Quantidade do Item

*Valor Entrada ICMS ST* = Valor ICMS ST / Quantidade do Item

----------------------------------------------------------------------------------------------------------------

**Saída:**

4
complete
**ICMS ST**

*Base ICMS ST Saída =  Base Entrada ICMS ST \* (*Fator de Conversão da Unidade \* Quantidade Saída)

*Valor ST Saída = Valor  ICMS ST Entrada \**(Fator de Conversão da Unidade \* Quantidade Saída)

|  |  |
| --- | --- |
| Quantidade do Item - Saída | 5 |
| Base do ICMS ST - Saída | 200 \* (1 \* 5 ) = 1000,00 |
| Alíquota | Não será preenchida |
| Valor ICMS ST | 36  \* (1 \* 5 ) = 180,00 |

# NF-e

**ICMS 60**

Conforme exemplo acima o XML será preenchido desta forma:

**CSOSN 500**

Documentação para esclarecimentos de como as tags do XML são geradas no grupo de tributação do ICMS60:

# Escrituração

Exemplo de Lançamentos escriturados com a situação exemplada:

|  |
| --- |
