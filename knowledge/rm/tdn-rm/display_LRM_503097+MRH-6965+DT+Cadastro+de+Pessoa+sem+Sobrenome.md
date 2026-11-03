---
content_hash: 536b91acd2c7a3f7813b8635f63bf40f6fd99d04c95a2db66574ff270b8badaf
fetched_at: '2026-06-29T00:08:29.521633+00:00'
page_id: '272150651'
product: rm
source: tdn-rm
title: 503097 MRH-6965 DT Cadastro de Pessoa sem Sobrenome
type: documentation
url: https://tdn.totvs.com/display/LRM/503097+MRH-6965+DT+Cadastro+de+Pessoa+sem+Sobrenome
version: 108
---

# CADASTRO DE PESSOA SEM SOBRENOME

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Rotina:** | |  | | --- | | **Rotina** | | Cadastro e/ou atualização do nome da pessoa. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Cadastro e/ou atualização do nome da pessoa. | |
| **Cadastros Iniciais:** | Para a utilização do requisito será necessário parametrizar o sobrenome como não obrigatório. |
| **Parâmetro(s):** | Configurações > Gerais > Validações   * Sobrenome não obrigatório |
| **Tickets relacionados** | 503097 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MRH-7629 |
| **País(es):** | Todos. |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | PPESSOA |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação visa possibilitar o cadastro do nome da pessoa sem sobrenome.

## Importante

* Para que funcione corretamente, os parâmetros precisam estar configurados corretamente.

## Procedimento para Configuração

Para configurar basta seguir os passos de configuração de parâmetros abaixo:

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **parametrizador**do RM acesse:
   1. * Configurações > Gerais > Validações

Marque a opção 'Sobrenome não obrigatório' e conclua o processo.

## Procedimento para Utilização

* Acesse o aplicativo RM.exe
* Abra um dos registros de relacionados a Pessoa. Ex: Funcionário, Pessoa, Candidato
* Altere o nome da pessoa, para um nome sem sobrenome.

divs
