---
content_hash: ec842eeac29b945d5b19382a4dcf54122defd23c13f3f3da8126cff02a7f7638
fetched_at: '2026-06-29T00:12:00.084197+00:00'
page_id: '880053356'
product: rm
source: tdn-rm
title: Guia do ICMS
type: documentation
url: https://tdn.totvs.com/display/LRM/Guia+do+ICMS
version: 43
---

# Conteúdo:

1Conteúdo:

# 1. Sobre

A Guia do ICMS oferece uma visão consolidada de toda a operação da empresa que sofreu incidência do ICMS e, também, os valores apurados.

Os dados necessários para a geração desta guia são provenientes dos Lançamentos Fiscais e dos Períodos de Apuração. São selecionados todos os Lançamentos Fiscais das Coligadas, Filiais e Período filtrados, que não estejam Cancelados ou Estornados.

# 2. Quadros disponíveis na guia

CardsQuadros de valores

O valor operacional representa o total das operações realizadas no período analisado considerando Coligadas, Filiais e períodos filtrados, que foram tributados pelo ICMS.

Já o card do total dos impostos, representa o total do débito e do crédito do ICMS para as Coligadas, Filiais e períodos filtrados. São considerados o ICMS próprio, o Diferencial de Alíquota e ICMS ST.

As informações são provenientes dos Itens dos Lançamentos Fiscais, excluindo os cancelados ou estornados.

* **Valor Operacional**: Somatório do valor financeiro dos itens: (Valor da Mercadoria + Despesa + Seguro + Frete - Desconto) dos Lançamentos Fiscais de Entrada ou Saída.
* **Total do Imposto:**

* + **Créditos:**Somatório dos Créditos de ICMS e ICMS-ST calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados.
  + **Débitos:**Somatório dos Débitos de ICMS e ICMS-ST calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados.

## 

Gráfico de Apuração de ICMS

Este quadro traz a representação gráfica do total dos créditos, dos débitos e o saldo do imposto a pagar ou o saldo credor por período de apuração.

A origem dos dados é o Período de Apuração. Se o mesmo estiver com Status aberto, o sistema faz uma simulação do encerramento e apresenta os valores parciais, considerando os lançamentos fiscais escriturados até a data do processamento.

Gráfico de Operações por CST

Neste gráfico, o valor operacional das operações selecionadas através do filtro aplicado, são agrupadas por Código de Situação Tributária - CST.  Para apresentação dos valores, o preenchimento do CST é obrigatório, em todas as operações do período informado no filtro.

A origem dos dados são os Itens do Lançamento Fiscal escriturados até o momento do processamento.

* **Valor Operacional**: Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais de Entrada ou Saída (mercadoria, despesas, segura, frete e subtrai o desconto).
* **Valor do ICMS**:  Totalização, crédito - débito, do valores de ICMS, ICMS-ST e Diferença de alíquota.
Apuração por UF

Este mapa traz a totalização dos valores devidos agrupados por Estados, considerando todas as filiais e períodos filtrados, oferecendo uma visualização gráfica dos valores debitados e creditados a título de ICMS próprio, assim como os valores de substituição tributária e diferencial de alíquota devidos.

Para visualizar os valores, clique no Estado desejado.

## 

Grids de Débitos e Créditos

Estas grids detalham todas as operações selecionadas através do filtro aplicado agrupadas até o nível do CFOP, que geraram débito ou crédito do ICMS próprio, ICMS ST ou Diferencial de Alíquota.

A origem dos dados são os Itens do Lançamento Fiscal escriturados até o momento do processamento.

As operações são agrupadas por:

* Coligada
* Período
* Filial
* Estado
* CST e
* CFOP.

50%50%

São selecionados todos os Lançamentos Fiscais de Saída e de Entrada, não cancelados e que estejam associados a CFOP's "Fiscais".

* + Os valores da Coligada, Filial, Estado, Período são recuperados do lançamento;
  + Os valores de ICMS são recuperados, e totalizados, a partir dos Itens das Situações tributárias do lançamento.
  + No caso dos Lançamentos de entrada, crédito, o Estado é considerado como sendo o estado da filial do lançamento;
  + O CFOP/Natureza é dado pelas Situações tributárias do lançamento e o CST é recuperado a partir do CFOP da respectiva Situação tributária (e não o CST do item da Situação tributária);
  + Os valores de ICMS, ICMS-ST e Diferença de alíquota são buscados nos Itens das Situações tributárias do lançamento (e totalizados de acordo com o agrupamento citamos mais acima);

Origem dos valores na estrutura de dados

|  |  |  |
| --- | --- | --- |
| **Grupo** | **Campo** | **Origem (tabela/coluna)** |
| Débitos | Período (Data do Lançamento (E/S)) | DLAF.DATALF |
| Débitos | Coligada | DLAF.CODCOLIGADA |
| Débitos | Filial | DLAF.CODFILIAL |
| Débitos | Estado | DLAF.CODETD (lançamentos de saída)  GFILIAL.ESTADO (lançamentos de entrada) |
| Débitos | CST (Situação Tributária do ICMS) | DREGRAICMS.SITTRIBUTARIA |
| Débitos | CFOP (Código da Natureza) | DCFOP.CODNAT |
| Débitos | ICMS (Valor ICMS Produto) | DITEM.VLRICMSPRD |
| Débitos | ICMS-ST (Valor ICMS ST Produto) | DITEM.VLRICMSSTPRD |
| Débitos | Dif. Aliq. (Valor Diferencial de Alíquota) | DITEM.VLRDIFALIQUOTA |

Ajustes da Apuração

Esta grid traz o detalhamento de todos os Lançamentos de Ajustes que afetam a apuração do ICMS ou ICMS ST, agrupados por:

* Período
* Coligada
* Filial e
* Estado

---

0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=880053215)
