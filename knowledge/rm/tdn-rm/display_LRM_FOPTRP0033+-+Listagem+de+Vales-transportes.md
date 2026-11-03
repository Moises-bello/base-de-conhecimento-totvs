---
content_hash: 7d10bcb3ed85ef2972330a11b541bad58330cbbed031c6c5a573c68b322c0414
fetched_at: '2026-06-29T00:05:52.796737+00:00'
page_id: '1060226925'
product: rm
source: tdn-rm
title: FOPTRP0033 - Listagem de Vales-transportes
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPTRP0033+-+Listagem+de+Vales-transportes
version: 3
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores

## **02. V****ISÃO GERAL**

O objeto de negócio Declaração de Opção do Vale Transporte tem como finalidade exibir a intenção de utilização de receber o Vale Transporte.  
  
Para mais informações pode ser acessado o link com informações do [Objeto de Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=1054771562)

#### **Regras de Filtro (Importante)**

Para garantir a performance e a segurança dos dados, o objeto possui uma lógica de filtros obrigatórios:

**Importante - Regras de Preenchimento:** O objeto exige que todos os parâmetros declarados recebam um valor para processar a requisição. Para alternar entre os tipos de filtro, utilize a lógica abaixo:

* **Filtrar por CPF:** Informe o número do CPF  do funcionário ou -1 para todos.
* **Filtrar por Matrícula:** Preencha com a chapa do funcionário ou -1 para todos.
* **Filtrar por Tarifa:** Preencha com o Cod. da Tarifa ou -1 para todos.

1. ## **03. EXEMPLO DE UTILIZAÇÃO**

   Visão de Dados

   Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados Declaração de Opção do Vale Transporte

   Relatório

   Gerando o relatório utilizando o SmartView:

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PFUNC
* PPESSOA
* PTARIFA
* PFVALETR
