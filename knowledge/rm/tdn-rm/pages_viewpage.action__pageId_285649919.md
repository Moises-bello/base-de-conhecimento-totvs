---
content_hash: db12d8512cb14b60f39a5e7ef694bf9cc2c47f6d76f8a65ffd83f85eea94690e
fetched_at: '2026-06-29T00:08:38.381661+00:00'
page_id: '285649919'
product: rm
source: tdn-rm
title: DT Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285649919
version: 107
---

# Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Lançamento - Acordo | Lançamento - Acordo |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Template de Acordo | Template de Acordo | |
| **Cadastros Iniciais:** | *Template de Acordo* |
| **Parâmetro(s):** | Template > aba Regras > Parâmetro Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produçãokey,summary,type,created,updated,due,assignee,reporter,priority,status,resolution0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1128 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql-Server, Oracle* |
| **Tabelas Utilizadas:** | FTEMPLATEACORDO |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foi disponibilizado no Cadastro de Template na aba Regras o parâmetro "Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido". Este parâmetro tem como objetivo permitir gerar acordo para lançamento com boleto com status CNAB igual a Registrado ou Remetido. O sistema executará o processo normalmente e manterá o boleto no lançamento original. O cancelamento desse boleto, que será através do processo manual ou do retorno bancário, será de responsabilidade do usuário do financeiro.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Na visão de **Template de Acordo**, acesse o template no qual será parametrizado com o novo parâmetro. Acesse a aba **Regras** e marque o parâmetro **"Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido"**.

|  |  |
| --- | --- |
| **Menu** | *Contas a Pagar / Receber* |
| **Submenu** | *Acordo -> Template Acordo -> Aba Regras (Tela de Inclusão/Edição).* |
| **Nome do Parâmetro:** | Permitir Acordo Para Lançamento Com Boleto Registrado Ou Remetido |
| **Descrição:** | Permite gerar acordo para lançamento com boleto com status CNAB igual a Registrado ou Remetido. |
| **Módulo** | *Totvs Gestão Financeira* |

## Procedimento para Utilização

Após o procedimento de configuração do novo parâmetro, selecione o lançamento que tenha um boleto registrado ou remetido e execute o processo de geração de acordo.

**Importante**: Note que depois de efetuar a geração do acordo o boleto do lançamento não é cancelado. O cancelamento desse boleto, que será através do processo manual ou do retorno bancário, será de responsabilidade do usuário do financeiro.

## Vídeo

## *.600400*

divs
