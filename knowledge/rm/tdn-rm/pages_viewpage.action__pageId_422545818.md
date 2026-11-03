---
content_hash: f02a88fd211432b821f86b84cf4b41ecea09033d491379eef115a08c5c2e411e
fetched_at: '2026-06-29T00:09:21.122573+00:00'
page_id: '422545818'
product: rm
source: tdn-rm
title: BRPDE - Beneficiário dos Rendimentos Pagos a Residentes ou Domiciliados no
  Exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545818
version: 7
---

São beneficiário dos Rendimentos Pagos a residentes ou Domiciliados no Exterior.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Ordem | Campo | Valores válidos | Obrigatório | Campo |
| 1 | Identificador de registro | BRPDE | Sim | Fixo BRPDE |
| 2 | Beneficiário | 1 - Pessoa física  2 - Pessoa jurídica | Sim | Tipo do Cliente/Fornecedor |
| 3 | Código de país | De acordo com a tabela de códigos dos países constante na IN RFB nº 1990/2020 | Sim | Classificação do País do Cliente/Fornecedor |
| 4 | Número de identificação fiscal - NIF | - | Não | FCFO.NIF |
| 5 | Indicador de beneficiário dispensado do Número de Identificação Fiscal - NIF | S - Dispensado do Número de identificação fiscal - NIF  N - Não é dispensado do Número de identificação fiscal - NIF | Sim | Situação do NIF (Se "Beneficiário Dispensado do NIF" então "S" senão "N") |
| 6 | Indicador de que o país não exige Número de Identificação Fiscal - NIF | S - Dispensado do Número de identificação fiscal - NIF  N - Não é dispensado do Número de identificação fiscal - NIF | Sim | Situação do NIF (Se "País não Exige NIF" então "S" senão "N") |
| 7 | CPF/CNPJ | CPF com 11 dígitos  CNPJ com 14 dígitos | Não | Documento do Cliente/Fornecedor |
| 8 | Nome/Nome empresarial | - | Sim | Nome do Cliente/Fornecedor |
| 9 | Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica | De acordo com a tabela de informações sobre os beneficiários dos rendimentos constante na IN RFB nº 1990/2020 | Não | Tipos de Relacionamentos de Participantes (CRELACIONAMENTO.CODIGO) 00 == 900 01 == 500 02 == 510 03 == 520 04 == 530 05 == 540 06 == 550 07 == 570 09 == 560 |
| 10 | Logradouro | - | Não | Endereço do Cli./For. |
| 11 | Número | - | Não | Endereço do Cli./For. |
| 12 | Complemento | - | Não | Endereço do Cli./For. |
| 13 | Bairro/Distrito | - | Não | Endereço do Cli./For. |
| 14 | Código postal | - | Não | Endereço do Cli./For. |
| 15 | Cidade | - | Não | Endereço do Cli./For. |
| 16 | Estado/Província | - | Não | Endereço do Cli./For. |
| 17 | Telefone | - | Não | Endereço do Cli./For. |

|  |  |  |
| --- | --- | --- |
| Observações: | | |
| Ordem | Campo | Descrição |
| 9 | Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica | Preenchimento obrigatório se campo de ordem 2 (Beneficiário) igual a 2. |

Fonte: <https://www.in.gov.br/web/dou/-/ato-declaratorio-executivo-cofis-n-94-de-26-de-novembro-de-2021-363167350>
