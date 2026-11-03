---
content_hash: b668c874748f086d077f678f7b12f3f651827e566ab61b28843b0ce5cbe56ea5
fetched_at: '2026-06-29T00:10:52.286867+00:00'
page_id: '571776476'
product: rm
source: tdn-rm
title: Validações de Autorização das Diárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571776476
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Condições Contratuais com Convênios**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Ao executar o processo "Encerramento de Parcial", se o parâmetro "Diárias OBRIGATORIAMENTE incluídas nas Guias / Autorizações de Internação" estiver marcado, serão feitas as seguintes validações: 

* Será retornada a mensagem "Diária não autorizada. Excluir diária incorreta ou obter autorização para a diária lançada. Código: "x"." caso a diária lançada não esteja cadastrada em "Guia / Autorização".
* Será retornada a mensagem "Quantidade da DIÁRIA COBRADA maior do que a QUANTIDADE AUTORIZADA. Código: "x"." caso a quantidade da diária lançada for maior do que a quantidade da diária cadastrada em "Guia / Autorização".

As seguintes validações não necessitam do parâmetro "Diárias OBRIGATORIAMENTE incluídas nas Guias / Autorizações de Internação" marcado:

* Será retornada a mensagem "Quantidade de diárias ( "x" ) maior do que o período da parcial." caso a quantidade da diária lançada for maior do que o período da parcial.
* Será retornada a mensagem "Horário limite para cálculo de nova diária não está definido nas condições contratuais." caso o parâmetro "Horário limite para cálculo de nova diária" na tela de condições contratuais com convênios não esteja informado.

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TELA CONDIÇÕES CONTRATUAIS COM CONVÊNIOS**

Parâmetros "Diárias OBRIGATORIAMENTE incluídas nas Guias / Autorizações de Internação" e "Horário limite para cálculo de nova diária": 

## **04. TABELAS UTILIZADAS**

* SZATENDDIARIAS
* SZATENDAUTORIZ
* SZLEITO
* SZCLASSEACOMODACAO

]]>
