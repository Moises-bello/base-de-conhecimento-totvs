---
content_hash: ff8578d2e8ea0e2399c63c4b77d19c24732ac18c8ec50f025032a93138e1ad79
fetched_at: '2026-06-29T00:11:50.682805+00:00'
page_id: '844979134'
product: rm
source: tdn-rm
title: Migração dos dados do PEP1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844979134
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Estrutura do Processo**
3. **Telas utilizadas**

Migração dos dados do PEP1 Visão Geral

## **01. VISÃO GERAL**

**Este documento tem como objetivo detalhar a funcionalidade de migração de registros do produto descontinuado PEP1 para o prontuário eletrônico atual (PEP). A funcionalidade permite que os usuários visualizem os registros de atendimentos, incluindo aqueles realizados no PEP1, após a ativação de um parâmetro específico.**

Estrutura do Processo

## **02. ESTRUTURA DO PROCESSO**

* **Parâmetro de Ativação:** Um novo parâmetro foi adicionado à seção "Prontuário Eletrônico" dos parâmetros gerais do sistema. Ao ativar o parâmetro "Exibir histórico do PEP1", os registros de atendimentos provenientes do PEP1 serão exibidos na funcionalidade "Histórico de Atendimento".

* **Identificação de Registros:** Os registros migrados do PEP1 serão devidamente identificados na funcionalidade "Histórico de Atendimento", permitindo ao usuário distinguir entre os atendimentos realizados no PEP atual e aqueles provenientes do PEP1.

* Não é necessário realizar nenhuma configuração além do parâmetro de ativação.
Telas utilizadas

## **03. TELAS UTILIZADAS**

**Parâmetros Gerais:**

* No RM: "Ambiente" → Parâmetros → Gestão Hospitalar → Prontuário Eletrônico → "Exibir histórico PEP1".  Selecionar o parâmetro para exibição do histórico.

**Histórico de Atendimento:**

* Após a ativação do parâmetro, a funcionalidade "Histórico de Atendimento" dentro do PEP exibiráos registros relacionados as rotinas Prescrição médica, evolução, receitas, anamnese e parecer do especialidade, incluindo aqueles provenientes do PEP1. Os registros migrados deverão estar identificados no histórico de atendimento e não serão exibidos com a abertura de uma nova página. A exibição vai ocorrer apenas com a abertura do accordeo.
