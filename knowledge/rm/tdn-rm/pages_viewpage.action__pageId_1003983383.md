---
content_hash: e8bcaa5c1858d2cbce3c39a3809796c4f8e482e30c7529229fa48626d0a4d932
fetched_at: '2026-06-29T00:05:46.978961+00:00'
page_id: '1003983383'
product: rm
source: tdn-rm
title: Coleta de acesso a Artefatos Sensíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003983383
version: 8
---

## 📘 Visão Geral

O **Serviço de Coleta de Acesso a Artefatos Sensíveis** tem como objetivo **rastrear e registrar o acesso de usuários a artefatos considerados sensíveis** dentro do ecossistema RM.

Esses artefatos podem estar contidos em **consultas SQL**, **relatórios RM Reports** ou **planilhas .NET**, e seu monitoramento garante maior segurança e rastreabilidade no uso de dados sigilosos.

Todas as informações coletadas são armazenadas na tabela **`GHSTACESSOSENSIVEL`**, que centraliza os registros de acessos de forma unificada e padronizada.

---

## 🗃️ Estrutura da Tabela `GHSTACESSOSENSIVEL`

| Campo | Tipo | Descrição |
| --- | --- | --- |
| **ID** | UNIQUEIDENTIFIER | Identificador único (GUID) do acesso registrado |
| **CODCOLIGADA** | INT | Código da coligada associada ao artefato sensível |
| **TIPOARTEFATO** | CHAR(1) | Tipo de artefato sensível acessado: • **C** → Consulta SQL • **R** → RM Reports • **P** → Planilha .NET |
| **APLICACAO** | CHAR(1) | Código da aplicação onde o artefato está localizado |
| **CODARTEFATO** | VARCHAR(150) | Código identificador do artefato sensível |
| **TABELA** | VARCHAR(255) | Nome da tabela de banco de dados acessada |
| **COLUNA** | VARCHAR(255) | Nome da coluna acessada |
| **RECCREATEDBY** | VARCHAR(50) | Usuário que acessou o artefato sensível |
| **RECCREATEDON** | DATETIME | Data e hora em que o acesso ocorreu |

Todos os registros são identificados unicamente pelo campo `ID` (GUID), permitindo auditorias completas e sem risco de duplicidade.

---

## 🧠 Funcionamento Geral

A coleta dos acessos é **condicional**:  
O sistema **só registrará acessos** se existir pelo menos um **artefato sensível cadastrado** na tabela **`GARTEFATOSENSIVEL`**.

| Tabela | Finalidade |
| --- | --- |
| **GARTEFATOSENSIVEL** | Contém a lista de artefatos classificados como sensíveis. Define **quais consultas, relatórios e planilhas** devem ter seus acessos monitorados. |

Durante a execução normal das aplicações, o serviço monitora as ações do usuário e verifica, antes de cada acesso, se o artefato está marcado como sensível.

---

## 🧩 Escopo de Monitoramento

O serviço coleta acessos de **três tipos de aplicações RM**:

### 1️⃣ Consultas SQL

Quando o usuário executa uma **Consulta SQL**:

* O sistema identifica o **código do artefato** (consulta);
* Verifica se existe um **registro correspondente em `GARTEFATOSENSIVEL`**;
* Caso positivo, cria um registro em `GHSTACESSOSENSIVEL` com as informações:

  + Coligada
  + Aplicação
  + Tabela e coluna acessadas
  + Usuário e data do acesso

Consulta “CS\_ALUNOS\_DADOS” possui campos registrados como sensível → ao ser executada, o acesso é gravado automaticamente.

---

### 2️⃣ RM Reports

Durante a **geração de relatórios RM Reports**:

* O serviço identifica o **código do relatório**;
* Valida se o artefato está cadastrado em `GARTEFATOSENSIVEL`;
* Caso positivo, cria um registro em `GHSTACESSOSENSIVEL` com as informações:

  + Coligada
  + Aplicação
  + Tabela e coluna acessadas
  + Usuário e data do acesso

Relatório “FIN\_LAN\_CONTÁBEIS” possui campos marcados como sensível → cada execução gera um registro de acesso no histórico.

---

### 3️⃣ Planilhas .NET

Quando uma **Planilha .NET** é aberta:

* O sistema verifica o **código da planilha** e compara com os artefatos sensíveis cadastrados;
* Caso positivo, cria um registro em `GHSTACESSOSENSIVEL` com as informações:

  + Coligada
  + Aplicação
  + Tabela e coluna acessadas
  + Usuário e data do acesso

Planilha “EXP\_FINANCEIRO\_ANALITICO” possui campos registrados como sensível → ao ser aberta, gera registro de acesso.

---

## 🔄 Fluxo Resumido do Processo

`Usuário executa funcionalidade(SQL / Report / Planilha)`

`↓`

`Sistema identifica tipo e código do artefato`

`↓`

`Verifica na tabela GARTEFATOSENSIVEL se o artefato é sensível`

`↓`

`Se SIM →` `grava registro na tabela GHSTACESSOSENSIVEL`

`Se NÃO → nenhuma ação é executada`

---

## ⚠️ Observações Importantes

* O serviço **não interfere na execução** das consultas, relatórios ou planilhas; ele apenas registra o acesso.
* Recomenda-se **manter a tabela `GARTEFATOSENSIVEL` sempre atualizada** com os artefatos realmente críticos.
* Os registros podem ser consultados para **auditorias internas**, **análises de conformidade (LGPD)** e **monitoramento de uso indevido**.
