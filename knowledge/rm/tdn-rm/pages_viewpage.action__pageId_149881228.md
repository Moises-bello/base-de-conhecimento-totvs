---
content_hash: 3f667ae658781d6333fe2121647d0b90c3a145f217cfd15c0ea6f74646864096
fetched_at: '2026-06-29T00:05:56.012848+00:00'
page_id: '149881228'
product: rm
source: tdn-rm
title: Utilizando a atividade "Adicionar Registro na Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881228
version: 11
---

# Adicionar Registro na Tabela:

---

Permiti que o usuário consiga inserir novos registros em uma determinada tabela.

|  |  |  |  |
| --- | --- | --- | --- |
| **Atividade** | **Propriedades** | **Função** | **Valor** |
|  | Nome do Data Server | Qual o Data Server será utilizado | GlbAtributoTipoData |
|  | **Código** | Código do registro que será inserido | -1 (O campo código é inserido automaticamente pelo processo) |
| **Nome** | Nome do registro que será inserido | Critério do usuário |
| **Tipo de Dados da Linguagem** | Tipo de dados lógico (C#) | System.Int32 |
| **Tipo de Dados Oracle** | Tipo de dados do banco de dados | Number(10,0) |
| **Tipo de Dados SQL** | Tipo de dados do banco de dados | Int |
| Tabela | Em qual tabela o registro será inserido | Activity=rmsReadRecordActivity1, Path=Tables["GMDATRIBUTOTIPO"].DataTable |
|  | Atividade Ler Registro | Salva o registro com os parâmetros passados pela atividade Adicionar Registro na Tabela | Nome da Atividade de Ler Registro |

falseObservação:

As propriedades em negrito são as colunas da tabela selecionada pela propriedade Tabela.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e Superiores

false

**Processo:** Fórmula Visual - Utilizando a atividade "Adicionar Registro na Tabela"

falsefalse

**Status:** Finalizado

false

**Data:** 10/05/2016

false

**Autores:**
