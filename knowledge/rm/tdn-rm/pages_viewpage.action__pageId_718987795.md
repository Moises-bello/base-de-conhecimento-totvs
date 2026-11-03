---
content_hash: 3822482d4c11fd3d17b95b3f15ce30828ce73d87179b66264480fc067a552d5b
fetched_at: '2026-06-29T00:11:26.656550+00:00'
page_id: '718987795'
product: rm
source: tdn-rm
title: Integração Hermes Pardini > Cancelar exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=718987795
version: 4
---

## **Conteúdo**

1. **Visão Geral**
2. **Execução do Processo**

itensVisão Geral

## **01. VISÃO GERAL**

Cancelamento de exames integrados com laboratório Hermes Pardini.

Execução do Processo

## **02.****EXECUÇÃO DO PROCESSO**

Caminho: Unidade de Diagnóstico >> Resultados laboratoriais

Selecione os exames que deseja cancelar.

**Regras para cancelamento:**

* Status: **EE** - Entregue laboratório de apoio.
* Local de Execução: Não permitido exames sem local de execução e não permitido mais de um tipo de local selecionado.

Após selecionar os exames seguindo as regras acima acesse:

* Processos >> Cancelar exames integrados

Será exibido a tela do processo de cancelamento com os exames selecionados anteriormente para conferência.

Após clicar em "Executar" o processo será iniciado.

**Log do processo executado:**

* Caso o exame não seja cancelado no laboratório, será informado os pedidos, exames do laboratório e motivo do não cancelamento com a tela de **Alerta**

* Caso o processo encontre algum erro, será informado na tela o log de **Erro**e o exame não será cancelado nem no laboratório integrado nem no RM Saúde.

* Caso o processo execute sem alerta e sem erro será exibido a conclusão do processo

O exame será cancelado também dentro do RM Saúde.
