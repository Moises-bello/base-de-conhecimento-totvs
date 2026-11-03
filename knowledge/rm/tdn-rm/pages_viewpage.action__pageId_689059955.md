---
content_hash: 07bd9c82d0d2b0c0e4976117c3fea15045e7092a108f8c694fdb2f91d71e54e1
fetched_at: '2026-06-29T00:11:21.176900+00:00'
page_id: '689059955'
product: rm
source: tdn-rm
title: Gerenciador de Movimento - Múltiplos Vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689059955
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | Folha de Pagamento |
| Função: | Gerenciador de Movimento |
| País: | Brasil |

## **02. SITUAÇÃO/REQUISITO**

Para empresas que possuem um número muito grande Múltiplos Vínculos e o cálculo da folha é feito de forma descentralizada, onde cada filial pode efetuar lançamentos simultaneamente com outra, mesmo tendo definido a ordem de cálculo na ficha financeira do funcionário, ainda assim, é necessário que uma ordem sequencial de cálculo seja seguida para que as bases de INSS dos funcionários que possuem múltiplos vínculos seja corretamente calculada.  Atualmente o sistema dispõe da tela em: RH | Folha de Pagamento | Folha Mensal  | Consulta | Múltiplos vínculos que Necessitam de Recálculo, que irá exibir todos os funcionários que necessitarem de recálculo. Porém há casos onde o recalculo não pode ser efetuado pois já houve pagamento para o funcionário. 

## **03. SOLUÇÃO**

Como solução, o produto possui o recurso de Gerenciador de Movimento, onde todas as movimentações de eventos digitadas ou lançadas pelo usuário serão armazenadas em uma tabela e lançadas posteriormente para o Envelope de Pagamento e/ou evenlope por centro de custo.

Abaixo exemplificaremos o lançamento para Multiplos Vínculos com a pessoa de código 324, cadastrada como Funcionário na Coligada 1 e Coligada  8:

Passo 01, Passo 02, Passo 03, Passo 04, Passo 05passo1,passo2,passo3,passo4,passo5yespasso1

Lançando o Grupo de Evento para a chapa 80999 na Coligada 8:

nopasso2

Lançando o Grupo de Evento para a chapa 00099 na Coligada 1:

nopasso3

Novamente na Coligada 8 e inserir eventos para a chapa 80999 através da entrada de eventos:

Na movimentação de eventos do Funcionário os eventos foram inseridos:

nopasso4

Fazendo o Lançamento do Gerenciador de Movimento para a chapa 00099 na Coligada 1:

O INSS foi calculado conforme a tabela progressiva:

No período da Ficha Financeira foi preenchido pelo cálculo com a Ordem Cálculo 1:

nopasso5

Fazendo o Lançamento do Gerenciador de Movimento para a chapa 80999 na Coligada 8:

O INSS foi calculado conforme a tabela progressiva:

No período da Ficha Financeira foi preenchido pelo cálculo com a Ordem Cálculo 2:

## **04. DEMAIS INFORMAÇÕES**

Ambas coligadas devem estar configuradas para utilizar o Gerenciador de Movimento para que os eventos sejam lançados no repositório.

## **05. ASSUNTOS RELACIONADOS**

Mais informações sobre a Recurso:
