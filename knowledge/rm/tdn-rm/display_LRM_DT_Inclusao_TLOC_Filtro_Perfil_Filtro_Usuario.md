---
content_hash: 6008248d3f3cd77fcd16f3e26f73caa3535e83740b3952181935421873b16cfb
fetched_at: '2026-06-29T00:06:00.886784+00:00'
page_id: '196813524'
product: rm
source: tdn-rm
title: DT_Inclusao_TLOC_Filtro_Perfil_Filtro_Usuario
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Inclusao_TLOC_Filtro_Perfil_Filtro_Usuario
version: 2
---

# INCLUSÃO TABELA TLOC NO FILTRO POR PERFIL E USUÁRIO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Locais de Estoque.* | *Cadastro de Local de Estoque.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Filtro por Usuário*.* | *Anexo Filtro por Usuário do cadastros de Usuários.* | | **Filtro por Perfil*.* | *Anexo Filtro por Perfil do cadastros de Perfis.* | |
| **Requisito (ISSUE):** | *PCREQ-6375.* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas utilizadas:** | *TLOC - Local de Estoque*  *GFILTROUSUARIO - Filtro por Usuário*  *GFILTROPERFIL - Filtros associados aos Perfis* |
| **Sistema(s) operacional(is):** | *Windows 7 SP1.* |
| **Versões/Release:** | *12.1.7.* |

## Descrição

Permitir que o usuário defina Filtro por Perfil e Filtro por Usuário para a tabela de Local de Estoque.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Para definir o **Filtro por Usuário** acesse o módulo **Serviços Globais\Segurança\Usuários** selecione um registro. Acesse o **Anexos\****Filtro por Usuário** e inclua o filtro para a Tabela TLOC.
2. Para definir o **Filtro por Perfil** no módulo **Serviços Globais\Segurança\Perfis** selecione um registro. Acesse o **Anexos\Filtro por Perfil** e inclua o filtro para a Tabela TLOC.

## Procedimento para Utilização

**Cadastros de Locais de Estoque:**

       1. Acesse o módulo **BackOffice\Gestão de Estoque, Compras e Faturamento\Cadastros\Locais de Estoque.**

O sistema apresenta a visão de locais de estoques com os registros cadastrados, aplicando o Filtro por Usuário e Filtro por Perfil definidos para o usuário logado.

       2. Caso o usuário logado realize a inclusão de um novo registro que não respeite o filtro definido para usuário ou perfil, o sistema irá emitir uma mensagem de consistência ao usuário conforme abaixo:

Essas informações não podem ser salvas!

Suas permissões (filtro por usuário) restringem o acesso a esses dados. Para salvar o registro, ele deve obedecer aos seguintes critérios.

**Observação:**todos os pontos do sistema que possuir um campo que exibe a informação de Local de Estoque, irá respeitar os filtros definidos por usuário e/ou perfil.
