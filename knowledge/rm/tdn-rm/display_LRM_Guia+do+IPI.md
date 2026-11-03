---
content_hash: 1a31af69e964df912da155dc15b9ed062894ec0d1cb255f943aa78e60a449e72
fetched_at: '2026-06-29T00:12:00.092001+00:00'
page_id: '880053608'
product: rm
source: tdn-rm
title: Guia do IPI
type: documentation
url: https://tdn.totvs.com/display/LRM/Guia+do+IPI
version: 12
---

Conteúdo:

Conteúdo:

# 1. Sobre

A Guia do IPI oferece uma visão consolidada de toda a operação da empresa que sofreu incidência do IPI e, também, os valores apurados.

Os dados necessários para a geração desta guia são provenientes dos Lançamentos Fiscais e dos Períodos de Apuração. São selecionados todos os Lançamentos Fiscais das Coligadas, Filiais e Período filtrados, que não estejam Cancelados ou Estornados.

# 2. Quadros disponíveis na guia

CardsQuadros de valores

* **Valor Operacional**: Somatório do valor contábil dos itens: (Valor da Mercadoria + Despesa + Seguro + Frete - Desconto) dos Lançamentos Fiscais de Entrada ou Saída.
* **Total do Imposto:**

* + **Créditos:**Somatório dos Créditos de IPI calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados.
  + **Débitos:**Somatório dos Débitos de IPI calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados.

Gráfico de Apuração

Este quadro traz a representação gráfica do total dos créditos, dos débitos e o saldo do imposto a pagar ou o saldo credor por período de apuração.

A origem dos dados é o Período de Apuração. Se o mesmo estiver com Status aberto, o sistema faz uma simulação do encerramento e apresenta os valores parciais, considerando os lançamentos fiscais escriturados até a data do processamento.

Gráfico de Operações por CST

Totalização de valores dos itens (valor operacional) e dos valor de IPI de Débito/Crédito devidamente agrupados por CST de acordo com os filtros aplicados.

A série do gráfico consiste da somatória dos valores operacionais de Créditos e Débitos. Ao parar o ponteiro do mouse em uma série é apresentado os valores detalhados da seguinte forma:

* **Valor Operacional de Entradas**: Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais de Entrada (mercadoria, despesas, segura, frete e subtrai o desconto).
* **Valor Operacional de Entradas**: Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais de Saída (mercadoria, despesas, segura, frete e subtrai o desconto).
* **Créditos IPI**:  Totalização de créditos
* **Débitos** **IPI**:  Totalização de débitos
Grids de Débitos e Créditos

Estas grids mostram os detalhamentos dos créditos e dos débitos do IPI, totalizando os valores do tributo por Coligada, período, Filial, CST e CFOP.

São selecionados todos os Lançamentos Fiscais de Entrada e Saída, não cancelados e que estejam associados a CFOP's "Fiscais", agrupados e totalizados por coligada, filial, período e CST.

* Os valores da Coligada, Filial, Período são recuperados do lançamento;
* O CFOP/Natureza é dado pelas Situações tributárias do lançamento e o CST é recuperado a partir do CFOP da respectiva Situação tributária (e não o CST do item da Situação tributária);
* O valor Operacional somatório do valor financeiro dos itens: (Valor da Mercadoria + Despesa + Seguro + Frete - Desconto) dos Lançamentos Fiscais.
* Os valor de IPI é recuperado nos Itens das Situações tributárias do lançamento (e totalizados de acordo com o agrupamento citamos mais acima);

 Origem dos valores na estrutura de dados

|  |  |
| --- | --- |
| **Campo** | **Origem (tabela/coluna)** |
| Período | DLAF.DATALF |
| Coligada | DLAF.CODCOLIGADA |
| Filial | DALAF.CODFILIAL |
| CFOP | DCFOP.CODNAT |
| Valor Operacional | DITEM.VALORMERC - DITEM.DESCONTOITEM +  DITEM.VALORDESPESA + DITEM.VALORSEGURO + DITEM.VLRFRETE |
| IPI | DITEM.VALORIPI |

Ajustes da Apuração

Esta grid traz o detalhamento de todos os Lançamentos de Ajustes que afetam a apuração do IPI, agrupados por:

* Período
* Coligada
* Filial

---

0solid

[Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=880053215)
