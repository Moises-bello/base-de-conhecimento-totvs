---
content_hash: dd7e3cd656565b707c9f6f6f43d8fcf824066883cb768a28e30f07ca04f74163
fetched_at: '2026-06-29T00:08:07.913732+00:00'
page_id: '237397400'
product: rm
source: tdn-rm
title: Concatena Filtro Por Perfil com AND em Consulta SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/Concatena+Filtro+Por+Perfil+com+AND+em+Consulta+SQL
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Mostrar como e porque utilizar as configurações para concatenar com o operador lógico AND os filtros por perfil.

# Introdução:

---

        Foi criado um novo parâmetro para mudar o comportamento dos filtros por perfil em consultas SQL.

        Na nova MDI, o parâmetro "**Concatena filtro por perfil com AND em Cons. SQL**" trata o comportamento dos filtros por perfil na execução das consultas SQL cadastradas.

      Por padrão, os filtros por perfil são concatenados nas consultas SQL do RM utilizando o operador lógico AND, entretanto, caso o usuário possua mais de um perfil associado e cada um desses perfis possuir uma condição para o mesmo campo da mesma tabela, os filtros se anulam conforme a consulta SQL de exemplo abaixo que realiza um select na tabela GFILIAL e possui filtros para as filiais 1, 2 e 9:

sql

        Por padrão o parâmetro fica habilitado, mantendo o comportamento atual. Para que os filtros possam ser concatenados com o operador lógico OR deve-se desabilitar o parâmetro. Com o parâmetro desabilitado, a consulta será montada da seguinte forma:

sql

        Com a alteração dos parâmetros, as consultas retornarão dados de todos os filtros cadastrados.

Fique atento:A execução de uma Consulta SQL considera os parâmetros de segurança por linha e por coluna configurados em cada consulta. Clique e saiba como essas configurações influenciam no resultado do seu select.falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Parâmetro global "Concatena filtro por perfil com AND em Cons. SQL"

falsefalse

**Status:** Finalizado

false

**Data:** 29/08/2016

false

**Autores:**
