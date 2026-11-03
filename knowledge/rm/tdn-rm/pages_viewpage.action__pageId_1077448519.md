---
content_hash: e82b3b4129d6649cf391de954e80ace99bcedfcb8843fb359805b19281d6b936
fetched_at: '2026-06-29T00:05:54.235340+00:00'
page_id: '1077448519'
product: rm
source: tdn-rm
title: Big Number - Férias em andamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077448519
version: 3
---

## 

## **CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Férias em andamento**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01. VERSÃO**

A partir da versão 12.1.2606 e superiores

## **02. VISÃO GERAL**

Através dessa visão será informado a quantidade de funcionários em situação de férias na data do sistema.

IMPORTANTE:

01 - Até a Liberação da competência se já estiver com a data do sistema operacional no próximo mês a contagem de funcionários em férias deve terminar no final do mês competência do produto.

02 - Esse número é guardado em cache então se houver cadastro de férias dentro do mês e a visão estiver aberta o host deve ser reiniciado para refletir o novo número.

## **03. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

A data atual do sistema operacional hoje é 17/06/2026

O retorno será com 3 funcionários em férias de acordo com os dados do banco

## **04.** **TELA Férias em andamento**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| No canto superior direito tem 3 pontos | Serve para selecionar se adiciona ou remove da visão dos favoritos |
| Retorno do Big Number | Retorna quantos funcionários estão com férias em andamento até a data do sistema operacional ou o último dia da competência enquanto não há liberação da competência |
| Percentual | .Demonstra a variação percentual entre a quantidade de funcionários com férias no mês anterior e no mês atual. Esse percentual pode ser negativo quando no mês anterior tiver mais férias que no mês atual  **Exemplo:** 4 férias em maio e 14 férias em abril -> 400 / 14 = 28,57 - 100 = 71,43     IMPORTANTE: Não haverá retorno de percentual caso não haja férias no mês anterior e se a quantidade de férias do mês anterior for igual a quantidade de férias do mês atual. |
| Botão Acessar | Acessa o processo de lançamento de férias que lançará férias de acordo com a parametrização do usuário, sendo que as férias devem estar previamente calculadas |

## **05. TABELAS UTILIZADAS**

* PFUFERIASPER
