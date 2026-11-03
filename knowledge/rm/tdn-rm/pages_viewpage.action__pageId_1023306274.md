---
content_hash: c1cc7358a3e2d3b2f4d9518261c1ee6a6616f0470d4613344ed5c86c3d25fe2d
fetched_at: '2026-06-29T00:05:48.149882+00:00'
page_id: '1023306274'
product: rm
source: tdn-rm
title: Reforma Tributária - Parâmetros dos Movimentos de Venda de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023306274
version: 5
---

## **Parâmetros dos Movimentos de Venda de Imóveis**

## Visão Geral

Os **Parâmetros de Movimento do IVA** têm como objetivo definir **como e quando o IVA será aplicado** aos movimentos financeiros e fiscais do sistema, garantindo aderência às regras da Reforma Tributária e consistência nos cálculos tributários.

Essa parametrização é essencial para assegurar que apenas os movimentos corretos participem do cálculo do IVA, respeitando as regras tributárias e os redutores sociais aplicáveis ao setor imobiliário.

---

## Objetivo da Parametrização

A funcionalidade de **Parâmetros Movimento IVA** permite:

* Controlar **quais tipos de movimento** estão sujeitos ao IVA
* Associar cada movimento a uma **regra tributária específica**
* Aplicar corretamente os **redutores sociais** definidos para Incorporação, Loteamento ou Locação
* Garantir **padronização, rastreabilidade e conformidade fiscal**

---

## Estrutura dos Parâmetros

A parametrização é realizada por meio de uma **tela específica**, onde são definidos os seguintes dados:

### 1. Parâmetro do Movimento

* Define o **tipo de movimento** que será considerado no cálculo do IVA.
* O sistema trabalha com um valor **default**, garantindo padronização na configuração.

> **Importante:**  
> Somente será permitido informar **movimentos do tipo 2.1.x**.  
> Essa validação é obrigatória e realizada automaticamente pelo sistema.

---

### 2. Regra Tributária

* Campo vinculado à **DREGRATRIBUTARIA**.
* Determina as regras fiscais que serão aplicadas ao movimento no cálculo do IVA.
* Permite flexibilidade para atender diferentes cenários tributários conforme legislação.

---

### 3. Redutor Social

* Campo vinculado à **tabela de redutores sociais**.
* Define qual redutor será aplicado à base de cálculo do IVA, conforme o tipo de operação:

  + Social – Incorporação Imobiliária
  + Social – Loteamento
  + Social – Locação

Essa associação garante que os benefícios fiscais sejam corretamente aplicados durante o cálculo do imposto.

---

## Validações do Sistema

Para assegurar a integridade da parametrização, o sistema realiza as seguintes validações:

* Permite **exclusivamente** movimentos do tipo **2.1.x**
* Impede o salvamento de parâmetros inconsistentes
* Garante que a regra tributária e o redutor social estejam corretamente vinculados

Essas validações evitam erros de cálculo e inconsistências fiscais.

---

## Controle e Auditoria

Todas as ações realizadas na parametrização dos **Parâmetros Movimento IVA** são **registradas em log**, incluindo:

* Inclusões
* Alterações
* Exclusões

Esse controle garante:

* Rastreabilidade das informações
* Atendimento a auditorias fiscais
* Segurança e governança dos dados

---

## Impacto no Processo

Uma vez configurados, os **Parâmetros Movimento IVA** passam a ser utilizados automaticamente pelo sistema nos processos de cálculo do imposto, assegurando que:

* O IVA seja aplicado apenas quando devido
* As regras tributárias estejam corretas
* Os redutores sociais sejam respeitados

---

## Disponibilidade

A funcionalidade de **Parâmetros Movimento IVA** está disponível **a partir da versão 12.1.2502** do TOTVS Construção Gestão de Imóveis.
