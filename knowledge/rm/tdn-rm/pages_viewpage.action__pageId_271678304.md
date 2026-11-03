---
content_hash: e62226b5e23e15fc22c426baa77eded1fc57359919c109a6c8d974a26da31e59
fetched_at: '2026-06-29T00:08:28.654688+00:00'
page_id: '271678304'
product: rm
source: tdn-rm
title: 98946 MCP-219 ER Liberação de Medição - Rateio por Municípios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271678304
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Liberação de Medição |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado/Ticket** | 98946 | | |
| **País** | (X) Brasil  (X) Argentina  (X) México  (X) Chile  (X) Paraguai  (X) Equador (X) Colômbia | | |

   

## Objetivo

Este documento visa especificar a implementação da funcionalidade de “Rateio da Medição por trecho, na Liberação do período” no produto TOTVS Obras e Projetos. Este processo estará disponível a partir de patch da versão 12.1.16 e também nas versões posteriores.

É comum em contratos de prestação de serviços, executarem medições por município (por trecho).  Esta operação é executada em períodos de contrato, onde a medição é executado em mais de um município.

Por se tratar de uma prestação de serviço, é necessário realizar o recolhimento do ISS.

O ISS incide sobre os serviços prestados mediante a utilização de bens e serviços públicos explorados economicamente mediante autorização, permissão ou concessão, com o pagamento de tarifa, preço ou pedágio pelo usuário final do serviço.

Portanto, é necessário gerar uma nota para cada município, descrevendo o valor pago que corresponde ao serviço executado no período corrente.

## Definição da Regra de Negócio

Quando os serviços forem prestados no território de mais de um Município, a base de cálculo será proporcional.

A funcionalidade de medição por trecho consiste em criarmos um rateio por município para as medições de períodos de contratos para que, ao serem faturados, os impostos sejam apurados corretamente para cada município.

 A necessidade do cliente é que cada município tenha a emissão do faturamento em separado, para que as notas fiscais sejam impressas por município, de forma que um não tenha consciência do que foi faturado para o outro.

Os lançamentos do rateio serão realizados pelo valor, o somatório dos valores lançados não podem superar o valor bruto do período.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Liberação de Medição | Alteração |  | Conforme descrito nesse documento |
|  |  |  |  |
|  |  |  |  |

## Tabelas Utilizadas:

* MCNTMUNICIPIO.
* MITMCNTMUNICIPIO

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
