---
content_hash: 854e3ec67224b37e2d6a5609c6d6252d587b3e1a0160ad060338e1876ab70ba2
fetched_at: '2026-06-29T00:09:07.682239+00:00'
page_id: '384587591'
product: rm
source: tdn-rm
title: 3234429 DSAUGHSCC-819 Problemas no estoque relacionados ao métodos PEPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384587591
version: 2
---

# PROBLEMAS NO ESTOQUE RELACIONADOS AO MÉTODO PEPS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospilar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mapa de Dispensação | SavMapaDispensacao | |
| **Parâmetro(s):** | Informe os parâmetros utilizados. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZAPRAZAMENTO, SZMOVIESTOQUEITEM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

A implementação consiste em parametrizar o sistema para alocar lotes disponíveis do produto quando o lote associado não possuir saldo disponível.

O saldo que o sistema considera, é o saldo disponível do Backoffice menos a quantidade já confirmada para outras requisições, ou seja, é considerado o saldo em movimentação.

## Procedimento para Utilização

* Parametrização: Acesse o menu Opções / Parâmetros / Parâmetros Gerais, aba Estoques II, e marque o parâmetro "Executa o método PEPS no processamento do mapa". O sistema deve estar com o parâmetro "Utiliza dispensação horária por requisição" desmarcado e o "Busca automática (lote/validade) pelo método PEPS na requisição de MAT/MED." marcado.

* Para o cenário, é necessário prescrever um medicamento que possua pouco saldo em estoque, isso porque ao prescrever, o sistema alocará o próximo lote com saldo, porém ele não verifica se a quantidade é o suficiente para todos os itens e por isso acaba alocando o mesmo lote para os itens.

* Acesse o Mapa de dispensação  e selecione a requisição criada.
* Selecione os itens e gere o mapa.

* Dê um duplo clique em um dos itens do mapa gerado e confirme todos os itens sem utilizar código de barras (pelo botão de confirmar todos)

* Dê um duplo clique no item confirmado e veja o lote que está confirmado e a quantidade. Esta quantidade não existe no lote selecionado.
* Neste ponto, caso tenha saldo suficiente no lote, deve-se criar uma requisição diretamente na Movimentação de estoque e baixar de todo o saldo disponível do lote selecionado.
* Retorne no mapa e faça o processamento do mapa. Com o parâmetro marcado, o sistema procurará o próximo lote para substituir o anterior. Caso não tenha saldo suficiente, é exibida uma mensagem e o processo não segue.

* Para verificar o lote selecionado automaticamente, basta entrar no item novamente e dar duplo clique para ver o lotes.
