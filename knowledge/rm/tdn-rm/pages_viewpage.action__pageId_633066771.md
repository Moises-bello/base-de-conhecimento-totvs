---
content_hash: 7189e983c9df5357246c4a2f44708ce4e7241b7fb27eca5c302d36fb48120b3a
fetched_at: '2026-06-29T00:11:06.280140+00:00'
page_id: '633066771'
product: rm
source: tdn-rm
title: Geração do Movimento de Fatura SUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633066771
version: 1
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Cadastro do Grupo de Codificação Contábil -SUS**
4. **Configuração por descrição única**
5. **Geração de movimento de fatura do SUS**
6. **Parâmetros -Tipo Movimento**
7. **Exclusão de Geração de movimento  do SUS**
8. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O movimento de fatura consiste no envio dos dados financeiros da fatura para o BackOffice integrado.

Quando integrado com o BackOffice RM, o movimento pode gerar o lançamento financeiro e o contábil.

## **02. EXEMPLO DE UTILIZAÇÃO**

Acesse o menu Faturamento > Faturamento SUS

A geração de movimento pode ser feita por grupo ou descrição única.

## **03. CADASTRO DO GRUPO DE CODIFICAÇÃO CONTABÍL - SUS**

* Para gerar um movimento por grupo é necessário acessar o menu:

Menu: Cadastros > Outros Cadastros >  Grupo de Codificação Contábil -SUS

 Inclua um novo grupo

## **04. CONFIGURAÇÃO POR DESCRIÇÃO ÚNICA**

* Para gerar um movimento por descrição  única, o produto da descrição única deve ser informado  de acordo  com o tipo de fatura AIH, BPA ou APAC.

Menu: Opções > parâmetros > Integração do RM Nucleus

## **05. GERAÇÃO DO MOVIMENTO DE FATURA DO SUS**

Acesse o menu Faturamento > Faturamento SUS

* Selecione a fatura com o status Faturada
* Execute o processo Gerar Movimento de Fatura do SUS

## **06. PARÂMETROS - TIPO MOVIMENTO**

* O tipo de movimento a ser gerado será preenchido de acordo com o parâmetro abaixo.

Os parâmetros poderão ser configurados  manualmente na geração do movimento ou já estarem configurados.

Mas é possível alterar o valor.

Menu: Opções > parâmetros > Integração do RM Nucleus

## **07. EXCLUSÃO MOVIMENTO DE FATURA DO SUS**

Através desse processo, será possível excluir o movimento de fatura .

* Selecione a fatura com o status Faturada e que tenha identificador do movimento.
* Execute o processo Excluir Movimento de Fatura.

## **08. TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZATENDIMENTO
* SZPARCIALATEND

Para AIH:

* SZSUSAIHPROD
* SZSUSRECEMNATO
* SZSUSAIHCID
* SZSUSPROCREALIZADOS

Para BPA:

* SZSUSBPALANC
* SZSUSBPAPROD
* SZSUSBPAPRODHIST

Para APAC

* SZSUSAPAC
* SZAPACPROC
* SZAPACMED
* SZAPACNEFRO
* SZAPACNEFROFISTULA
* SZAPACNEFROACOMPDRC
* SZAPACRADIO
* SZAPACQUIMIO
* SZAPACQUIMIO
* SZAPACPOSBARI
* SZAPACPREBARI
* SZAPACBARI
* SZAPACLAUDO
