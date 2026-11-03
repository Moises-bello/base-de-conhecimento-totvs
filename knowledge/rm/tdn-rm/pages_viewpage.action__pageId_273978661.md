---
content_hash: a1d2a86bf9f10a491a29049bc121648e9d58c6154021042f4d2e5f83cbd2a503
fetched_at: '2026-06-29T00:08:31.959832+00:00'
page_id: '273978661'
product: rm
source: tdn-rm
title: DT Movimentações bibliotecárias - Melhorias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273978661
version: 108
---

# Movimentações

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentações | |
| **Cadastros Iniciais:** | Publicações / Exemplares / Usuários / Regras de empréstimos |
| **Parâmetro(s):** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER / ORACLE |
| **Tabelas Utilizadas:** | LEMPRESTIMOS |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada melhoria para facilitar, agilizar e tornar mais claro as operações de movimentações da biblioteca.

## Procedimento para Implantação

Estas melhorias estão disponíveis à partir da versão 12.1.17, não há necessidade de alguma configuração ou parametrização específica, a melhoria já é definitiva no sistema.

## Procedimento para Utilização

**Exemplo:**

No TOTVS Gestão Bibliotecária acesse o menu **Movimentações / Movimentações.**

**Situação dos exemplares**

Na tela de movimentações ao iniciar uma operação e esta retorne uma lista com usuários e exemplares ou só exemplares, os exemplares terão seu status informado, se está emprestado, disponível ou reservado, sendo que o status de reservado só será exibido quando existir um único exemplar disponível para reservas de uma publicação.

**Devoluções e renovações rápidas**

Ao informar um usuário que possui empréstimos ativos e que deseja fazer uma devolução ou renovação de todos os exemplares ao mesmo tempo, não será mais necessário informar exemplar por exemplar para fazer uma devolução ou renovação, agora é necessário somente informar o usuário para iniciar a operação, selecionar os exemplares desejados e informar se deseja devolver ou renovar, ao selecionar a opção estes serão transferidos para a operação selecionada, bastando apenas confirmar a operação. Assim o tempo de devolução ou renovação poderá ser reduzido sem a necessidade de informar todos os exemplares da operação para um determinado usuário, além de agilizar, permite também fazer a devolução de vários exemplares, renovações e até mesmo empréstimos em uma única tela.

Aviso

Ao identificar um usuário o sistema irá listar todos os empréstimos em andamento deste usuário, de todas as filias e unidades bibliotecárias que ele tiver permissão, porém as operações de devolução e renovação rápidas só serão executadas para os empréstimos da filial e unidade do contexto corrente, mesmo que sejam selecionados todos os empréstimos listados na tela.

**Devoluções não identificadas**

O sistema permite que exemplares sejam devolvidos sem informar o usuário, informando assim somente os exemplares, porém esta tela mostrava antes no lugar do usuário a opção de usuário não identificado, ocupando espaço desnecessário na tela, este espaço foi removido e é exibido agora somente os exemplares, também foi inserido a coluna com o nome do usuário, sendo que a coluna do nome do usuário e da foto do usuário permitem um clique que abrirá os dados do usuário da biblioteca para consulta e identificação, também foi inserido uma coluna identificando se os exemplares que estão sendo devolvidos possuem reservas ou não.

divs
