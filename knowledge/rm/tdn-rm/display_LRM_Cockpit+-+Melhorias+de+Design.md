---
content_hash: cb7c48389cab4c626d405b65e1cadc7ed7ad4967bbad76655c270c61e1653fc1
fetched_at: '2026-06-29T00:08:58.944860+00:00'
page_id: '362448647'
product: rm
source: tdn-rm
title: Cockpit - Melhorias de Design
type: documentation
url: https://tdn.totvs.com/display/LRM/Cockpit+-+Melhorias+de+Design
version: 6
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo:

---

     Este documento tem por objetivo especificar as **Melhorias de Design realizadas no Cockpit**.

# 1 - Especificação:

---

.confluence-information-macro {
width: calc(100% - 25px);
background: #fff !important;
border: 0;
-moz-border-radius: 0px !important;
-webkit-border-radius: 0px !important;
border-radius: 0px !important;
color: #333;
margin: 10px 0 1em 0;
min-height: 20px;
padding: 10px;
position: relative;
}
.confluence-information-macro p.title{
padding-left: 20px;
margin-top: 0px;
margin-bottom: 5px;
}
.confluence-information-macro .confluence-information-macro-icon.aui-iconfont-error{
color: #fff;
}
.confluence-information-macro-warning{
background-color: #d04437 !important;
color: #fff;
}
.confluence-information-macro-information{
border: 1px solid #aab8c6 !important;
}
]]>

Para acessar a tela do **Cockpit** acesse, em qualquer módulo, o Menu**Ambiente**>>**Cockpit**,

# 1.1 - Desenho de tela anterior:

---

# 

# 1.2 - Melhorias realizadas no desenho da tela:

---

## 1.2.1 - Indicativo de Situação do Job Server e Grupo Informações Gerais

---

Foi adicionado um Ícone no topo à direita do Contêiner que representa a situação do Job Server:

**Legendas**

 Iniciado

 Parado

 Situação desconhecida

Foi adicionado um novo grupo de informações que contém as informações gerais sobre o Job Server e o Servidor.

* **Situação do Job Server:** É o mesmo valor do ícone do topo, só que por extenso.;
* **Somente Jobs Locais:** Se remete à configuração **Somente Jobs Locais**;
* **Situação do Servidor:**Indica se o Servidor está ou não operante;
* **Versão do Servidor:**Indica a versão do RM instalado no Servidor.

## 1.2.2 - Botão Expandir / Minimizar Contêineres

---

Na tela do **Cockpit,**observe que um novo botão foi adicionado:

Ao clicar nesse botão, todos os grupos de informações de todos os contêineres serão expandidos ou minimizados. Podem existir usuários que necessitem de analisar informações de diversos jobs servers ao mesmo tempo, e para isso teria que clicar em expandir em vários grupos de informações o que oneraria a navegabilidade, com esse botão, a análise de informações poderá ser realizada devidamente.

**Contêiner minimizado**

**Contâiner expandido**

## 1.2.3 - Menu de Contexto

---

Foi adicionado no topo à direita do Contêiner um ícone de Menu.

As opções são:

* Expandir / Minimizar Contêiner: Diferentemente do Expandir / Minimizar Todos Contêineres, essa funcionalidade expande ou minimiza os grupos de informações apenas do contêiner atual.
* Remover Servidor: Executa o processo de Exclusão de Servidor, o servidor vinculado ao Contêiner atual é excluído da tabela GKNOWNSERVER.
* Limpar Cache do Servidor: Executa o Processo de Limpeza de Cache para o servidor vinculado ao Contêiner atual.
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.21 ou Superior

false

**Processo:** Melhorias de Design - Cockpit

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
