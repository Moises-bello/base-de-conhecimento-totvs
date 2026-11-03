---
content_hash: 917795325d2ae5fa6b0a4a53330280038af0cb3ae215458694c14b99174f77df
fetched_at: '2026-06-29T00:05:47.114854+00:00'
page_id: '1005909334'
product: rm
source: tdn-rm
title: Objeto de negócio de acesso aos artefatos sensíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005909334
version: 3
---

## 📘 Visão Geral

Um **Objeto de Negócio** representa uma **massa de dados contextualizada**, projetada para reunir e disponibilizar todas as informações necessárias à análise de um cenário específico dentro do ecossistema TOTVS RM.

O **Objeto de Negócio de acesso aos Artefatos Sensíveis** tem como objetivo **listar todos os usuários que acessaram os artefatos sensíveis** cadastrados na base de dados, conforme definido na tabela **`GHSTACESSOSENSIVEL`**.  
Ele fornece uma visão consolidada e centralizada dos acessos, permitindo auditorias e análises de conformidade.

---

## 🗃️ Fonte de Dados

O objeto de negócio obtém suas informações diretamente da tabela:

| Tabela | Descrição |
| --- | --- |
| **GHSTACESSOSENSIVEL** | Armazena os usuários que acessaram os artefatos sensíveis configurados no sistema. |

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
| **Data Acesso** | Data que o usuário acessou o artefato. |
| **Usuário Acesso** | Usuário que acessou o artefato. |

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
