---
content_hash: ff5263db3388524fc05f95dae78231756f06cea8c8dcaf78711852b13aff4552
fetched_at: '2026-06-29T00:11:21.336309+00:00'
page_id: '69272091'
product: rm
source: tdn-rm
title: CNAE-SEFIP
type: documentation
url: https://tdn.totvs.com/display/LRM/CNAE-SEFIP
version: 9
---

|  |
| --- |
| **SEFIP -  ATUALIZAÇÃO CNAE 01/2019** |

O código CNAE a ser preenchido nos eventos de tabela de Estabelecimentos (S-1005) passou a respeitar o Anexo I da Instrução Normativa RFB 971/2009, com as alterações da Instrução Normativa RFB 1867/2019. Essa orientação foi publicada no portal do eSocial 01/03/2019, na Nota Técnica 11/2019.  
O programa do SEFIP não adequou aos novos códigos do CNAE conforme Instrução Normativa citada acima.  
Para atender aos clientes que tiveram alterações nos CNAEs foi criado novo campo no cadastro de seção, CNAE SEFIP, onde será preenchido automaticamente a partir do campo CNAE 2.0.

Para a criação do campo CNAE SEFIP deverá ser executado o RM Atualizador .

Deverá Atualizar os patches descritos abaixo:

12.1.24.125

12.1.23.189

12.1.22.263
