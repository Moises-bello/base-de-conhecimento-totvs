---
content_hash: a68ba6d46942ac65181c424dd5d50a4ed4710f9ca1e904c3b9ea14cb673c79e1
fetched_at: '2026-06-29T00:05:47.102523+00:00'
page_id: '1005902246'
product: rm
source: tdn-rm
title: Relacionamento Fabricante
type: documentation
url: https://tdn.totvs.com/display/LRM/Relacionamento+Fabricante
version: 1
---

## **01. VISÃO GERAL**

Esta funcionalidade permite cadastrar o relacionamento entre os **fabricantes internos do sistema** e os **fabricantes externos** provenientes dos cadastros do **Simpro** e do **Brasíndice**.

O objetivo desse relacionamento é estabelecer a correspondência (amarração) dos códigos de fabricantes, garantindo que, ao selecionar um item oriundo do Brasíndice ou do Simpro, o sistema consiga identificar corretamente o fabricante equivalente cadastrado no RM.

Dessa forma, o processo de integração e identificação de itens entre o RM e as tabelas externas torna-se mais confiável e automatizado.

## **02. CADASTRO RELACIONAMENTO FABRICANTE**

**Cadastros > Faturamento > Outros Cadastros > Relacionamento Fabricante**

 

**Campos**

Tipo: Simpro / Brasíndice

Código Fabricante Sistema: Código do RM que deseja vincular ao Fabricante externo

Código Fabricante Externo: Código do fabricante externo que será vinculado ao fabricante do RM

## **03. VALIDAÇÕES**

O sistema deve barrar cadastro de relacionamento para o mesmo Fabricante Sistema com o mesmo Tipo
