---
content_hash: 9220be84d3a087082c10eae5053faab06b896609c5de84c08a06cb13dc858b5c
fetched_at: '2026-06-29T00:08:37.504809+00:00'
page_id: '284879687'
product: rm
source: tdn-rm
title: 192746 MSAU-9921 DT Filtro de Unidades de Atendimento do Prestador
type: documentation
url: https://tdn.totvs.com/display/LRM/192746+MSAU-9921+DT+Filtro+de+Unidades+de+Atendimento+do+Prestador
version: 106
---

# Filtro de unidades de atendimento do Prestador

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento Externo | | Registro de Internações | | Parâmetros Gerais | | Elaboração de Contas | | Folha de Pagamento de Prestador | | Agenda Cirúrgica | | Cadastro de Agendas | |
| **Parâmetro(s):** | Filtra prestadores da unidade de atendimento |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZCADGERALUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows ® |

## Descrição

Implementado filtro de unidades de atendimento do prestador, para que ao realizar a pesquisa de prestadores no sistema, com o parâmetros marcado, devem aparecer somente os prestadores da unidade de atendimento relacionada.

## Procedimento para Configuração

* Valide se o perfil do usuário possui acesso às unidades de atendimento.

* Acesse o módulo TOTVS Gestão Hospitalar e marque o parâmetro "**Filtra prestadores da unidade de atendimento?**" que habilita a funcionalidade de Filtro de Unidades de Atendimento do Prestador.

* Abra o cadastro de um prestador e relacione as unidades de atendimento que ele atende.

**Procedimento para Utilização**

* No registro de internações, valide se os médicos que são listados possuem em seu cadastro a unidade de atendimento vinculada.

* No registro de atendimentos externos, valide se os médicos que são listados possuem em seu cadastro a unidade de atendimento vinculada.

* Na Agenda de Cirurgias, valide se os prestadores do procedimento são filtrados conforme a unidade de atendimento do registro.

* Por fim, validar se o sistema filtrará os prestadores no cadastro de Agendas.

divs
