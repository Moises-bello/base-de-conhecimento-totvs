---
content_hash: 819619248742573f5eeb757101d6cc615533d15b2f970180e0904cc3b2441a38
fetched_at: '2026-06-29T00:08:49.658508+00:00'
page_id: '331852429'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01 Envio de CT-e Multimodal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01+Envio+de+CT-e+Multimodal
version: 92
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

Descrever as alterações necessárias no sistema TOTVS Gestão de Estoque, Compras e Faturamento que permitirão o envio de um movimento de CT-e Multimodal, conforme o leiaute exigido pela SEFAZ para essa modalidade de CT-e.

## 

## Definição da Regra de Negócio

Leiaute Genérico

1. Na geração do xml do leiaute genérico, deverá ser tratada a **tag modal** para que retorne as informações conforme o parâmetro **Modal** do tipo de movimento de CT-e.
2. Quando o parâmetro Modal, da etapa Fis- Conhecimento de Transporte do tipo de movimento for igual a "Multimodal", na geração do xml do leiaute genérico, na tag xs:any, deverá ser incluído o xml do leiaute Multimodal.

Leiaute Multimodal

Abaixo o leiaute multimodal e a definição das informações do sistema pertinentes a cada uma das tags:

| Campo | Nível | Descrição | Ele | Tipo | Obrigatoriedade | Tamanho | Observações | Campo RM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **multimodal** |  | **Informações do Multimodal** | **G** |  | **Obrigatório** |  |  | - |
| COTM | 1 | Número do Certificado do Operador de Transporte Multimodal | E | C | Obrigatório | 1 - 20 |  | DFILIAL.OTM |
| indNegociavel | 1 | Indicador Negociável Preencher com: 0 - Não Negociável; 1 - Negociável | E | N | Obrigatório | 1 |  | Campo Indicador Negociável (verificar qual o campo foi criado na tabela) |
| **seg** | **1** | **Informações de Seguro do Multimodal** | **G** |  | **Opcional** |  |  | - |
| infSeg | 2 | Informações da seguradora | G |  | Obrigatório |  |  | - |
| xSeg | 3 | Nome da Seguradora | E | C | Obrigatório | 1 - 30 |  | TSEGURADORA.NOME da Seguradora informada em TCTESEGURO.SEGURADORA |
| CNPJ | 3 | Número do CNPJ da seguradora | E | N | Obrigatório | 14 |  | TSEGURADORA.CNPJ da Seguradora informada em TCTESEGURO.SEGURADORA |
| nApol | 2 | Número da Apólice | E | C | Obrigatório | 1 - 20 | Obrigatório pela lei 11.442/07 (RCTRC) | TCTESEGURO.APOLICE |
| nAver | 2 | Número da Averbação | E | C | Opcional | 1 - 20 | Não é obrigatório, pois muitas averbações ocorrem após a emissão do CT, mensalmente, por exemplo. | TCTESEGURO.AVERBACAO |

**Tabelas Utilizadas**

* TTMVEXT - Tipos de Movimento
* TCTESEGURO - Dados de Seguro do CT-e
* TSEGURADORA - Cadastro de Seguradoras
* DFILIAL - Dados Filiais RM Liber

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
