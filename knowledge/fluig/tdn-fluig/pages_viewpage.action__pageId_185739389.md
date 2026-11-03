---
content_hash: 8056e42da8a637c5e8e466474f65256b8f59e7e40a7f1ec0d1d56727004f4d54
fetched_at: '2026-06-28T21:35:18.827976+00:00'
page_id: '185739389'
product: fluig
source: tdn-fluig
title: Componente Seleção de usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739389
version: 25
---

# Índice

4true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Seleção de usuários**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma TOTVS Fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Seleção de usuários

---

O componente **Seleção de usuários** oferece a possibilidade do usuário selecionar um ou mais usuários para alguma necessidade dentro de seu componente ou *widget*.

## Utilização básica

---

Para habilitar o componente de seleção de usuário no seu *widget*, adicione a seguinte propriedade no  do *widget*:

xml

O componente possui as opções:

* **multiselect**: ***true***para que seja possível selecionar mais de um registro; ***false***para que seja possível selecionar apenas um registro;

* **required**: ***true***para que seja possível avançar apenas se algum registro estiver selecionado; ***false***para obrigar a selecionar algum usuário.

* **onlyActiveUsers**: ***true*** para que apenas usuários ativos sejam apresentados; ***false*** para que todos os usuários cadastrados sejam apresentados. O padrão é *false*, portanto se este parâmetro não for informado, todos os usuários serão listados.

A utilização deste componente pode ser feita da seguinte maneira:

js

**Tela exibida ao executar o componente**
