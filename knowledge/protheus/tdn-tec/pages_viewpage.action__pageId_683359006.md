---
content_hash: e011b899807b086b9b892afdb06ffab505f38682c1acbc064f217ce7185ee4ed
fetched_at: '2026-07-02T19:24:27.829510+00:00'
page_id: '683359006'
product: protheus
source: tdn-tec
title: WebApp - Web Components (Versão 9.0.0)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683359006
version: 15
---

## **Top**

Atenção

Esta versão é compatível com o Application Server 20.3.0.x (Harpia) e superior.  
Para utilizar o webapp na release 12.1.33 é necessário estar com a lib 20221010 ou superior.

* ###
* ###
* ###
* ###
* ###

# **webapp WebApp ()**

---

Com o TOTVS | SmartClient HTML, fica ainda mais fácil ter acesso ao ERP da sua empresa! O aplicativo provê o acesso a interface via http, podendo utilizar a maioria dos navegadores de dispositivos como tablets e notebooks para gerenciar sua empresa!

O TOTVS | SmartClient HTML teve sua interface toda reescrita nessa nova versão, utilizando Web Components e Lit Element, o que possibilitou além de uma melhora no código, um ganho de performance considerável para o usuário final (verifique na sessão )

Consulte a lista dos **[navegadores homologados](https://tdn.totvs.com/display/tec/SmartClient+HTML+%28WebApp%29+-+Navegadores+homologados)** para o SmartClient WebApp.

# **webcomponents Web Components ()**

---

Web Components é uma suíte de diferentes tecnologias que permite a criação de elementos customizados reutilizáveis — com a funcionalidade separada do resto do seu código — e que podem ser utilizados nas aplicações web.

Visando a reutilização de código e simplificação de marcação customizada, os Web Components utilizam três tecnologias principais, que podem ser utilizadas em conjunto, para criar elementos customizados, com funcionalidade encapsulada, que podem ser reutilizados onde for necessário sem preocupação com conflito de código. Essas tecnologias são:

* **Custom elements:** Um conjunto de APIs JavaScript que permite definir elementos customizados e seus respectivos comportamentos, podendo ser utilizados de diferentes formas na interface da aplicação.
* **Shadow DOM:** Um conjunto de APIs JavaScript para incorporar uma árvore DOM "fantasma" encapsulada a um elemento — que é renderizada separadamente do DOM do documento principal — e controlar a funcionalidade associada. Nesse caso, você pode manter os recursos de um elemento privados, fazendo com que seu comportamento e estilo possam ser escritos sem medo de causar conflito com outras partes do documento.
* **HTML templates:**Os elementos `<template>` e `<slot>`  permitem que você escreva templates de marcação que não são exibidas na página. Elas podem então ser reutilizadas várias vezes como modelo de estrutura de um elemento customizado.

Referência: [Web Components | MDN (mozilla.org)](https://developer.mozilla.org/pt-BR/docs/Web/Web_Components)

# **lit Lit ()**

---

Lit é uma biblioteca simples para construir Web Components rápidos e leves que possibilitam uma alta performance em suas aplicações Web.

No núcleo do Lit está uma classe base de componentes que fornece estado reativo, estilos associados ao escopo, e um sistema de modelo declarativo que é minúsculo, rápido e expressivo.

A primeira coisa a saber sobre o Lit é que **cada Lit Element é um Web Component**. Os Web Components têm o superpoder da interoperabilidade: apoiados nativamente por navegadores, os Web Components podem ser usados em qualquer ambiente HTML, com qualquer estrutura.

Isso faz do Lit uma escolha ideal para desenvolver **componentes compartilháveis ou sistemas de design**. Os Lit Elements podem ser usados em vários aplicativos e sites, mesmo que esses aplicativos e sites sejam construídos em uma variedade de stacks front-end. Os desenvolvedores do site que usam Lit Element não precisam escrever ou mesmo ver qualquer código Lit; eles podem apenas usar os componentes da mesma maneira que eles fazem com elementos HTML incorporados.

Lit também é perfeito para **melhorar progressivamente sites HTML básicos**. Os navegadores reconhecerão os componentes Lit na sua marcação e os inicializarão automaticamente.

Você também pode construir **aplicativos altamente interativos e ricos em recursos** a partir de Lit Element, assim como você faria com uma estrutura como React ou Vue. Os recursos e a experiência do desenvolvedor Lit são comparáveis a essas alternativas populares, mas o Lit minimiza o lock-in, maximiza a flexibilidade e promove a manutenção, abraçando o modelo de componente nativo do navegador.

Referência: [What is Lit? – Lit](https://lit.dev/docs/)

# **comparativo**

# **Comparativo de Performance entre as versões ()**

---

Após a reescrita da interface utilizando a tecnologia Lit Element, foram realizados vários testes de performance utilizando o ERP TOTVS Protheus; abaixo segue uma amostra desses testes, demosntrando a melhoria de performance entre a versão anterior e a nova versão.

| Interface Anterior | Interface Nova | Componente |
| --- | --- | --- |
|  |  | TCBrowse **2000 colunas** |
|  |  | TCBrowse **2000 colunas** |
|  |  | TTree **4000 linhas x 8 colunas** |
|  |  | TTree **4000 linhas x 8 colunas** |

# **visual**

# **Comparativo Visual entre as versões ()**

---

Após a reescrita da interface utilizando a tecnologia Lit Element, alguns componentes sofreram uma ligeira modificação em seu estilo, como pode ser visto abaixo:

| Interface Anterior | Interface Nova | Componente |
| --- | --- | --- |
|  |  | Grid |
|  |  | Calendário |
|  |  | cGetFile |
|  |  | TGet / TFolder |
|  |  | Relatório |
