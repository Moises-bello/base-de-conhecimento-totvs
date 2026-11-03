---
content_hash: 06297acd59ab5a5e2fcb60be2d5b5853750faaa5485c78f7a915d6e25bd2f9da
fetched_at: '2026-06-29T00:12:01.193166+00:00'
page_id: '889106438'
product: rm
source: tdn-rm
title: Objeto de Negócio de Permissões e Recursos do Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889106438
version: 14
---

# Objetivo

Este recurso permite manter todas as funcionalidades do sistema padrão, customizadas ou de metadados agrupados para uma leitura mais dinâmica das informações pelo Objeto de Negócio.  
A tabela base de funcionalidades alimenta o Objeto de Negócio para que possa ser utilizado pelos recursos do Smart View.

Disponível a partir da versão 12.1.2410

# Como atualizar a tabela de funcionalidades

**Atualização automática:**

Através do Notify Server, de forma automática esta tabela é atualizada a cada subida do RM.Host.exe, que executa o processo apenas uma vez, mantendo o agrupamento de funcionalidades atualizado.

Importante saber que caso existam dados na tabela, o processo será ignorado, não realizando a sobrescrita das informações.

**Processo manual:**

Caso haja necessidade de realizar uma atualização imediata é possível solicitar a execução de um processo.  
Dentro do módulo Serviços Globais -> aba Segurança -> Perfis, no item de menu -> Processos, selecione a opção -> Atualizar tabela de funcionalidades

# Objeto de Negócio

O objeto de negócio, Acessos e Permissões é a entidade básica que representa todas as funcionalidades que se pode extrair do RM para um recurso do Smart View.

# Recursos do Smart View

Através do TOTVS Compartilhamento é possível ter acesso e importar estes recursos do Smart View.

### Visão de Dados

* Acessos e Permissões - Funcionalidade  
  Apresenta uma listagem com todos os Acessos e Permissões do sistema filtrados pela Tag de Segurança.
* Acessos e Permissões - Coligada  
  Apresenta uma listagem com todos os Acessos e Permissões do sistema filtrados pelo código da Coligada.
* Acessos e Permissões - Usuário  
  Apresenta uma listagem com todos os Acessos e Permissões do sistema filtrados pelo código do usuário.

Exemplo na importação dos recursos:

Exemplo após a importação:

Exemplo das permissões do usuário "astoni"
