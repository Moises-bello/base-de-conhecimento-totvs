---
content_hash: 9fbc78e17aaf35caa377c04022075c98e542d7b63a07c8771ac590dc017f357d
fetched_at: '2026-06-28T21:35:24.928701+00:00'
page_id: '272407097'
product: fluig
source: tdn-fluig
title: Componente Segurança de itens de aprendizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272407097
version: 16
---

# Índice

4true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Segurança de itens de aprendizado**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma TOTVS Fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Segurança de itens de aprendizado

---

O componente **Segurança de itens de aprendizado** tem como objetivo facilitar e padronizar a implementação da segurança dos itens de aprendizado em *widgets*.

## Utilização básica

---

Para habilitar o componente de seleção de usuário no seu *widget*, adicione a seguinte propriedade no  do *widget*:

xml

O componente possui os parâmetros:

* **containerId**: Id do elemento HTML que receberá o contêiner do componente de segurança (obrigatório);
* **itemId**: Id do item do catálogo para carregar as definições de segurança (opcional);
* **showRadioButtons: *true***para exibir os *radio buttons*referentes a configuração de herança do item, ***false***para não exibir (opcional, valor padrão é ***true***);
* **itemType**: tipo de item do catálogo para que, quando for informado o código do item (itemId), traga as definições de segurança corretas (obrigatório).

Valores disponíveis para o parâmetro itemType

* 'CatalogItem' para itens do catálogo de treinamentos e trilhas (pasta, treinamento, trilha e *link*);
* 'DisciplineItem' para itens do catálogo de disciplinas e turmas (pasta, disciplina e *link*);
* 'DisciplineClass' para itens do catálogo de disciplinas e turmas (turma e turma modelo);
* 'AssessmentCatalogItem' para itens do catálogo de tópicos e questões (tópicos e questões).

A utilização deste componente pode ser feita da seguinte maneira:

js

## Métodos disponíveis

---

Os métodos disponíveis para utilização são:

**.getSelectRadio(); - Retorna o valor do botão *radio* selecionado contendo o tipo de herança de segurança**

jsEclipsegetSelectRadio()

**.getPermissions(); - Retorna todas as permissões do item (exibidas em tela e salvas no banco de dados)**

jsEclipsegetPermissions()

**.getRestrictions(); - Retorna todas as restrições do item (exibidas em tela e salvas no banco de dados)**

jsEclipsegetRestrictions()

**Tela exibida ao executar o componente**

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
