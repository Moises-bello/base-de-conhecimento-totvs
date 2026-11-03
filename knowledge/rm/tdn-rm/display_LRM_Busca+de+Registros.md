---
content_hash: 568e7db7d1dd49533210a9ed8a39d1ff72041d14d1c772add44aa1b0d7a84082
fetched_at: '2026-06-29T00:09:11.399143+00:00'
page_id: '403746946'
product: rm
source: tdn-rm
title: Busca de Registros
type: documentation
url: https://tdn.totvs.com/display/LRM/Busca+de+Registros
version: 15
---

**CONTEÚDO**

**20**

# **01. VISÃO GERAL**

A busca de registros é uma ferramenta que deve ser utilizada para buscar registros em telas que possuem inúmeros registros.

Ao clicar no binóculo será aberta a ferramenta de busca.

No primeiro campo deve-se escolher em qual campo do cadastro será efetuada a pesquisa. No segundo campo deve-se inserir o valor a ser pesquisado.

Para facilitar a pesquisa a medida que se for digitando será executada a busca nos registros.

Caso a busca não retorne nenhum registro será informado ao usuário que não foram encontrados registros com os dados informados.

Um recurso que a Busca permite utilizar é o do %(percentual). Para buscar um valor que contém o conteúdo digitado.

Comando % (LIKE)

Ao utilizar a diretiva **%**, deve-se atentar para:

* Em toda pesquisa realizada nesse campo, o **%** é adicionado internamente ao **final do texto**, não sendo necessário sua repetida inserção ao final da pesquisa.
* O **RM** não dá suporte ao uso do **% entre as letras do texto da pesquisa**. Ex: [%tot%sa].

# **02. EXEMPLO DE UTILIZAÇÃO**

        Vamos fazer a busca pela palavra Mestre. No campo texto insira o valor %ME. Com essa busca será informado todos os registros que contem em qualquer parte da string as letras ME.

# **03. AUTO FILTRO DE LINHA**

Realiza um filtro com as informações já exibidas na visão.

false

**Versão:** 12.01.XX
