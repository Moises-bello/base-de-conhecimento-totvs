---
content_hash: 0901d0db2f2a58b2d2591a7a6d9a79676b69f15b275423b973bce1ef3b2e2252
fetched_at: '2026-06-29T00:05:47.108628+00:00'
page_id: '1005909240'
product: rm
source: tdn-rm
title: Objeto de negócio do histórico de situação dos artefatos sensíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005909240
version: 1
---

## 📘 Visão Geral

Um **Objeto de Negócio** representa uma **massa de dados contextualizada**, projetada para reunir e disponibilizar todas as informações necessárias à análise de um cenário específico dentro do ecossistema TOTVS RM.

O **Objeto de Negócio do histórico de situação dos Artefatos Sensíveis** tem como objetivo **listar o histórico de inclusão e/ou exclusão de um artefato sensível,** conforme definido na tabela **`GHSTARTEFATOSENSIVEL`**.

---

## 🗃️ Fonte de Dados

O objeto de negócio obtém suas informações diretamente da tabela:

| Tabela | Descrição |
| --- | --- |
| **GHSTARTEFATOSENSIVEL** | Armazena o histórico dos um artefatos sensíveis configurados no sistema. Cada registro representa uma associação entre o artefato, a data e o usuário informando se foi uma inclusão ou exclusão. |

---

## 📑 Campos Disponibilizados

| Campo | Descrição |
| --- | --- |
| **Cód. Coligada** | Código da coligada associada ao artefato sensível. |
| **Tipo do Artefato** | Tipo do artefato sensível, podendo ser: • **Consulta SQL** • **RM Reports** • **Planilha .NET** |
| **Descrição Tipo Artefato** | Descrição textual do tipo do artefato (ex.: *Consulta SQL*, *Relatório RM*, *Planilha .NET*). |
| **Aplicação** | Código do sistema ao qual o artefato pertence. |
| **Cód. Artefato** | Código identificador único do artefato sensível. |
| **Descrição Artefato** | Nome descritivo do artefato sensível. |
| **Tabela** | Nome da tabela no banco de dados associada ao campo sensível. |
| **Coluna** | Nome da coluna da tabela referente ao dado sensível contido pelo artefato. |
| **Data** | Data que a alteração foi realizada |
| **Usuário** | Código do usuário que realizou a alteração |
| **Tipo Registro** | Tipo da Alteração realizada   * I - Inclusão * E - Exclusão |
| **Descrição Tipo Registro** | Descrição do tipo de registro |
| **Situação** | 1 - Ativo  0 - Inativo |

Todos os campos refletem informações atualizadas diretamente da base RM, garantindo confiabilidade e rastreabilidade das configurações sensíveis.

---

## 🧭 Localização no Smart View

No **Smart View**, o Objeto de Negócio de Artefatos Sensíveis está localizado em:

cssConfluence

Caso o objeto não apareça na listagem, é provável que o usuário não possua permissão para acessá-lo.  
Veja a seção abaixo sobre **liberação de acesso ao perfil**.

---

## 🔐 Liberação de Acesso ao Objeto de Negócio

Para disponibilizar o Objeto de Negócio de Artefatos Sensíveis a um perfil de usuário, siga os passos abaixo:

1️⃣ **Acesse o módulo:** `Serviços Globais`

2️⃣ **Abra a aba:** `Segurança e Perfis`

3️⃣ **Filtre pelo perfil desejado** e clique em **Editar**

4️⃣ **Selecione a aba:** `Acesso a Menus`

5️⃣ **Libere a permissão:**

cssConfluence

Após a liberação, o objeto ficará visível na árvore de seleção do Smart View.
