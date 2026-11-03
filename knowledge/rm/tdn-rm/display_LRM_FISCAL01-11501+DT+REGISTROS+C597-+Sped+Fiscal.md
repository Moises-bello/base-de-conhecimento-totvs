---
content_hash: e9a9863d2c6fa123e06200ed3c1462817ed32fd4159ba6edc2ac0b1251ecceb8
fetched_at: '2026-06-29T00:10:32.037569+00:00'
page_id: '525018446'
product: rm
source: tdn-rm
title: FISCAL01-11501 DT REGISTROS C597- Sped Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11501+DT+REGISTROS+C597-+Sped+Fiscal
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11501 |

## **02. SITUAÇÃO/REQUISITO**

Implementar a geração do Registro:

#### **REGISTRO C597 - OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL**

Incluído com o objetivo de promover ajuste junto a apuração para os documentos(Códigos 06, 28, 29 E 66), criado na mesma estrutura do Registro C197 que trabalha a partir do código de ajuste e seus 3º e 4º dígito para determinar a influência a crédito ou a débito junto a apuração.

Filho do Registro C590

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C597” |  |
| 02 | COD\_AJ | Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3 | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal – Código de Ajuste associado ao  DLAFAJUSTESPED.IDCODIGOAJUSTE |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste do documento fiscal | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.DESCRICAOCOMPLEMENTAR |
| 04 | COD\_ITEM | Código do item (campo 02 do Registro 0200) |  |
| 05 | VL\_BC\_ICMS | Base de cálculo do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.BASECALCULO |
| 06 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.ALIQUOTA |
| 07 | VL\_ICMS | Valor do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.VALORICMSICMSST |
| 08 | VL\_OUTROS | Outros valores | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.OUTROSVALORES |

Registro equivalente ao registro C197.

1. Alterar o enumerado do campo "Registro" do Cadastro de Ajuste, onde está "C197/D197" alterar para "**C197/D197/C597**".
2. Implementar o registro.

## **03. SOLUÇÃO**

Implementação do registro REGISTRO C597: OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES  
DE VALORES PROVENIENTES DE DOCUMENTO FISCAL

Geração apenas a partir de 2020.
