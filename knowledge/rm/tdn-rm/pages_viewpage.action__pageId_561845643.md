---
content_hash: 1340e57b37d12a50404d75c9b1006e9cb73f96b267f71f3c7394cc29ee2a79b4
fetched_at: '2026-06-29T00:10:48.389485+00:00'
page_id: '561845643'
product: rm
source: tdn-rm
title: Conexão de Destino Utilizando API Rest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561845643
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo desse documento é esclarecer o uso de conexão destino usando a APIs Rest. Disponível a partir da versão 12.1.29.

Veja mais sobre as APIs do RM: .

# Conexão:

---

    Veja abaixo um exemplo de como criar uma conexão com API Rest.

   Passos para criar a conexão de destino com a API Rest:

false1Conexão

* Endereço base: Baseado nas APIs do RM, o endereço base é o host + porta;
* Verbos http: são disponibilizados os verbos PUT e POST.
* Endpoint envio: Baseado nas APIs do RM, o endpoint pode ser consultado nas documentações de API ou no swagger.  .
* Registro por transação: Atualmente as APIs do RM não aceitam envio de registros em array, por este motivo, ao usar APIs do RM, esse campo deve ser preenchido com 0 (zero). Assim serão enviados 1 registro por vez.
Autenticação

Na aba Autenticação, selecione se a autenticação na API será Basic, Oauth, ou sem autenticação;

Em seguida, preencha os campos necessários.

* Autenticação Basic:

* Autenticação Oauth:

Json Schema

Na aba Json schema, informe o json schema da API.

Para as APIs do host podem ser consultadas no swagger o Model Schema para criação do Json Schema, em algum conversor. Veja mais em: .

Ao utilizar APIs do RM, campos que não são mapeados no conceito na aba "Ligações" devem ser removidos do Json Schema.

Ligações

Por último, configure as ligações entre a tabela destino e origem.

Arraste primeiro a tabela de destino, depois a de Origem. Em seguida, clique no ícone 3, em destaque na imagem abaixo, para que as associações de campos sejam feitas automaticamente baseando-se no nome.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexões Destino: API Rest

falsefalse

**Status:** Finalizado

false

**Data:** 02/09/2020
