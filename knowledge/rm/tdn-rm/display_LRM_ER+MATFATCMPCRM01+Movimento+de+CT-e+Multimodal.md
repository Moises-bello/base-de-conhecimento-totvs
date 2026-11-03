---
content_hash: e5279f303101df92024bb5887ddc036def7ec458f6f588f3473314ec5263e28a
fetched_at: '2026-06-29T00:08:49.640185+00:00'
page_id: '331852062'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01 Movimento de CT-e Multimodal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01+Movimento+de+CT-e+Multimodal
version: 95
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-2068 | **Subtarefa1** | NA |
| **Chamado/Ticket2** |  | | |
| **País** | Brasil | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## 

## Objetivo

Descrever as alterações necessárias no sistema TOTVS Gestão de Estoque, Compras e Faturamento que permitirão a inclusão de um movimento de CT-e Multimodal de forma que possa ser feito o envio desse para a SEFAZ conforme o leiaute exigido para essa modalidade de CT-e.

## 

## Definição da Regra de Negócio

Parâmetros de Tipo de Movimento

Em Fis - Conhecimento de Transporte, no ComboBox **Modal** (TTMVEXT.MODAL) deve ser apresentada a opção "Multimodal".

Edição do Movimento

Quando o parâmetro **Modal**, da etapa Fis- Conhecimento de Transporte do tipo de movimento estiver igual a "Multimodal", na edição do movimento desse tipo o sistema deverá apresentar o seguinte comportamento:

1. Em CTRC | Outros Dados, deverá ser criado um ComboBox chamado **Indicador Negociável** que deverá apresentar as opções "0 - Não Negociável" e "1 - Negociável". Esse campo é de preenchimento obrigatório e deve ser gravado na base.
2. Em CT-e, deverá ser apresentada a aba Seguro de Carga. Nessa aba deverão ser apresentados somente os seguintes campos:  
   - Seguradora;  
   - Apólice;  
   - Averbação: esse campo deverá ser tratado na tela para que seja possível informar apenas 20 caracteres.

Tabelas Utilizadas

* TTMVEXT - Tipos de Movimento
* TMOVTRANSP - Dados de Trasnporte
* TCTESEGURO - Dados de Seguro do CT-e

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
