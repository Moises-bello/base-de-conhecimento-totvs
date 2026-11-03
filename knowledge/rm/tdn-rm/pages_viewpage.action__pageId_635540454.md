---
content_hash: 9e48f3e7db26bfdeac7bc31608654e5a43b35494eb10eeb68bfa306da6b6d447
fetched_at: '2026-06-29T00:11:06.834126+00:00'
page_id: '635540454'
product: rm
source: tdn-rm
title: Nota Técnica 2020.005
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=635540454
version: 4
---

A Nota Técnica, 2020.005, trouxe uma série de novos campos e alterações de regras de validação para a versão 4.0, Nota Fiscal Eletrônica (NF-e), modelo 55 e Nota Fiscal de Consumidor Eletrônica (NFC-e), modelo 65.

falseVersoes1201VERSAO 1.20

## Cronograma

Este evento entra em vigor:

* Homologação a partir de **01/07/2021**.

* Produção a partir de **01/09/2021**.

## Legislação

Este documento foi elaborado com base na [Nota Técnica 2020.005 - v.1.20](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=) disponível no portal da NF-e.

## Versões

Os ajustes estão disponíveis a partir das versões:

12.1.29.300  
12.1.31.220  
12.1.32.156

falseRegras de Validação

#### **Ajustes**:

Na tag Indicador de presença **“tpViaTransp”** (id: I23a) foram incluídas as opções:

* 12=Em mãos – Alterar a Descrição do Campo (Handcarry. (NT 2013/005 v 1.10)
* 13=Por reboque – Novo

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 122.01 | I23a | tpViaTransp | Via de transporte internacional informada na Declaração de Importação (DI) ou na Declaração Única de Importação (DUImp) | E | I18 | N | 1-1 | 2 | 8=Conduto/Rede Transmissão 9=Meios Próprios 10=Entrada/Saída Ficta  11=Courier  12=Em mãos  13=Por reboque |

falseRegras de Validação

#### **Ajustes**:

#### **cBarra** e **cBarraTrib:** Utilizam o serviço do módulo de estoque para preencher os novos campos

#### **Grupo I. Produtos e Serviços da NF-e**

    Incluídos os Campos:

* **Código de barras** (Código de barras diferente do padrão GTIN do Grupo I (id:I03a)).
* **Código de Barra da Unidade Tributável** (Código de Barras da unidade tributável que seja diferente do padrão GTIN do Grupo I (id:I12a)).

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 102.01 | I03a | cBarra | Código de barras diferente do padrão GTIN | E | I01 | C | 0-1 | 3-30 | Preencher com o Código de Barras próprio ou de terceiros que seja diferente do padrão GTIN |
| 111.01 | I12a | cBarraTrib | Código de Barras da unidade tributável que seja diferente do padrão GTIN | E | I01 | C | 0-1 | 3-30 | Preencher com o Código de Barras próprio ou de terceiros, que seja diferente do padrão GTIN, correspondente àquele da menor unidade comercializável identificado por Código de Barras. |
