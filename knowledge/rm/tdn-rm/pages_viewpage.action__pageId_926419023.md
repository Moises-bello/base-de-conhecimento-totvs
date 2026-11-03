---
content_hash: 57ee898119b7ba51afa2196d778b040bed34c5fc2d40391f6ed5cf88f9726af9
fetched_at: '2026-06-29T00:12:07.485619+00:00'
page_id: '926419023'
product: rm
source: tdn-rm
title: Relatórios - Relatório Dinâmico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=926419023
version: 2
---

### Introdução

---

Visando dar flexibilidade na execução dos relatórios dentro do RM, criamos a opção de geração dinâmica de relatórios, onde, através de parâmetros criados diretamente no relatório, teremos uma execução do mesmo mais direcionada e customizável.

A geração de um relatório dinâmico depende de alguns parâmetros que devem ser diretamente aplicados no relatório que será executado.

A lista de campos disponíveis é a abaixo:

* XCOMPRADOR
* XCLIENTE
* XLOCADOR
* XLOCATARIO
* XIDLAN
* XIMOVEL
* XCONTRATOLOC
* XEMPREENDIMENTO
* XUNIDADE
* XSUBUNIDADE

Todos estes campos estão disponíveis para confecção do relatório dinâmico e podem ser também definidos como lookup ou seleção múltipla.

* LKP\_CAMPO: Apresenta uma lookup da tabela passado como parâmetro. Exemplo: **LKP\_XCONTRATOLOC**
* MRE\_XCONTRATOLOC: Deverá apresentar uma aba de seleção múltipla, da tabela escolhida, na geração do relatório. Exemplo: **MRE\_XCONTRATOLOC**

Há também a possibilidade de inserção de parâmetros do tipo DateTime, Texto ou Int.

### Exemplo de parâmetros que serão gerados no relatório dinâmico

---

Na edição de relatórios, posso incluir um novo parâmetro e defini-lo da seguinte maneira:

Veja que no caso, estou definindo que quero uma lookup da tabela XLOCATARIO. A descrição desse parâmetro será *"Selecione o Locatário"*

Também estou definindo um parâmetro dateTime que vou chamar de *"Competência":*

O resultado na execução dinâmica é o seguinte:
