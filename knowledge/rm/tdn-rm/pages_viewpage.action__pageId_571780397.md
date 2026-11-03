---
content_hash: e1ec856b631c38d0e8cd7524c820f0ad5a831f0dc09c15c53037ff6322134f9e
fetched_at: '2026-06-29T00:10:52.290576+00:00'
page_id: '571780397'
product: rm
source: tdn-rm
title: Validação dos Preços de Taxas e Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571780397
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parâmetros**
4. **Tabela Procedimentos e Serviços**
5. **Tabela Valores de CH/CO**
6. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Ao encerrar a parcial, cada taxa ou serviço passa pelas seguintes validações:

* Valida se o valor da taxa ou serviço está igual ao cadastrado na Tabela de Procedimentos e Serviços. Se for diferente, retorna a mensagem:  "Valor do item cobrado é R$ XX,XX, diferente que o valor contratado de R$ XX,XX ou o valor contratado foi modificado para o valor em reais".
* Valida se a quantidade de CH da taxa ou serviço está igual à prevista na Tabela de Procedimentos e Serviços. Se for diferente, retorna a mensagem "Quantidade de CH do item XXXXXXXX diferente da prevista em Contrato".

Se o parâmetro "Mostrar Relatório com Mensagens não impeditivas" estiver habilitado, a mensagem devolvida para o usuário é um alerta (não impede o encerramento da parcial); caso contrário, a mensagem será um erro (impede o encerramento da parcial).

## **02. EXEMPLO DE UTILIZAÇÃO**

Para a validação, confere-se os cadastros de Valores CH/CO ( Cadastros → Condições Financeiras com Convênio → Convênio do Atendimento→ Anexos → Valores de CH/CO) e o cadastro na Tabela de Procedimentos e Serviços (Cadastros → Tabela de Procedimentos e Serviços). Caso tenha dois cadastros de CH/CO, um do tipo Normal e outro do tipo Especial, o cadastro de tipo Especial é usado.

## **03. PARÂMETROS**

É possível habilitar o parâmetro "Mostrar Relatório com Mensagens não impeditivas" ao acessar o menu Opções → Parâmetros → Parâmetros Gerais → aba Faturamento II

## **04. TABELA PROCEDIMENTOS E SERVIÇOS**

É possível mudar os valores da tabela de Procedimentos e Serviços para o item ao acessar Cadastros → Outros Cadastros → Tabela de Procedimentos e Serviços → Pesquisar pela Tabela utilizada pelo convênio e pelo item.

## **05. TABELA VALORES DE CH/CO**

Disponível em Cadastros → Condições Financeiras com Convênio → Convênio do Atendimento→ Anexos → Valores de CH/CO

## **06. TABELAS UTILIZADAS**

* SZTABPROCSERV
* SZCONDFINACEIRACH
* SZATENDTAXASERV

]]>
