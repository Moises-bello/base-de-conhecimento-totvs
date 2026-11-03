---
content_hash: 9e6d296f8ef7db0a43ee2403f8fee5099ce1ccfc4e29ad55a21bb02d7ac23fb0
fetched_at: '2026-06-29T00:08:14.250596+00:00'
page_id: '244444597'
product: rm
source: tdn-rm
title: DT_USUÁRIO_PADRÃO_WS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244444597
version: 115
---

# Usuário e senha padrão para WS (UX2)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Framework* |
| **Módulo:** | *Serviços Globais* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Paramâmetros Globais.* | *GlbParamsAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Chamada de WebService*.* | *WsDataServer.* | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *Usuário de integração Fluig / Senha de integração Fluig* |
| **Ponto de Entrada:** | *Parâmetros Globais* |
| **Chamados Relacionados** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | [FRW\_FRW002-24](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-24) |
| **País(es):** | *TODOS* |
| **Banco(s) de Dados:** | *TODOS* |
| **Tabelas Utilizadas:** | *GPARAMS* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Permite que chamadas feitas ao wsDataServer sejam feitas por um usuário de login(autenticação) diferente do usuário de contexto(utilizado no RMContext).

Com isso mantemos a segurança do RM e permitimos que exista um usuário "master" que poderá acessar o DataServer com outro usuário passado no contexto.

## Procedimento para Implantação

O sistema é atualizado na versão 12.1.4

## Procedimento para Configuração

*(Estes procedimentos devem ser feitos quando for necessário configurar parâmetros e/ou  rotinas no menu).*

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (Parâmetros Globais)**, acesse **Ambientes/Parâmetros/Parâmetros Globais (Integração Fluig)**. Configure *(mantenha somente a instrução correspondente)* o(s) parâmetro(s) a seguir:  
   *(É necessário criar uma tabela para cada parâmetro descrito no item **Parâmetro(s)**, da tabela **Características do Requisito**)*

divs
