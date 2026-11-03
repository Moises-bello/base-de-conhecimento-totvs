---
content_hash: c9a7d50ebe600f72bca6d8fdd2c4ff761fe91f04339d01e0c4cd45756242da01
fetched_at: '2026-06-29T00:10:31.213752+00:00'
page_id: '521115361'
product: rm
source: tdn-rm
title: FISCAL01-11411 DT - Registro C500
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11411+DT+-+Registro+C500
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11411 |

## **02. SITUAÇÃO/REQUISITO**

1. Incluir o modelo “66” na geração desse Registro.
2. Para documentos cancelados, incluir o campo CHV\_DOCe é obrigatório.
3. Campos incluídos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 1 | REG | Texto fixo contendo "C500” |  |
| 28 | CHV\_DOCe | Chave da Nota Fiscal de Energia Elétrica Eletrônica | Gerar com a informação do Campo Chave de Acesso do Lançamento Fiscal |
| 29 | FIN\_DOCe | Finalidade da emissão do documento eletrônico:  1 – Normal 2 – Substituição  3 – Normal com ajuste | Gerar com valor fixo “1”. Este campo só deve ser preenchido se o modelo do documento for “66”. |
| 30 | CHV\_DOCe\_REF | Chave da nota referenciada. | Não gerar |
| 31 | IND\_DEST | Indicador do Destinatário/Acessante: 1 – Contribuinte do ICMS;  2 – Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS;  9 – Não Contribuinte | Gerado conforme o Campo Contribuinte do ICMS do Cadastro do Cliente\Fornecedor. FCFO.CONTRIBUINTE |
| 32 | COD\_MUN\_DEST | Código do município do destinatário conforme a tabela do IBGE | Gerado com o Código do Município do Cadastro do Cli\For |
| 33 | COD\_CTA | Código da conta analítica contábil debitada/creditada | Não gerar |

## **03. SOLUÇÃO**

Implementação dos novos campos no registro C500 do SPED

Para documentos cancelados, o campo CHV\_DOCe sempre será gerado.

A geração destes novos campos se dará a partir de 2020.
