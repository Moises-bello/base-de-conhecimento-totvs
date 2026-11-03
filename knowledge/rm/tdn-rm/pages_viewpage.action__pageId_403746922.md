---
content_hash: baa51b3c646b33917d44b6a67dff7b35f944a0a09383fe1841d2e69bd0156798
fetched_at: '2026-06-29T00:09:11.328812+00:00'
page_id: '403746922'
product: rm
source: tdn-rm
title: Fórmulas Globais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746922
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

As fórmulas globais são aquelas apresentadas para todos os módulos do sistema, e são passíveis de uso em qualquer um deles.

Conheça as fórmulas globais:

## **02. EXEMPLO DE UTILIZAÇÃO**

**EXECSQL**

Executa uma consulta SQL. Caso a execução tenha pelo menos uma linha de resultado, está variável retorna VERDADE.

Sua sintaxe é: EXECSQL('código da consulta SQL').

 

**Exemplo:**

EXECSQL('Codigo\_Consulta\_SQL')

 

**PROXREGSQL**

Avança um registro na Consulta SQL executada.

Sua sintaxe é: PROXREGSQL('código da consulta sql')

 

**Exemplo:**

PROXREGSQL('Codigo\_Consulta\_SQL')

  

**RESULTSQL**

Esta função lê uma linha do resultado da execução da SQL.

Sua sintaxe é: RESULTSQL('código da consulta sql', 'nome do campo')

 

**Exemplo:**

RESULTSQL('Codigo\_Consulta\_SQL', 'SALARIO')

false

**Versão:** 12.01.XX
