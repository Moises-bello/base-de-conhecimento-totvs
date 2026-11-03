---
content_hash: b02b0bd5e4d25dda8fb9a021c9637ed87c42dc016c22eab52c80ffdcf69f96fb
fetched_at: '2026-06-29T00:11:05.348617+00:00'
page_id: '630016423'
product: rm
source: tdn-rm
title: Transferência para Gastos Particulares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=630016423
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O processo de transferência para os gastos particulares tem a finalidade de transferir os itens que o convênio não cobre ou que foram lançados erroneamente e que devem ser pagos pelo própria paciente.

**Somente será possível transferir itens se a parcial estiver com o status "Em Elaboração".**

Para que o preço do item seja diferente do preço praticado pelo convênio, deve-se parametrizar o sistema da seguinte forma:

ParametrizacaoCaso os parâmetros abaixo estejam informados, o sistema calcula o preço de acordo com a tabela informada. Caso contrário, o valor será o praticado pelo convênio.Honorários e ExamesDiárias, Taxas e ServiçosMatmed

## **02. EXEMPLO DE UTILIZAÇÃO**

Para se transferir itens das abas: honorários, diárias, taxas e serviços e exames, basta selecionar os itens e executar o processo "Transfere itens selecionados para Gastos Particulares"

Os itens serão estornados das respectivas abas e serão lançados na aba de Gastos Particulares

No caso de transferência de MATMED, pode-se informar a quantidade a ser transferida

## **03.****TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDDIARIAS
* SZATENDTAXASERV
* SZATENDSADT
* SZATENDMATMED
* SZATENDGASTOPARTIC
