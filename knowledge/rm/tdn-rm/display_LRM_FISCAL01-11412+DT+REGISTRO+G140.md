---
content_hash: ccfb24e4c4ae1404521f304d4af673bcca16d133ff44356c800abe1aacd95523
fetched_at: '2026-06-29T00:10:31.242952+00:00'
page_id: '521129595'
product: rm
source: tdn-rm
title: FISCAL01-11412 DT REGISTRO G140
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11412+DT+REGISTRO+G140
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-11412 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11412 |

## **02. SITUAÇÃO/REQUISITO**

Evolução do registro G140 do SPED Fiscal para os novos campos criados à partir de 2020.

## **03. SOLUÇÃO**

Implementados os novos campos do Registro G140, conforme mapeamento de campos, que serão gerados somente à partir do ano de 2020.

Campos incluídos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 1 | REG | Texto fixo contendo "G140” |  |
| 04 | QTDE | Quantidade, deste item da nota fiscal, que foi aplicada neste bem, expressa na mesma unidade constante no documento fiscal de entrada | Nas operações de entrada é a quantidade do Item do Lançamento Fiscal.   Nas operações de saída, é a quantidade informada no Patrimônio.| |
| 05 | UNID | Unidade do item constante no documento fiscal de entrada | Gerado com a Unidade informado no Item do Lançamento Fiscal. |
| 06 | VL\_ICMS\_OP\_AP LICADO | Valor do ICMS da Operação Própria na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS Próprio informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 07 | VL\_ICMS\_ST\_AP LICADO | Valor do ICMS ST na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS ST informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 08 | VL\_ICMS\_FRT\_A PLICADO | Valor do ICMS sobre Frete do Conhecimento de Transporte na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS do Frete informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 09 | VL\_ICMS\_DIF\_A PLICADO | Valor do ICMS Diferencial de Alíquota, na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do Difal  informado na Sub pasta ICMS do Item do Lançamento Fiscal |
