---
content_hash: f4e49026da6f81dff195a4ec23bf99838bcc1f229f704c88d42d118f0dbbd80b
fetched_at: '2026-06-29T00:05:53.092254+00:00'
page_id: '1065247722'
product: rm
source: tdn-rm
title: Contratos – Desfazer Venda Backoffice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1065247722
version: 5
---

**Base Unificada PVI → PI**

## **Visão Geral**

Esta funcionalidade permite que contratos tenham sua venda desfeita diretamente pela visão de contratos no sistema, respeitando regras de permissão, configuração de status e validações do processo.

O objetivo é possibilitar o retorno do contrato para um estado anterior, garantindo controle operacional e consistência com o fluxo definido no sistema de Gestão de Imóveis.

---

## **Pré-requisitos**

Para que a funcionalidade esteja disponível ao usuário, é necessário que:

* A **situação atual do contrato** esteja configurada para permitir a ação de desfazer venda no backoffice.
* O **usuário possua permissão** específica para executar a ação.
* O contrato esteja visível na **visão de contratos**.

---

## **Acesso à Funcionalidade**

Na visão de contratos:

1. O usuário deverá acessar o menu de ações da linha do contrato.
2. Caso os critérios sejam atendidos, será exibida a opção:
   * **Desfazer venda no backoffice**

---

## **Regras de Negócio**

### **1. Disponibilidade da Ação**

A opção de desfazer venda será exibida somente quando:

* A situação do contrato permitir a operação, conforme parametrização do sistema.
* O usuário possuir permissão adequada.

---

### **2. Execução da Ação**

Ao selecionar a opção **Desfazer venda no backoffice**:

* O sistema executará o processo de desfazimento da venda.
* O contrato será automaticamente retornado para a **situação anterior**, conforme configuração definida no sistema.

---

### **3. Integração com Gestão de Imóveis**

Para contratos originados ou integrados ao módulo de Gestão de Imóveis:

* A proposta/venda **somente aceitará execução do processo** se estiver em uma situação diferente de:
  + **Em Preparação**
  + **Efetivada**

Importante!

Caso a proposta esteja em uma dessas situações, a ação não será executada pelo sistema.

---

## **Comportamento do Sistema**

* O sistema deve validar todas as regras antes de habilitar ou executar a ação.
* Caso alguma condição não seja atendida:
  + A opção não será exibida **ou**
  + A execução será bloqueada com mensagem de validação.
* O retorno do contrato respeita a parametrização de fluxo definida no ambiente.

---

## **Permissões**

A funcionalidade depende de controle de acesso, sendo necessário:

* Perfil com permissão para:
  + Visualizar contratos
  + Executar a ação de desfazer venda no backoffice

---

## **Observações**

* A funcionalidade não altera regras de negócio já existentes no fluxo de contratos.
* O comportamento de retorno de status depende exclusivamente da configuração do sistema.
* Recomenda-se validação prévia das permissões e parametrizações antes da utilização em ambiente produtivo.
