---
content_hash: 1a3a05c763ea50a5fb679e111abe65139af9ac6a0be5f57bfc3b3b9ac42747ff
fetched_at: '2026-06-29T00:10:31.894864+00:00'
page_id: '522010799'
product: rm
source: tdn-rm
title: FISCAL01-11509-DT - REGISTRO 1391 SPED Fiscal - Implementação do registro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522010799
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | [FISCAL01-11509](https://jiraproducao.totvs.com.br/browse/FISCAL01-11509) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-11509](https://jiraproducao.totvs.com.br/browse/FISCAL01-11509) |

## **02. SITUAÇÃO/REQUISITO**

#### **REGISTRO 1391 - PRODUÇÃO DIÁRIA DA USINA**

Campos incluídos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "1390” |  |
| 18 | COD\_ITEM | Informar o insumo conforme código do item (campo 02 do Registro 0200) | Criar um “lookup” na Tela de Cadastro de CONTROLE DE PRODUÇÃO DE USINA |
| 19 | TP\_RESIDUO | Tipo de resíduo produzido:  01 - Bagaço de cana 02 - DDG  03 - WDG | Criar este campo na Tela de Cadastro de CONTROLE DE PRODUÇÃO DE USINA |
| 20 | QTD\_RESIDUO | Quantidade de resíduo produzido (toneladas) | Criar este campo na Tela de Cadastro de CONTROLE DE PRODUÇÃO DE USINA |

## **03. SOLUÇÃO**

Os campos e suas validações, como solicitado, foram incluídos na geração do SPED e irão ser exibidos a partir de 2020 na versão 14
