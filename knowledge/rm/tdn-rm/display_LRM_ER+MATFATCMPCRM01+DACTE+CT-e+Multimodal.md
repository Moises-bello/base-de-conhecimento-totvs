---
content_hash: 5b3b0c9cd3793898a2a7fade9566fd273746fe8e73273ed327eb88ebfd9435d9
fetched_at: '2026-06-29T00:08:49.664913+00:00'
page_id: '331852909'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01 DACTE CT-e Multimodal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01+DACTE+CT-e+Multimodal
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

Descrever como deve ser feito o relatório padrão para impressão da DACTE do CT-e Multimodal.

## 

## Definição da Regra de Negócio

Na prestação de serviço de Transporte Multimodal de Cargas, esse DACTE fica dispensado de acompanhar a carga, exceto em caso de contingência com uso de FS-DA.

**O campo Modal do DACTE deve ser tratado para considerar o modal informado no parâmetro do tipo de movimento.**

Abaixo o leiaute exemplo do CT-e Multimodal, de acordo com a Nota Técnica 2016/002:

Campos Específicos do Leiaute Multimodal

1. Nº do Certificado do Operador de Transporte Multimodal: informar o campo DFILIAL.OTM;
2. Indicador Negociável: preencher conforme campo **Indicador Negociável** do movimento (verificar campo criado na tabela);
3. CNPJ da Seguradora: TSEGURADORA.CNPJ da Seguradora informada em TCTESEGURO.SEGURADORA;
4. Nome da Seguradora: TSEGURADORA.NOME da Seguradora informada em TCTESEGURO.SEGURADORA;
5. Número da Apólice: TCTESEGURO.APOLICE;
6. Número da Averbação: TCTESEGURO.AVERBACAO.

**Tabelas Utilizadas**

* TTMVEXT - Tipos de Movimento
* TCTESEGURO - Dados de Seguro do CT-e
* TSEGURADORA - Cadastro de Seguradoras
* DFILIAL - Dados Filiais RM Liber

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
