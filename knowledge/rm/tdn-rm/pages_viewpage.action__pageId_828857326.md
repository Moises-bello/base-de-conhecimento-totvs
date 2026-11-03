---
content_hash: fed685f7090051a91c2bd8f43826ece67bf97d7f1ab0e1de08b95b0d1428e34a
fetched_at: '2026-06-29T00:11:48.894023+00:00'
page_id: '828857326'
product: rm
source: tdn-rm
title: Importação da Tabela MATMED  de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828857326
version: 23
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Visualização**
3. **Relacionar itens**
4. **Layout de Importação**
5. **Importar Tabela MATMED**
6. **Atualizar tabela MATMED**
7. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Esta rotina é utilizada para importar ou atualizar a tabela MATMED de convênios e seus preços, por meio de um arquivo no formato CSV( separado por ponto e vírgula).

Conforme o padrão, o arquivo CSV deve usar **apenas o ponto e vírgula** como delimitador de colunas, sem pontos e vírgulas adicionais dentro dos dados.

Visualização

## **02. VISUALIZAÇÃO**

Para utilizar a rotina, acesse o menu **Faturamento > Atualização de Preços > Importação de Tabela MatMed para Convênios**.

Para visualizar os itens de uma tabela, preencha os campos: **Convênio**, **Tabela MatMed**  são obrigatórios e o restante será opcional como **Data de Vigência, Código e Descrição**, e clique em **Consultar**.

Nesse momento serão carregados todos os itens do estoque que estejam vinculados a uma tabela de preços correspondente.

Relacionar itens

## **03. RELACIONAR ITENS**

Cada item de estoque pode ter um ou mais itens relacionados. Após estabelecer esse relacionamento, é possível realizar a atualização dos preços com base na tabela MATMED importada.

Layout de Importação

## **04.** **LAYOUT DE IMPORTAÇÃO**

A rotina suporta arquivos CSV separados por ponto e vírgula e deve seguir o layout especificado para a importação.

| Posição | Coluna | Tamanho | Tipo | Condição |
| --- | --- | --- | --- | --- |
| **1** | **CodigoPRD** | 30 | Inteiro | Opcional |
| **2** | **Codigo** | 8 | Inteiro | Obrigatório |
| **3** | **Descricao** | 100 | Texto | Obrigatório |
| **4** | **Unidade** | 5 | Texto | Obrigatório |
| **5** | **Preco** | 15,4 | Decimal | Obrigatório |
| **6** | **CodigoEspecifico** | 20 | Inteiro | Opcional |
| **7** | **DescricaoEspecifico** | 100 | Texto | Opcional |

**Exemplo:**

Informação

Os campos opcionais quando não utilizados, não devem ser informados no arquivo.

Caso algum unidade de medida não exista no cadastro, uma mensagem será disparada e a importação é encerrada.

Importar Tabela MATMED 

## **05.** **IMPORTAR TABELA MATMED**

Para realizar a importação da tabela MATMED, siga os passos abaixo:

1. Acesse o menu.
2. Informe a Tabela MATMED que será importada.
3. Informe a Data de Vigência.
4. Selecione o tipo de filtro para atualização:
   1. Por código
   2. Por descrição
   3. Por código e descrição
5. Marque a opção "Código PRD" se aplicável.
6. Selecione o arquivo CSV a ser importado.
7. Clique em **Executar** para iniciar o processo.

Atualizar tabela MATMED

## **06. Atualizar tabela MATMED**

Para atualizar a tabela MATMED, realizar os seguintes passos:

1. 1. Menu
   2. Informe o **Tabela MATMED** que será atualizada;
   3. Informe a **Data de vigência**da tabela;
   4. Selecione o tipo de filtro que será utilizado para atualização
      1. Por código
      2. Por descrição
      3. Por código e descrição
   5. Quando todos os dados estiverem preenchidos de acordo, clique em **Executar** para dar inicio no processo.

O processo grava uma lista de itens que não puderam ser atualizados.

Tabelas Utilizadas

## **05. TABELAS UTILIZADAS**

* SZITEMESTOQESPECIFICO
* SZITEMESTQPRECO
* SZREVBRASINDICE
