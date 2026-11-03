---
content_hash: b21642bf8f71161cdd744ac239deb972311c9325bcad530f8e705a11fd03bec0
fetched_at: '2026-06-28T21:35:23.472022+00:00'
page_id: '255755875'
product: fluig
source: tdn-fluig
title: DES - Implementação de código Javascript em formulário com abas de navegação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=255755875
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

**Versão:** Todas as versões

# Ocorrência

Código JavaScript não funciona em nav-tabs nas abas secundárias.

# Causa

O código JavaScript é criado em tempo de carregamento da página. Como a <div> com código está em uma aba secundária, ela não é visível neste momento.

# Solução

Para resolver este caso dispomos de duas documentações no Style Guide: [Navs](https://style.fluig.com/components.html#nav) e [Togglable tabs](https://style.fluig.com/javascript.html#tabs).

Como exemplo, vamos colocar um componente [*Chart*](https://style.fluig.com/chart.html) em uma aba secundária.

As *tabs* aceitam eventos, portanto para mostrar um componente em uma aba não selecionada, é necessário adicionar:

js

O comando $('a[data-toggle="tab"]') pode ser alterado para $('a[href="#id\_tab"]') aonde você vai utilizar o *id* da sua *tab*.

Para aplicar o gráfico em uma aba diferente da primeira, ficaria assim:

js1ScriptxmlHTML
