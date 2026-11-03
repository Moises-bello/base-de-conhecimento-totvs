---
content_hash: 0eb024c1a508f40ce54556208b5aebf38f0842b691c8e85584a7e5547558eb1b
fetched_at: '2026-06-28T21:35:18.831485+00:00'
page_id: '185739563'
product: fluig
source: tdn-fluig
title: Componente Seleção de papéis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739563
version: 16
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Seleção de papéis**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma TOTVS Fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Seleção de papéis

---

Para habilitar o componente **Seleção de papéis** no seu *widget*, adicione a seguinte propriedade no  do *widget*:

xml

O componente possui as opções:

* **multiselect**: ***true***para que seja possível selecionar mais de um registro; ***false***para que seja possível selecionar apenas um registro;
* **required**: ***true***para que seja possível avançar apenas se algum registro estiver selecionado; ***false***para obrigar a selecionar algum papel.

## Utilização básica

---

A utilização deste componente pode ser feita da seguinte maneira:

js

**Tela exibida ao executar o componente**
