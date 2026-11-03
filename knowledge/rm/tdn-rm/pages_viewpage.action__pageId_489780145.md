---
content_hash: 18a59a075b1ca9e3226ba9f7742202fbc4b3962a8f57362c9ccf4fa6156de3c7
fetched_at: '2026-06-29T00:10:20.204638+00:00'
page_id: '489780145'
product: rm
source: tdn-rm
title: Utilizando "Onvalidate" em um controle do Metadados.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489780145
version: 11
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

O Onvalidate permite que uma Fórmula Visual seja disparada no momento que o foco deixa um determinado controle.

**02. EXEMPLO DE UTILIZAÇÃO**

**•** Para utilizar o **OnValidate**, você deve acessar a aba "**Apresentação**" da sua "**Apresentação de Formulários**":

**•** Nesta aba, você deve selecionar o controle em que deseja que uma Fórmula Visual seja disparada quando o foco deixar esse controle:

**•** Feito isso, você deve acessara aba "**Eventos**" para configurar seu **OnValidate**:

**•** Clique no botão **(...)** para selecionar a Fórmula Visual que será executada quando o foco deixar o controle:

**•** Feito isso, você deve salvar sua "**Apresentação de Formulários**" e gerar seu projeto metadados novamente.

**•** Acessando sua tela criada pelo metadados, quando seu cursor ("**Foco"**) abandonar o controle (No nosso caso exemplo, o controle escolhido foi o campo "**Código**") a Fórmula Visual será executada (No nosso exemplo, a fórmula visual apenas gera uma exceção):

**•** Pode ser utilizado para os campos que sejam de um tipo de controle diferente de caixa de seleção também.  
Lembrando que o evento onde a fórmula visual é disparada é quando o foco deixa o controle.
