---
content_hash: 38c767c8f014ec061acc8ffdd7a6f61a9cba1e37a3912d51d0674e1c2e05c320
fetched_at: '2026-06-28T21:35:17.310269+00:00'
page_id: '1040986447'
product: fluig
source: tdn-fluig
title: 5 Erros comuns no desenvolvimento em widgets no TOTVS Fluig
type: documentation
url: https://tdn.totvs.com/display/fluig/5+Erros+comuns+no+desenvolvimento+em+widgets+no+TOTVS+Fluig
version: 39
---

# Erros comuns no desenvolvimento de *widgets*

---

Desenvolver *widgets* no TOTVS Fluig exige o cumprimento de padrões arquiteturais específicos da plataforma (FreeMarker e Fluig Style Guide). Ignorar essas regras frequentemente causa falhas silenciosas de renderização, lentidão na interface, quebra de código ao migrar entre ambientes (Homologação para Produção) e conflitos visuais.

Este guia documenta os 5 erros mais recorrentes entre desenvolvedores e apresenta as melhores práticas estruturais para evitá-los, para isso vamos ter como base um **exemplo prático**!

Download do exemplo:

Caso você tenha interesse em fazer o *download* do projeto que criamos para este exemplo, .

## Erro 1 - Escopo da super *widget* e o perigo das múltiplas instâncias

---

A arquitetura do TOTVS Fluig é rigorosa no carregamento e instanciamento de uma *widget* na página. Se a estrutura global não for respeitada, o componente falhará ao renderizar. Os principais equívocos incluem:

* **Usar ES6 na declaração principal:** a arquitetura do Fluig requer um escopo global que apenas a declaração `var` provê na raiz do arquivo. Utilizar `const` ou `let` para declarar a variável da SuperWidget impede de instanciar o objeto no `window`.

* **Funções soltas:** é ideal manter toda a implementação dentro da SuperWidget e evitar criar funções fora dela, caso contrário, você não terá acesso aos atributos fornecidos por ela (como o `this.instanceId`).

* **Divergência entre o ID da DIV principal e a variável JS:** o `id` da `div` encapsuladora nos arquivos `view.ftl` e `edit.ftl` possui a mesma nomenclatura base da variável JavaScript. Exemplo: se a div é `<div id="wExemplosPraticos_${instanceId}">`, a variável deve ser `var wExemplosPraticos = SuperWidget.extend({...});`.

* **Ignorar o suporte a múltiplas instâncias na mesma página:** um desenvolvedor deve assumir que sua *widget* pode ser inserida duas ou mais vezes na mesma página. Para que ações de clique e manipulações de DOM não afetem a *widget* errada, **sempre** concatene o `${instanceId}` nos seletores de ID e utilize as funções de binding nativas.

1. Estrutura correta de instanciação:

Sempre inicie sua *widget* com `var` e o nome idêntico ao código do projeto:

jsNo javascripttrue2. Cuidado com callbacks assíncronos (a perda do this):

Em requisições AJAX, o contexto do `this` muda, fazendo você perder o acesso ao `this.instanceId`.

jsNo javascripttrue

O exemplo abaixo mostra o uso de **Arrow Functions** (`success: (data) => { ... }`), que é a abordagem moderna e limpa. Ela herda o `this` automaticamente da *widget*, eliminando a necessidade de criar variáveis de escape (como o antigo `var that = this`).

jsNo javascripttrue {
console.log(this.instanceId); // Acessível com sucesso!
}
});
}]]>

## Erro 2 - Deixar dados fixos (Hardcoded) e ignorar o Style Guide

---

**1. Hardcode de dados e ambientes**

Anotar IDs fixos (pastas, formulários, *logins*) no código Javascript fará com que a *widget* quebre imediatamente ao ser exportada para outro ambiente. Ex.: de Homologação para Produção, onde os IDs são diferentes.

A solução correta é criar uma tela de configuração (`edit.ftl`) para o administrador salvar esses dados usando a API `UPDATEPREFERENCES` nativa do Fluig e depois resgatá-los no `view.ftl` via FreeMarker.

No arquivo Javascript (`.js`), capture e salve os dados:

xmlJavascript {
FLUIGC.toast({ title: 'Sucesso', message: 'Preferências salvas!', type: 'success' });
}
}, this.instanceId, preferences);
}]]>

**2. A importância da identidade visual e uso do Style Guide**

Um erro de UI/UX é criar telas com CSS customizado (`<style>`) ou ignorar os componentes oficiais. O usuário precisa sentir que sua *widget* é uma funcionalidade que faz parte do Fluig e não um sistema terceiro colado na tela.

Para isso, você deve usar as classes do **Fluig Style Guide**. Veja como nosso código funcional aplica isso na prática:

* **Estrutura de painéis:** envelopamos a *widget* com as classes `.panel.panel-primary`, `.panel-heading` e `.panel-body`. Isso cria a borda, o cabeçalho e a sombra idênticos aos portais nativos.

* **Grid System responsivo:** o *layout* não flutua de forma aleatória. Ele respeita a grade do Style Guide(`.row` > `.col-md-12`, `.col-md-8`), garantindo que a barra de busca se adapte perfeitamente, tanto no celular quanto em monitores grandes.

* **Classes utilitárias (Helpers CSS):** evite criar CSS duplicado para margens ou fontes. Utilizamos os *helpers* oficiais do Fluig, como `fs-mb-32` (Margin-Bottom de 32px), `fs-p-16` (Padding de 16px) e `fs-font-16` (tamanho de fonte 16px).

* **Iconografia:** elementos de interface usam as fontes oficiais do produto, como `flaticon-aim` e `flaticon-open-package`, garantindo padronização.

Exemplo do `edit.ftl` usando o Style Guide e capturando as preferências:

xml

### Configurações da Busca

ID da Pasta Raiz

Salvar Configurações
