---
content_hash: e99ed79af35db80ee1b58233a272f128ad465f17aa9e54a33b270d33ca3129f3
fetched_at: '2026-06-29T00:08:12.044836+00:00'
page_id: '243633976'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Motivo_Exclusão_Cancelamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243633976
version: 113
---

# MOTIVO DE EXCLUSÃO DE ITEM DE COTAÇÃO E CANCELAMENTO DE COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cancelar Cotação.* | *CmpCancelarCotacaoAction.* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCCOTACAOITMMOV - Itens de Movimento Cotados.*  *TCCOTACAO - Cotações.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**nos processos de **Cancelamento de Cotação** e **Exclusão de Item de Movimento** foi disponibilizado o campo **Descrição** para que seja possível informar através de texto o motivo do Cancelamento da Cotação ou Exclusão de Itens de Movimento.

Disponibilizado na visão de Itens de Movimento, janela de edição da cotação, os campos **Código e Descrição de Motivo da Exclusão**.

## Procedimento para Utilização

****Exclusão de Item de**** **Movimento:**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione uma opção de filtro e clique em Executar.

3. Na visão de Cotação selecione um registro e clique em **Editar**.

O sistema apresenta a janela de edição da **Cotação:...**.

4. Na pasta **Itens de Movimento**selecione um ou vários itens e clique em **Excluir Item(ns).**

O sistema apresenta a janela **Exclusão de Item(s)**.

5. Informe os **Motivo** e a **Descrição** confirme clicando em **OK.**

**Cancelamento de Cotação:**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione um registro na visão e acesse **Processos / Cancelar Cotação**.

O sistema apresenta a janela de **Cancelar Cotação.**

3. Informe os **Motivo**e a**Descrição**confirme clicando em**Executar.**

divs
