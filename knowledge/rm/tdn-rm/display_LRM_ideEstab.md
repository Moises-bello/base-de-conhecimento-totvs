---
content_hash: e46df9e2def9a041b3daa99dc2897efad91bb2b8b15c959dcf8cad6309b318aa
fetched_at: '2026-06-29T00:11:26.412984+00:00'
page_id: '716359690'
product: rm
source: tdn-rm
title: ideEstab
type: documentation
url: https://tdn.totvs.com/display/LRM/ideEstab
version: 2
---

## Identificação dos Estabelecimentos que receberam/repassaram recursos.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| ideEstab | ideContri | 1-1 |  | Identificação dos estabelecimentos que receberam/repassaram recursos | Deve receber o CNPJ da Filial que recebeu ou repassou o recurso, ou seja, a Filial associada ao lançamento financeiro a receber/pagar. |
| tpInscEstab | ideEstab | 1-1 | 1 | Preencher com o código correspondente ao tipo de inscrição  Validação: Deve ser igual a [1] (CNPJ) | Valor fixo "1" gerado pelo sistema. |
| nrInscEstab | ideEstab | 1-1 | 15 | Informar o número de inscrição do estabelecimento conforme o tipo de inscrição indicado no campo {tpInscEstab}.  Validação: Deve ser um número de CNPJ válido | GFILIAL.CGC |
