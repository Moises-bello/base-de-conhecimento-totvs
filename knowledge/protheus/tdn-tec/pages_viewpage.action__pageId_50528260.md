---
content_hash: b546243f2a9825664cb0e17063127ce004c23f1d2db282628652ba4936489a0e
fetched_at: '2026-07-02T19:24:25.710429+00:00'
page_id: '50528260'
product: protheus
source: tdn-tec
title: Parâmetros de Linha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=50528260
version: 14
---

Parâmetros de Linha do TOTVS | SmartClient HTML

Um parâmetro de linha é um argumento enviado para o WebApp para a execução de um programa, comunicação ou ambiente específico.

## Parâmetros disponíveis

A seguir, observe os parâmetros de linha disponíveis:

| Parâmetro | Descrição |
| --- | --- |
| P | Identifica o programa inicial a ser executado |
| C | Identifica o nome da seção de conexão com o servidor |
| E | Identifica o nome da seção do ambiente no servidor |
| A | Parâmetro para o programa inicial  Identifica um parâmetro que será passado para o programa inicial. O parâmetro especificado é recebido pelo programa como uma string. Podem ser especificados mais de uma opção A=<valor>.  Ex: &A=TESTE&A=9901&A=01/01/1999 |

Nome dos parâmetros

Os nomes dos parâmetros são sensíveis a caixa alta/baixa e devem ser informados exatamente como descritos acima.

## Como passar os parâmetros através da URL

Os parâmetros de linha podem ser informados através da URL. Para isso, após a URL de acesso ao WebApp, é necessário informar o caractere **?** e os demais argumentos separados pelo caractere **&**.

textEclipseExemplo
