---
content_hash: 5c71681e35f63315eb45a3e407e48f95747fba7e352f13e724b8be6c7be8e0e2
fetched_at: '2026-06-29T00:11:51.560661+00:00'
page_id: '849097434'
product: rm
source: tdn-rm
title: Regra Preenchimento do Código de Agrupamento para Pacotes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849097434
version: 3
---

## **01. Visão Geral**

Ao lançar **pacotes** na **parcial do paciente**, o sistema define automaticamente o **código de agrupamento** a ser informado no XML TISS, conforme o tipo de pacote selecionado, seguindo a **tabela de domínio 25 da ANS**.

## **02. Regras de Preenchimento**

* **Pacote de Diária** e **Pacote de Diária de Isolamento**  
  O sistema preenche o **código de agrupamento 05 – Diárias**.  
  Esse código é utilizado para identificar as despesas de diárias no XML TISS.
* **Pacote de Procedimentos**  
  O sistema preenche o **código de agrupamento 07 – Taxas e Aluguéis**.  
  Essa regra permanece aplicável aos pacotes técnicos ou de procedimentos, sem alteração no comportamento atual.

O código é gerado automaticamente durante a **montagem do XML TISS**, com base no tipo de pacote vinculado ao item lançado na parcial.

## **03.** **Exemplo de Geração no XML TISS**

**Pacote de Diária**

  05
  90101030
  Pacote de diária de internação
  1
  450.00
  450.00
]]>

**Pacote de Procedimento**

  07
  40808018
  Pacote de procedimento cirúrgico
  1
  1200.00
  1200.00
]]>
