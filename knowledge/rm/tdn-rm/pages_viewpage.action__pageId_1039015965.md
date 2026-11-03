---
content_hash: af85b4621fb2c5f4996ef3b167be1ca3b716c8b7c2eaf69b93fb5bd058243d05
fetched_at: '2026-06-29T00:05:49.152791+00:00'
page_id: '1039015965'
product: rm
source: tdn-rm
title: Configurações para inserir Itens Confirmados da Solicitação MatMed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039015965
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

No Prontuário Eletrônico (PEP), ao liberar uma solicitação de MatMed de um medicamento marcado como "Se Necessário", o sistema poderá ser configurado para que este medicamento apareça no Painel de Dispensação já com o status Confirmado.

## **02. EXEMPLO DE UTILIZAÇÃO**

Pré-Requisitos para gerar um item Confirmado automaticamente no Painel de Dispensação:

**1 – Parâmetros Gerais de Estoque – marcar “Confirma itens que não baixa estoque na requisição”.**

**2 – Cadastro de Produto:**

2.1 - Não poderá ser controlado por lote. O campo “Controlado por lote” (TPRODUTO.CONTROLADOPORLOTE) deverá estar desmarcado.

2.2 - No anexo “Informações Totvs Saúde” deverá estar configurado:

- Baixa Estoque = Não

- Marcar os campos “Permitido prescrições dos itens na Modalidade”:

Se Necessário

A critério médico

- Desmarcar o campo “Permite processamento parcial de requisição”

**3 - No Prontuário Eletrônico (PEP):**

3.1 - Criar uma Prescrição médica onde um dos medicamentos prescritos esteja marcado o campo “Se Necessário”.

Liberar a prescrição.

3.2 - Na “Solicitação de MatMed”, a Enfermagem irá solicitar o medicamento e este cairá automaticamente no Painel de Dispensação com o status igual a Confirmado

**4 – No Gestão Hospitalar, Painel de Dispensação**

**5 - Definições Técnicas:**

- Itens confirmados devem ser inseridos na tabela de movimentação de aprazamento (tabela SZMOVITMAPRAZ), necessário para serem listados no Painel de Dispensação.

- O status do item deverá estar Confirmado (SZMOVIESTOQUEITEM.CONFIRMADO igual a T)

- O status do aprazamento deverá estar Confirmado (SZAPRAZAMENTO.STATUS igual a F)
