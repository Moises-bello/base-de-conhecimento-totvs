---
content_hash: aec7ebbf2b6322ee1a5d4fc9520a8981972b015f39d060968db9efc714578ec3
fetched_at: '2026-06-29T00:05:47.883871+00:00'
page_id: '1019322846'
product: rm
source: tdn-rm
title: Guia de Permissões Essenciais para Criar Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1019322846
version: 2
---

*(Válido para usuários do* ***Atendimento Revitalizado****,* ***PDC*** *e* ***App****)*

Este documento descreve as permissões mínimas que devem ser liberadas no perfil do usuário para que ele consiga **criar, editar e visualizar atendimentos**, tanto no **Atendimento Revitalizado**, quanto no **PDC** e no **Aplicativo**.

Essas permissões garantem o correto funcionamento do atendimento, evitando erros de abertura, carregamento ou avanço entre etapas.

## **1. Atendimento Revitalizado**

Menu principal onde os atendimentos são criados e acompanhados.  
**Permissões necessárias**

* Visualizar
* Incluir
* Editar
* Etapa
* Excluir *(opcional, conforme política da empresa)*

Essas permissões permitem que o usuário abra, registre e finalize atendimentos.

## **2. Tipo de Atendimento**

O usuário não acessa este menu, mas o sistema precisa da permissão de leitura para carregar informações internas.  
**Permissão necessária**

* Visualizar

## **3. Checklist (quando utilizado pelo processo)**

Alguns atendimentos possuem checklists vinculados. Sem permissão, o usuário pode ter erro ao abrir ou salvar o atendimento.  
**Permissão necessária**

* Visualizar

## **4. Modelos**

Modelos podem ser carregados automaticamente pelo fluxo do atendimento.  
**Permissão necessária**

* Visualizar

## **5. Gerar Atendimento**

Conjunto de permissões essenciais para executar ações dentro do atendimento (inserir etapas, anexos, informações complementares etc.).  
**Permissões essenciais**

* Visualizar
* Editar
* Inserir
* Excluir *(opcional)*

### **Permissões complementares**

*(utilizadas internamente pelo sistema)*

* Checklist: Visualizar
* Movimentos: Visualizar

## **Por que algumas permissões são necessárias mesmo sem uso direto pelo usuário?**

Menus como **Movimentos** e **Checklist interno** são utilizados automaticamente pelo sistema para:

* carregar informações
* executar validações internas
* permitir avanço das etapas
* garantir funcionamento da máquina de cálculo

O usuário não acessa esses menus, mas o atendimento depende dessas permissões.

# **Resumo das Permissões Mínimas**

|  |  |  |
| --- | --- | --- |
| **Grupo** | **Ação** | **Necessário** |
| Atendimento Revitalizado | Visualizar / Incluir / Editar / Etapa | Obrigatório |
| Tipo de Atendimento | Visualizar | Obrigatório |
| Checklist | Visualizar | Recomendado |
| Modelos | Visualizar | Necessário |
| Gerar Atendimento | Visualizar / Editar / Inserir | Obrigatório |
| Menus internos (Movimentos, Checklist interno) | Visualizar | Necessário para funcionamento técnico |
