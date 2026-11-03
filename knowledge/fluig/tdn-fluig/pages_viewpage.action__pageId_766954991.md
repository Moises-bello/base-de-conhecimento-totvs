---
content_hash: d335e8a685a4897427a4a04ffde2b44a9661c6ce1f0a07b02e4b2537591b6b3e
fetched_at: '2026-06-28T21:35:29.787974+00:00'
page_id: '766954991'
product: fluig
source: tdn-fluig
title: Componente de visualização de documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=766954991
version: 19
---

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Visualização de documentos**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

## Estrutura Básica

---

Como pode-se notar na estrutura básica, o componente recebe basicamente um parâmetro:

Veja o exemplo abaixo:

jsEclipseEstrutura básica do componente

O parâmetro espera um objeto contendo até quatro atributos, onde apenas um é obrigatório:

Parâmetro config

## Utilização Básica

---

Um exemplo da utilização básica abaixo:

jsEclipseminhawidget.js

* No arquivo [application.info](http://application.info/) de seu *widget*, adicione o componente como dependência. Como no exemplo abaixo:

bashEclipseapplication.info

# Visualização de documento em comunidade ou formulários

---

O componente **Visualização de documento** tem como objetivo facilitar a visualização de documentos no Fluig plataforma, restando para o desenvolvedor somente configurar o *plugin* para montar sua lógica de negócio. 

Caso a forma antiga estiver sendo utilizada, recomendamos que a atualização seja feita seguindo os passos deste documento.

#f2f2f2#f2f2f2Exemplo utilizando a forma antiga

```
try {  
    var cfg = {  
        url: "/ecm_documentview/documentView.ftl",  
        maximized: true,  
        title: "Imprimir",  
        callBack: function () {  
            parent['ECM'].documentView.getDocument('7', '1000');  
        },  
        customButtons: []  
    };  
    parent['ECM'].documentView.panel = parent['WCMC'].panel(cfg);  
} catch (error) {  
    console.log("error", error);  
}
```

Caso esteja usando em Formulários, importe o arquivo como no exemplo abaixo:

]]>
