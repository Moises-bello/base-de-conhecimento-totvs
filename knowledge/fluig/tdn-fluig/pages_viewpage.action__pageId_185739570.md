---
content_hash: ee4a33fce847c93c1a56188ad9f4ce7399dd6d549619fadae51dd6a679c8e48f
fetched_at: '2026-06-28T21:35:18.838371+00:00'
page_id: '185739570'
product: fluig
source: tdn-fluig
title: Componente Seleção de sub grupos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739570
version: 13
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Seleção de sub grupos**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma TOTVS Fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Seleção de sub grupos

---

Para habilitar o componente **Seleção de sub grupos** no seu *widget*, adicione a seguinte propriedade no  do *widget*:

xml

O componente possui as opções:

* **group:**grupo pai dos sub grupos a serem selecionados;
* **multiselect**: ***true***para que seja possível selecionar mais de um registro; ***false***para que seja possível selecionar apenas um registro.
* **required**: ***true***para que seja possível avançar apenas se algum registro estiver selecionado; ***false***para obrigar a selecionar algum sub grupo.

## Utilização básica

---

A utilização deste componente pode ser feita da seguinte maneira:

js

**Tela exibida ao executar o componente**
