---
content_hash: b5fa7293bca0fa974084186107cac07329a917c1f2b43e5e7b0db84cb76fcbdb
fetched_at: '2026-06-29T00:10:27.787856+00:00'
page_id: '516645227'
product: rm
source: tdn-rm
title: DT Ajustes de Telas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Ajustes+de+Telas
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Pagamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-205](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-205) |

## **02. SITUAÇÃO/REQUISITO**

* Alterar PAGAR VIA  para "PAGAR COM".
* Tela de carteira digital - Excluir mensagem "COM QUAL CARTÃO DESEJA PAGAR".
* Tela de carteira digital - Retirar crases e maiúscula de Valor das "P"arcelas e Quantidade de "P"arcelas.
* Tela de carteira digital - Fazer tela semelhante à tela de valores do boleto com a visualização do cartão no meio antes dos botões de pagamento.
* Tela de extrato financeiro - Alterar a cor do separador de valor para cinza claro.
* Alterar no cliente a mensagem para os casos de pagamento não autorizado ou qualquer outra exceção de pagamento.
* Passar o cardFlag para a API de pagamento com cartão da carteira digital

## **03. SOLUÇÃO**

* Alterado o "PAGAR VIA" para PAGAR COM na página de escolha da forma de pagamento.
* Excluída a mensagem descrita acima.
* Excluída a crase de "VALOR A PAGAR".
* Inclusão de cabeçalho conforme tela de pagamento com valor do boleto, vencimento e foto.
* Alterada a cor do separador para cinza claro na tela de extrato financeiro.
* Bandeira do cartão passou a ser informado para a API de pagamento utilizando dados da carteira digital.
