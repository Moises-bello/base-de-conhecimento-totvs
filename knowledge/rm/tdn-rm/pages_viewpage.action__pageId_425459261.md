---
content_hash: 9efeff9ced88c9376649282eb57dbaf72e96fb7f3723608d08c03d1175787531
fetched_at: '2026-06-29T00:09:34.844507+00:00'
page_id: '425459261'
product: rm
source: tdn-rm
title: Cutter / PHA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459261
version: 3
---

O Cutter/PHA é uma tabela de códigos que indicam a autoria de uma obra literária, utilizando de dados da publicações . O código Cutter é universal e possui o registro de combinações de número com sobrenome de  , o PHA (Prado, Heloísa de Almeida) são os códigos ajustados para os nomes brasileiros, as combinações destes dados geram códigos que auxiliam assim na localização dos exemplares dentro da biblioteca.

O cadastro dos códigos podem ser feitos diretamente pelo cadastro de Cutter/PHA (Tabelas auxiliares | Cutter/PHA) item a item ou podem ser feitos também através do utilitário de  .

**Geração do Cutter/PHA**  
 O Cutter/PHA pode ser gerado através do cadastro de publicações, é somente necessário ter a publicação cadastrada com as regras listadas abaixo e selecionar o botão ao lado do item Cutter/PHA no cadastro de publicações.

**Regras básicas para geração do Cutter/PHA**

**1 - Publicação com título principal e autor definidos.**

* Requisitos desta regra:
  + Publicação com título cadastrado.
  + Autor cadastrado com tipo de autor definido e que esteja definido como autor principal no cadastro da publicação.
* Regra:
  + O Cutter/PHA será formado pela primeira letra (em maiúsculo) do sobrenome do autor da publicação + número da tabela Cutter/PHA que mais se aproxima ao sobrenome do autor + primeira letra (em minúsculo) do título da publicação.
* Exemplo:
  + Autor: ALMEIDA, Marcelo Cavalcante
  + Título: Testemunho Político
  + Resultado: A447t

**2 - Publicação com título principal sem autor.**

* Requisitos desta regra:
  + Publicação com título cadastrado.
  + Autor não cadastrado ou sem tipo de autor definido e sem definição de autor principal no cadastro da publicação.
* Regra:
  + O Cutter/PHA será formado pela primeira letra (em maiúsculo) do título da publicação + número da tabela Cutter/PHA que mais se aproxima do título da publicação.
* Exemplo:
  + Autor: sem autor definido
  + Título: Testemunho Político
  + Resultado: T343

**3 - Publicação com título principal com autor usando apenas o primeiro nome.**

* Requisitos desta regra:
  + Publicação com título cadastrado.
  + Autor não cadastrado ou sem tipo de autor definido e sem definição de autor principal no cadastro da publicação.
* Regra:
  + O Cutter/PHA será formado pela primeira letra (em maiúsculo) do Nome do autor + número da tabela Cutter/PHA que mais se aproxima do título da publicação + a primeira letra (em minúsculo) do título da publicação.
* Exemplo:
  + Autor: Paulo
  + Título: Força
  + Resultado: P328f

**Observações**

* Se o título da publicação iniciar com valor numérico, o primeiro número será convertido por extenso e assim será utilizado a primeira letra do nome do número. Caso a publicação possua um idioma o sistema irá considerar os seguintes idiomas na conversão para o nome por extenso do número: português, alemão, inglês, espanhol e francês.

Assim por exemplo caso o título da publicação seja "4 tools..." e estiver com o idioma definido como inglês no cadastro da publicação o sistema irá utiliza a letra "F" de four no lugar da "Q" de quatro ou do numeral "4".

* Se o título da publicação começar com algum artigo nos idiomas listado, os mesmos serão desconsiderados e será considerado a primeira palavra após o artigo que inicia o título:

Artigos desconsiderados:

* + Português: o, a, os, as, um, uma, uns, umas.
  + Alemão: der, die, das.
  + Inglês: a, an, the.
  + Espanhol: el, los, las, la.
  + Francês: le, les, la, du, des.
* Se o tipo do autor definido em seu cadastro for o tipo institucional, sempre será utilizada a primeira caractere do nome todo, independente se estiver normalizado ou não.
* Se a natureza da referência for Livre ( , será utilizado além da primeira letra do autor, as duas próximas letras do nome do autor e também os três primeiros caracteres do título principal.
