---
content_hash: 1712f7b00a3ffd2bc2aec59f09f1e23b187f0ef3c1654f11b567393d8506c3e3
fetched_at: '2026-06-29T00:10:52.353484+00:00'
page_id: '572024279'
product: rm
source: tdn-rm
title: Validação dos dados ANS do Registro de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572024279
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esse documento define parâmetros e regras dos dados ANS do Registro de Atendimento de Guias Tiss.

## **02. EXEMPLO DE UTILIZAÇÃO**

* Validação número de registro ANS do convênio:

     Caso o campo Registro ANS esteja vazio e o Padrão for TISS, deve retornar erro no encerramento da conta.

* Validação de médico requisitante:

      Verifica se o código de médico requisitante não está informado, retornando erro.

# 

* Verifica existência de registros na tabela SZANSATEND, retornando erro se não houver registro.

## **03. TABELAS UTILIZADAS**

* SZANSATEND
* SZATENDIMENTO
