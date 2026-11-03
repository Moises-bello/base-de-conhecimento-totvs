---
content_hash: bd776f286e5d998a3f8582c5ba4f701b59df9fc24cc3a467116f155dad726525
fetched_at: '2026-06-29T00:06:01.844862+00:00'
page_id: '198940973'
product: rm
source: tdn-rm
title: Filtro_por_Usuário_e_Perfil_para_a_Tabela_TLOC_BRA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198940973
version: 3
---

# Filtro por Usuário e por Perfil para a Tabela TLOC

Permitir que o usuário defina Filtro por Perfil e Filtro por Usuário para a tabela de Local de Estoque. Ao definir um **Filtro por Usuário** ou **Filtro por Perfil**, quando o usuário acessar o cadastro de Local de Estoque e demais pontos do sistema que possuírem a informação de Local de Estoque, será respeitado os filtros definidos por usuário e/ou perfil.

**Configuração de Parâmetros:**

1. Para definir o **Filtro por Usuário**acesse o módulo **Serviços Globais\Segurança\Usuários** selecione um registro. Acesse o **Anexos\****Filtro por Usuário** e inclua o filtro para a Tabela TLOC.
2. Para definir o **Filtro por Perfil** no módulo **Serviços Globais\Segurança\Perfis** selecione um registro. Acesse o **Anexos\Filtro por Perfil** e inclua o filtro para a Tabela TLOC.

## Procedimento para Utilização

**Cadastros de Locais de Estoque:**

       1. Acesse o módulo **BackOffice\Gestão de Estoque, Compras e Faturamento\Cadastros\Locais de Estoque.**

O sistema apresenta a visão de locais de estoques com os registros cadastrados, aplicando o Filtro por Usuário e Filtro por Perfil definidos para o usuário logado.

       2. Caso o usuário logado realize a inclusão de um novo registro que não respeite o filtro definido para usuário ou perfil, o sistema irá emitir uma mensagem de consistência ao usuário conforme abaixo:

Essas informações não podem ser salvas! Suas permissões (filtro por usuário) restringem o acesso a esses dados. Para salvar o registro, ele deve obedecer aos seguintes critérios.

**Observação:**todos os pontos do sistema que possuir um campo que exibe a informação de Local de Estoque, irá respeitar os filtros definidos por usuário e/ou perfil.

**Tabelas Utilizadas**

* TLOC - Local de Estoque
* GFILTROUSUARIO - Filtro por Usuário
* GFILTROPERFIL - Filtros associados aos Perfis

**Conteúdos Relacionados:**

*Links dos principais conceitos e processos.*
