---
content_hash: 8c8276bc73818a8b0d156e87031cc65cade6840ec405ce6ab8d6d70bf9e26efe
fetched_at: '2026-06-29T00:10:32.026227+00:00'
page_id: '525016948'
product: rm
source: tdn-rm
title: FISCAL01-11503 DT REGISTRO C870 - Sped Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11503+DT+REGISTRO+C870+-+Sped+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | FISCAL01-11503 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11503 |

## **02. SITUAÇÃO/REQUISITO**

#### **REGISTRO C870 - ITENS DO RESUMO DIÁRIO DOS DOCUMENTOS (CF-E-SAT) (CÓDIGO 59)**

Este registro é filho do C860 (perfil B) e traz o detalhamento dos itens contidas no Resumo Diário Dos Documentos (Cf-E-Sat) (Código 59).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C870” |  |
| 02 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Gerado com o Código do Produto TPRD.CODIGOPRD |
| 03 | QTD | Quantidade do item | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.QTDEPRD |
| 04 | UNID | Unidade do item (Campo 02 do registro 0190) | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.CODUND |
| 05 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Gerado com o ST do Item do Lançamento Fiscal - DITEM.CST |
| 06 | CFOP | Código Fiscal de Operação e Prestação | Gerar com a CFOP associada ao Lançamento Fiscal - DNATUREZA.CODNAT |

Implementar a partir da versão 12.1.24.

Os ajustes da automação do SPED serão realizados ao final de toda a implementação.

Documentação complementa das alterações em: [https://docs.google.com/document/d/1kyP4gwChIGLBO56DIj879AMz1J9a1PBH1wKbOIm2Jrc/edit?pli=1#](https://docs.google.com/document/d/1kyP4gwChIGLBO56DIj879AMz1J9a1PBH1wKbOIm2Jrc/edit?pli=1 "Follow link")

## **03. SOLUÇÃO**

Foi implementado a geração do Registro C870, conforme o manual 3.0.2 do SPED Fiscal ICMS IPI, somente para lançamentos emitidos a partir de 2020 que seja de Saída e possua Modelo do Documento 59.
