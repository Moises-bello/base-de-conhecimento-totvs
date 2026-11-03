---
content_hash: ce6132117edec9da6f084afeac5e17a20b3deeea05f33c557fa7a9ca8d14d430
fetched_at: '2026-06-29T00:08:57.190766+00:00'
page_id: '353278695'
product: rm
source: tdn-rm
title: Segurança dos Serviços (WebAPI) - Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353278695
version: 9
---

# Objetivo

---

Este documento tem como objetivo auxiliar na definição de segurança de acesso aos serviços da WebAPI de acordo com as permissões concedidas na linha RM.

# Atributo

---

Foi definido o seguinte atributo para decoração dos *controllers* e *actions*: **RMApiAuthorize**

| Propriedade | Descrição |
| --- | --- |
| SecurityId | Id de Segurança do *Controller*. Deverá ser gerado pelo RM Especifica, da mesma forma que é gerado para Actions do RM. |
| ExecuteId | Id de Permissão para operações (*actions*). Mesmo que é utilizado para Processos e Anexos na Linha RM. |
| Module | Identificador do Módulo da Linha RM. Ex.: Serviços Globais - G |

Por padrão, o *SecurityId* e *ExecuteId* tem o valor zero.

*Controllers* com o *SecurityId* com o valor zero não tem sua autorização validada, da mesma forma que nas *Actions* e *DataServers* da linha RM.

# Exemplos

---

No *controller* e/ou *actions* (métodos) deverá ser informado o atributo com as devidas configurações:

c#1ExemploControllertrue

Note o uso do atributos nas Linhas 1 e 9. Os métodos que não tiverem atributos definidos, herdarão a permissão definida no *Controller*.

# Definição na Árvore de Permissões

---

Deverá ser definido no **Menu Profile do Módulo**, por exemplo **GlbProfileController**, de acordo com a hierarquia habitual (*pages, groups, items, policies*) a estrutura para definir a permissão e exibição na árvore de perfil.

As *Pages* e *Groups* devem ser definidos somente por questão de organização da árvore. No exemplo abaixo, foi criada uma página "Controllers (WebAPI)" e um grupo "Exemplo".

Importante

Lembrando que itens com *Tag* vazia ou igual a zero, NÃO são mostrados na árvore de permissão. O Ids de Segurança devem ser gerados pelo RM Especifica, do mesmo modo que é feito para Actions do RM.

As permissões são validadas independente de Coligada do RM, visto que temos APIs independentes de contexto.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.21

false

**Processo:** Segurança de serviços REST (Web API)

falseÍndice

.\*ndice:none

falsefalse

**Status:** Em desenvolvimento

false

**Data:**

false

**Autores:**
