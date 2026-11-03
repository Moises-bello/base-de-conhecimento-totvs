---
content_hash: e029ad8e7e6f93556580711c12368c71d3de26fb723f72e6f9fe1b7857c4e676
fetched_at: '2026-06-29T00:09:16.929032+00:00'
page_id: '421387660'
product: rm
source: tdn-rm
title: 3835464 DSAUGHCOM-1089 DT Cadastro de Padrão de Prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421387660
version: 3
---

# Cadastro de Padrão de Prescrição - Prontuário RM e PEP 2.0

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Cadastros / Cuidados com o paciente / Prescrição Médica / Padrões de Prescrição   |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Padrões de Prescrição | SauPrincipioAtivoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Prontuário |  | | Integração PEP 2.0 (Princío Ativo) | SauPrinciple | |
| **Tickets relacionados** | <https://totvssuporte.zendesk.com/agent/tickets/3835464> |
| **Requisito/S****tory/Issue:** | <http://jiraproducao.totvs.com.br/browse/DSAUGHCOM-1089> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZPRINCIPIOATIVO |
| **Sistema(s) Operacional(is):** | Windows® |
| ****Scripts Solicitados:**** | SA.2018.10\_03: Inclusão da coluna UTZPEP na tabela SZPRINCIPIOATIVO |

## Descrição

Implementação de melhoria para configurar a usabilidade dos Padrões de Prescrição para: apenas Prontuário (RM Saúde), apenas PEP 2.0, ou ambos.

## Procedimentos para Utilização

## Cadastro:

**Passo 1. Acessar os Cadastros / Cuidados com o Paciente / Prescrição Médica / Padrões de Prescrição.**

**Passo 2. Selecionar um Princípio Ativo já existente ou incluir um novo registro.**

**Passo 3. Na tela de cadastro do Princípio Ativo será possível definir para quais prontuários o Padrão de Prescrição será disponibilizado (com o valor default para Ambos).**

## Usabilidade:

## **Para exemplificar a usabilidade dessas novas opções, foram cadastrados 3 Princípios Ativos, um para cada opção.**

**- Prontuário (RM Saúde):**

**Passo 1. Acessar o Prontuário / Prescrição Médica.**

**Passo 2. Acessar a pesquisa por Medicamentos e pesquisar pelo Princípio Ativo ou pelo Nome Comercial do medicamento vinculado ao Padrão de Prescrição. Serão exibidos apenas os Princípios Ativos definidos para o Prontuário ou para Ambos:**

**Passo 3. Pesquisar diretamente pelo Princípio Ativo ou pelo Nome Comercial do medicamento vinculado ao Padrão de Prescrição. Serão exibidos apenas os Princípios Ativos definidos para o Prontuário ou para Ambos:**

**- PEP 2.0:**

**Passo 1. Acessar o Prontuário Eletrônico / Aleta de Prescrição Médica.**

**Passo 2. No painel de Medicamentos, pesquisar pelo Princípio Ativo ou **pelo Nome Comercial do medicamento vinculado ao Padrão de Prescrição. Serão exibidos apenas os Princípios Ativos definidos para o PEP 2.0 ou para Ambos:****
