---
content_hash: 3a4927e5e2993d0f3920e2ecfccd3c7088ad72273d28a376f3e8b09fd2a38f99
fetched_at: '2026-06-28T21:35:18.834699+00:00'
page_id: '185739566'
product: fluig
source: tdn-fluig
title: Componente Seleção de grupos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739566
version: 21
---

# Índice

4true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Seleção de grupos**. O objetivo é apresentar o seu funcionamento e o detalhamento dos parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma TOTVS Fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Seleção de grupos

---

Para habilitar o componente **Seleção de grupos** no *widget*, adicione a seguinte propriedade no  do *widget*:

xml

O componente possui as opções:

* **multiselect**: ***true***para que seja possível selecionar mais de um registro; ***false***para que seja possível selecionar apenas um registro;
* **required**: ***true***para que seja possível avançar apenas se algum registro estiver selecionado; ***false***para obrigar a selecionar algum grupo.

## Utilização básica

---

A utilização deste componente pode ser feita da seguinte maneira:

js

**Tela exibida ao executar o componente**
