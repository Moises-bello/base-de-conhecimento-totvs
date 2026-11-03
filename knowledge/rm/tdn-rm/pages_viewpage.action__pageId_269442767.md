---
content_hash: b2f67c952b91d48366f4a21dc6d481ee03a57ad41213dbf2a1792ee0c1069101
fetched_at: '2026-06-29T00:08:23.027274+00:00'
page_id: '269442767'
product: rm
source: tdn-rm
title: DT Filtros de Itens Associados ao Atendimento e ou Requisição na Devolução
  de Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269442767
version: 114
---

# **Filtros de itens associados ao atendimento e/ou Requisição na Devolução de Paciente**

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Estoques / Movimentação de Estoque / Devolução p/ Paciente | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® / Oracle® |
| **Tabelas Utilizadas:** | SZMOVIESTOQUE, SZMOVIESTOQUEITEM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A melhoria consiste em permitir que o  TOTVS Gestão Hospitalar apresente apenas os itens associados ao atendimento e/ou à requisição em movimentações do tipo Devolução para Paciente, com o objetivo de agregar melhoria operacional ao sistema.

## Procedimento para Utilização

### Parametrização

Para que o sistema realize o filtro dos itens associados ao atendimento e/ou a requisição em movimentações do tipo Devolução p/ Paciente siga os seguintes passos para realizar a parametrização:

1. Acesse o menu **Opções** / **Parâmetros**/ **Parâmetros Gerais**.
2. Acesse a aba **Estoque.**
3. Marque a opção **Filtra Itens Associados ao atendimento e/ou à Requisição**.
4. Clique em **Grava** e em seguida, clique em **Fecha**.
5. Acesse o menu **Estoques** / **Movimentações de Estoque**.
6. Clique em **Incluir\***.
7. Preencha as informações\* obrigatórias da aba **Identificação.**
   1. \*Quando preenche-se o campo **Req. associada** as informações do grupo **Aplicação** serão preenchidos automaticamente.
   2. Selecione o **Tipo de Movimento** de **Devolução p/ Paciente**.
8. Acesse a aba **Itens da Movimentação.**
9. Clique em ****Incluir****.
10. Acesse o campo **Código** e aperte a tecla **Tab**.
11. Na tela de pesquisa preencha a informação do item que deseja realizar a devolução e clique em **Pesquisar**.
    1. No cenário parametrizado o sistema pesquisa apenas os itens associados ao atendimento e/ou à requisição relacionados à informação preenchida na pesquisa.

Observação

Sem a parametrização da funcionalidade, o resultado do item 7 apresentaria todos os itens cadastrados no sistema conforme figura abaixo:

divs
