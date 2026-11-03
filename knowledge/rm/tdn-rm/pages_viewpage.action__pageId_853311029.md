---
content_hash: a72852d653e66f5e197c4756aa1cbebd5ac38be7f180c0a456a74751fa038309
fetched_at: '2026-06-29T00:11:54.490031+00:00'
page_id: '853311029'
product: rm
source: tdn-rm
title: Importação extrato bancário - Formato OFX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853311029
version: 23
---

95

Oferecemos a conciliação bancária através da importação do arquivo **OFX** disponibilizado pelo banco facilitando ainda mais o dia a dia.

Observação

Este recurso está disponível a partir do patch 12.1.2406.123

## **01. Visão Geral**

OFX é a sigla para Open Financial Exchange, trata-se de um tipo de arquivo no formato digital disponibilizado pelos bancos diretamente no internet banking, que exportam as movimentações do extrato bancário.   
A forma de fazer a exportação depende do sistema de cada instituição, normalmente está localizado na tela de extrato, na opção salvar ou exportar.   
Além na sigla OFX, alguns bancos disponibilizam este formato com o nome Money 2000 ou Money 2002.

## **02. Layout OFX**

Considerando o padrão do layout do arquivo OFX, abaixo detalhamos quais os campos são considerados pelo TOTVS Gestão Financeira para: identificação da conta, importação das transações bancárias e atualização de saldo.

Informações bancárias

Informações utilizadas para identificar e localizar a conta/caixa referente a conta corrente do extrato que está sendo importado.

| TAG | Descrição | Mapeamento TOTVS Gestão Financeira |
| --- | --- | --- |
| <BANKACCTFROM></BANKACCTFROM> | Agrupador das informações sobre a Conta Bancária |  |
| <BANKID></BANKID> | Identificador do Banco | FCXA.NUMBANCO |
| <BRANCHID></BRANCHID> | Identificador da Agência (opcional) | FCXA.CODAGENCIA |
| <ACCTID></ACCTID> | Número da Conta corrente | FCXA.CODCONTA |

Informações das Transações

Informações utilizadas para importar as movimentações bancárias

| TAG | Descrição | Mapeamento TOTVS Gestão Financeira |
| --- | --- | --- |
| <BANKTRANLIST></BANKTRANLIST> | Agrupador das informações sobre as transações |  |
| <STMTTRN></STMTTRN> | Agrupador que delimita os dados de uma transação. E usado exclusivamente para transações lançadas (liquidadas) |  |
| <DTPOSTED> | Data da transação | FXCX.DATA |
| <TRNAMT> | Valor da transação | FXCX.VALOR |
| <FITID> | Identificador único da transação, definido pela instituição | FXCX.NUMERODOCUMENTO |
| <MEMO> | Informações extras | FXCX.HISTORICO |
| SEM TAG | Diferente do padrão CNAB o arquivo OFX não possui o conceito de categorias, desta forma foi definido o valor fixo "900" como categoria do OFX. | FXCX.CATEGORIA |

Identificação do Saldo Bancário

Informações utilizadas para atualizar o saldo bancário da conta/caixa.

| TAG | Descrição | Mapeamento TOTVS Gestão Financeira |
| --- | --- | --- |
| <BALAMT> | Saldo atual da conta | FCXA.SALDOBANCARIO |
| <DTASOF> | Data para o qual o saldo é válido | FCXA.DATASALDOBANCARIO |

## **03.** **Tabelas Envolvidas**

* FRECONCIL - Armazena os dados importados do arquivo para conciliação.
* FCXA - Representa a conta caixa associada a conta bancária
* FXCX - Representa as movimentações de extrato bancário
