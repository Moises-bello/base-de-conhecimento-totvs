---
content_hash: 2b64862059a06fbf9c16d9b144b9d4d1b20f7c466f29c9d62bd2792a325ab8e5
fetched_at: '2026-06-29T00:10:26.783173+00:00'
page_id: '514741089'
product: rm
source: tdn-rm
title: ICMS Diferido
type: documentation
url: https://tdn.totvs.com/display/LRM/ICMS+Diferido
version: 20
---

# Conteúdo

2Conteúdo

## **01. ICMS Diferido**

O ICMS (Imposto Sobre Circulação de Mercadorias e Serviços) Diferido é uma vantagem fiscal sob algumas operações que consiste na postergação do recolhimento do tributo para a operação seguinte. Este documento visa dar orientações sobre as parametrizações necessárias e o funcionamento do ICMS Diferido no módulo TOTVS Gestão Fiscal.

## **02. Cadastros**

O Cadastro da Regra de ICMS deve ser parametrizado no campo Situação tributária o valor **51*****,*** que é o CST (Código da Situação Tributária) referente a tributação com diferimento.

Preenchimento do campo Tipo Tributação:

1. Preencher com **Diferido** quando se quer aplicar 100% de diferimento nas operações.
2. Preencher com **Tributado** quando ser que aplicar o Diferimento Parcial.

No caso do Diferimento Parcial ou seja tipo de tributação **Tributado,** realizar a parametrização a seguir: No anexo do **Produto → Dados Fiscais por UF** parametrizar o percentual do diferimento no campo % Diferimento Parcial ICMS.

Observação: A UF que deve ser parametrizada é igual a UF da filial do movimento.

## **03. Movimento**

Requisitos para que o ICMS com diferimento seja calculado no tributo ICMS do item do movimento.

Para carregar o percentual de diferimento na linha do tributo ICMS, o movimento deve atender as regras abaixo:

* Natureza com Operação Interna, Interestadual ou Importação 1.xxx, 5.xxx, 6.xxx ou 3.xxx.
* CST da Regra de ICMS deve ser 51.
* O campo **Emite Cupom Fiscal**  (Desmarcado) no tipo do movimento   
  (Parâmetros Movimento -> Etapa 61 - Fiscal - Dados Fiscais)
* O campo **Consumidor Final** informado na aba Fiscal do movimento (Desmarcado).

O valor do tributo ICMS será reduzido conforme o percentual do diferimento quando existente.

### Exemplo:

difparDiferimento Parcial

|  |  |
| --- | --- |
| Base do ICMS | 1000,00 |
| Alíquota do ICMS | 18% |
| Percentual do Diferimento | 30% |
| Valor do ICMS | 126,00 |

totDiferimento Total

|  |  |
| --- | --- |
| Base do ICMS | 1000,00 |
| Alíquota do ICMS | 18% |
| Percentual do Diferimento | 100% |
| Valor do ICMS | 0,00 |

**Cálculo do ICMS Diferido**

Valor do ICMS = (Base do ICMS \* (Alíquota do ICMS / 100)).

Valor do ICMS = (Valor do ICMS - (Valor do ICMS \* (Percentual do Diferimento / 100))).

Observação: Se houver redução na base de cálculo do ICMS o imposto será calculado normalmente aplicando tal redução.

## **04. NF-e**

Na NF-e o ICMS com Diferimento será preenchido no Grupo de Tributação 51.

Vide documentação para esclarecimentos de como as tags do XML são geradas no grupo de tributação do ICMS51

## **05. Escrituração**

No processo de escrituração do movimento que possui o tributo ICMS com percentual de diferimento, no que se refere ao diferimento é escriturado somente o **Percentual do Diferimento na Visão do Item,**aba Valores ICMS no campo % Diferimento Parcial.

Exemplo de Lançamentos escriturados com diferimento total e parcial:

| Diferimento Total | Diferimento Parcial |
| --- | --- |

## **06. Lançamento Fiscal**

Requisitos para que o ICMS com diferimento seja calculado no item do lançamento fiscal

Para carregar o percentual de diferimento no item do lançamento fiscal deve atender as regras abaixo:

* Natureza com Operação Interna ou Importação 1.xxx, 5.xxx ou 3.xxx.
* O lançamento fiscal não deve ser de Cupom Fiscal. Para esta consistência é verificado o tipo de documento do Lançamento Fiscal, se no cadastro de **Tipo de Documento, aba Dados Adicionais** o campo Utiliza Cupom Fiscal está (Desmarcado);
* O campo **Operação com Consumidor Final** informado na aba Outros do lançamento fiscal deve estar (Desmarcado).

Comportamento o campo **Valor ICMS Diferido** da Situação Tributária**:**

* Exibido somente quando a filial utiliza a rotina estadual  (Rotina Estadual de Pernambuco).
* Calculado quando o Diferimento é 100%. (Tipo Tributação: **Diferido**)
* Valor do ICMS Diferido = (Valor do ICMS Outros \*  (Alíquota do ICMS da Regra de ICMS  / 100))).

No Item do Lançamento Fiscal é carregado o percentual de diferimento apenas para o cálculo do valor do ICMS quando é diferimento parcial.
