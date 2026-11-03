---
content_hash: c0369f4ca524935c029c6486f34beb380e70783c380d5b7d660ea7fb0be416d6
fetched_at: '2026-06-29T00:11:53.701530+00:00'
page_id: '850700902'
product: rm
source: tdn-rm
title: Exceção à Restrição de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=850700902
version: 1
---

## 

## **01. EXEMPLO DE UTILIZAÇÃO**

A validação da “**Exceção à Restrição de Contrato**” acontece em 3 momentos:

 

- Na tela de **Registro de Atendimento**, ao clicar em “**Salvar**”

- Ao selecionar o **Leito** na tela de **Registro de Atendimento** (no click do botão)

- No Encerramento da Parcial verifica se tem exceção de contrato para M

atMed

 

Exceção à Restrição de Contrato

**Código que faz o tratamento da Exceção**

- Se tem Exceção cadastrada pega o valor do procedimento e ***não verifica*** se tem Restrição

- Se **não tem** Exceção cadastrada, pega o valor do procedimento e ***verifica*** se tem Restrição

A validação da “**Exceção à Restrição de Contrato**” acontece em 3 momentos:

 

- Na tela de **Registro de Atendimento**, ao clicar em “**Salvar**”

- Ao selecionar o **Leito** na tela de **Registro de Atendimento** (no click do botão)

- No Encerramento da Parcial verifica se tem exceção de contrato para MatMed

 

**Uso da tabela: szCondContratExcecao** 

Locais aonde foi encontrada referência à tabela: 

- Na cópia da “**Condição Contratual**” (copia a tabela)

- Classes que fazem referência à tabela:

- insuranceContract (SauContractModule)

- SauAutoInc

## **05. TABELAS UTILIZADAS**

**szCondContratExcecao**
