---
content_hash: 1aee652021e5e0a802a8ce2548056e92b3510edc74203dec2a9f4125e8dc1d58
fetched_at: '2026-06-29T00:05:53.115518+00:00'
page_id: '1066699008'
product: rm
source: tdn-rm
title: OIDC - Tela de Login
type: documentation
url: https://tdn.totvs.com/display/LRM/OIDC+-+Tela+de+Login
version: 4
---

# **01.** **Visão Geral**

Esta documentação detalha as alterações na interface de login do sistema RM para suporte ao protocolo **OpenID Connect (OIDC)**. A experiência do usuário (tela antiga vs. tela nova) é determinada de forma dinâmica pela combinação das configurações de parâmetros globais do ambiente e configurações individuais do usuário.

# **02.** **Configurações de Ambiente (Parâmetros Globais)**

Foi adicionada uma nova aba nos **Parâmetros Globais** do sistema (Módulo Global / Serviços Globais) para gerenciar o comportamento da integração.

### 2.1. Campo: Integração OIDC

Este campo define a postura de segurança e integração do ambiente como um todo, devido a isso, somente usuários **SUPERVISORES** do módulo de Serviços Globaispoderão alterar esse campo

| **Valor Texto** | **Descrição** |
| --- | --- |
| **Não Integrado** | O sistema utiliza exclusivamente a autenticação nativa/legada. |
| **Obrigatório** | Todos os usuários devem realizar o login via provedor de identidade (Identity/OIDC). |
| **Opcional** | Permite um cenário híbrido entre autenticação nativa e OIDC. |



---

# **03.** **Configurações por Usuário**

Independente da configuração global, o cadastro do usuário possui uma flag que indica se aquele usuário específico já está vinculado ou preparado para a autenticação moderna. Assim como o campo anterior, somente usuários **SUPERVISORES** do módulo de Serviços Globaispoderão alterar esse campo

---

# **04.** **Lógica de Exibição da Tela de Login**

A interface apresentada ao usuário final varia entre o formato **Antiga** (campos de Usuário e Senha visíveis) e **Nova** (campo único de Usuário, com redirecionamento posterior).

A tabela abaixo descreve a matriz de decisão do sistema:

| **Integração OIDC (Parâmetros Globais)** | **Login OIDC (Usuário)** | **Comportamento da Tela** | **Descrição** |
| --- | --- | --- | --- |
| **Não Integrado (0)** | Nenhum | **Antiga** | Fluxo padrão de usuário e senha. |
| **Não Integrado (0)** | Algum | **Antiga** | Mesmo com o usuário configurado, a flag global desativada força o modo legado. |
| **Opcional (2)** | N | **Antiga** | Ambiente permite OIDC, mas o usuário ainda não foi migrado. |
| **Opcional (2)** | Algum | **Nova** | Ambiente permite e o usuário está apto; ativa-se a interface moderna. |
| **Obrigatório (1)** | Não | **Nova** | O ambiente força o OIDC; a tela nova é exibida para processar a autenticação. |
| **Obrigatório (1)** | Sim | **Nova** | Fluxo completo de autenticação moderna. |

---

# **05.** **Detalhamento das Interfaces**

### 5.1. Tela Antiga (Legada)

* **Campos:** Nome de Usuário e Senha visíveis simultaneamente.
* **Autenticação:** Realizada diretamente com a base de dados RM ou LDAP integrado.

### 5.2. Tela Nova (Moderna)

* **Campo:** Apenas o campo "Usuário".
* **Fluxo:** Ao informar o usuário, o sistema valida as condições da tabela acima. Se confirmado o uso de OIDC, o campo de senha é suprimido e o usuário é redirecionado para a página de autenticação do provedor de identidade (Ex: TOTVS Identity) via WebView2.

false

**Índice:**

false

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Integração OIDC

falsefalse

**Status:** Em Desenvolvimento

false

**Data:** 22/04/2026
