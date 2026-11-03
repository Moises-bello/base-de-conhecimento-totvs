---
content_hash: a49b240a1871ef1ebcb6da0526ba4c3d3d9fcdafa91d8eedc64d1c84d9540b8d
fetched_at: '2026-06-29T00:10:44.528281+00:00'
page_id: '553322741'
product: rm
source: tdn-rm
title: Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553322741
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Demostrar o comportamento da aplicação quando o parâmetro **Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis**estiver habilitado.

# Introdução:

---

        Criado um novo parâmetro que influencia no comportamento dos filtros por perfil em consultas SQL.

        Na nova MDI, o parâmetro "**Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis**" altera o comportamento dos filtros por perfis na execução das consultas SQL cadastradas.

Fique atento

Os filtros por perfis são previamente cadastrados na visão de Perfis, na aba Segurança no módulo Serviços Globais.

      Por padrão, ao executar uma consulta SQL são aplicados os filtros cadastrados nos perfis do mesmo módulo em que a consulta SQL está cadastrada.

      Caso o parâmetro **Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis** esteja habilitado, ao executar uma consulta SQL serão aplicados todos os filtros por perfis cadastrados independentemente do módulo de origem do perfil e da SQL.

**Por exemplo:**Um usuário está associado a um perfil no módulo de Serviços Globais, este perfil possui filtro para a tabela PFUNC

      O mesmo usuário também está associado a outro perfil no módulo Folha de Pagamento e este perfil também possui filtro para a tabela PFUNC

      Existe uma consulta SQL cadastrada no módulo Folha de Pagamento que retorna os dados de todos os funcionários.

      Se a consulta SQL for executada pelo usuário e o parâmetro global **Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis**estiver desabilitado: será aplicado somente o filtro cadastrado no perfil do módulo Folha de pagamento (*chapa <> 00001*)

      Caso a consulta SQL seja executada pelo usuário e o parâmetro global **Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis**esteja habilitado: os filtros cadastrados em ambos os módulos serão aplicados. *chapa <> 00001* do Folha de pagamento e *chapa <> 00002* do Serviços Globais

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.25 ou superiores

false

**Processo:** Parâmetro global "Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis"

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
