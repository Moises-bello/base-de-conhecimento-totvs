---
content_hash: 98e8eb35b37cd3038a057367947ec1fe1b3cb2d3f12722aa04eba8f9d0173851
fetched_at: '2026-06-29T00:05:58.825549+00:00'
page_id: '189303703'
product: rm
source: tdn-rm
title: Filtro por data
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtro+por+data
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Filtro de Relatório |
| **Subprocesso** | **:** | Utilizando filtro por data |
| **Data da publicação** | **:** | 26/05/2015 |

|  |  |
| --- | --- |
| Status do Documento: | Em Produção |
| Data: | 26/05/2015 |
| Versão: | 1.0 |
| Versão Anterior: | 1.0 |
| Autores: | [Diego Henrique Almeida de Oliveira](http://tdn.totvs.com/display/~diego.henrique)  [Fábio Augusto Amaral Melo Nunes](http://tdn.totvs.com/display/~fabio.nunes)  [Welbert Marques Silva](http://tdn.totvs.com/display/~welbert.silva)  [Wesley Avelino De Carvalho](http://tdn.totvs.com/display/~wesley.carvalho) |

# Objetivo

A finalidade do filtro por data como o próprio nome já diz, é executar em relatório um filtro que possua como parâmetro um campo de data.

# Como Funciona

DeckPasso 1

Na guia Gestão, clique em Rm Reports e crie um novo relatório com os dados iguais aos da imagem abaixo.

Passo 2

Após abrir a pagina de edição do relatório, clique no campo "Adicionar Fonte de Dados"

Passo 3

Na aba de "Tabelas da Base" escreva na caixa de pesquisa o nome da tabela funcionários (PFUNC) e adicione a tabela ao seu relatório conforme exemplo abaixo

Passo 4

Adicione então a seguir os campos Nome e Data retornados pela tabela inserida ao relatório conforme o exemplo abaixo

Passo 5

Após adicionar os campos, clique em Filtros (ao lado do campo Adicionar Fonte de Dados) e insira um novo filtro clicando no lookup do campo "Filtros". Selecione o filtro existente e clique em modificar.

Passo 6

Adicione a seguinte condição ao filtro: Data de Admissão >= 01/01/2000. Insira está condição clicando no lookup do campo valor, pois este irá lhe trazer um calendário para que possa ser selecionada a data do filtro

Passo 7

Depois de executado os processos anteriores, salve e gere o relatório. Na visualização dele, os funcionários retornados deverão ser aqueles que possuam data de admissão maior ou igual ao dia 01/01/2000
