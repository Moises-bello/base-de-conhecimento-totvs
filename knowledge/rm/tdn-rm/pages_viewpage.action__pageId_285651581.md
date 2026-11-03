---
content_hash: bf801bae38c20785acbc398b8b73d52261b6d6158437142dad25c7f5f4e4b9be
fetched_at: '2026-06-29T00:08:38.393095+00:00'
page_id: '285651581'
product: rm
source: tdn-rm
title: DT Inclusão de Boletos para Lançamentos com os Campos "Tipo de Juros ao dia,
  Juros ao Dia, Carência Juros e Multa ao Dia" com Valores Diferentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285651581
version: 108
---

# Inclusão de boletos para lançamentos com os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia com valores diferentes

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Boletos* | *Inclusão de Boletos* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastro de Boletos* | *Cadastro de Boletos* | | Alteração Global de Boletos | Alteração Global de Boletos | |
| **Cadastros Iniciais:** | **Lançamentos, Convênio, Conta/Caixa.** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1113 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql-Server, Oracle* |
| **Tabelas Utilizadas:** | *FLAN, FLANBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Permitir inclusão de boletos para vários lançamentos mesmo com os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia diferentes entre eles.

Foi disponibilizado no cadastro de convênio os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia, para que seja possível cadastrar valores default. Esses valores serão utilizados ao efetuar a inclusão de um boleto para vários lançamentos quando os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia for diferente entre eles. Caso não haja valor default configurado, o boleto será criado com os campos vazio.

No cadastro de boleto, os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia foram liberados para edição quando o boleto está em aberto e não remetido. Os campos também foram liberados no processo de alteração global de boleto

## Procedimento para Utilização

       1.            Definir default para os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia no cadastro de convênio - Menu Movimentações Bancárias | Convênio | Aba Cobrança Bancária

       2.            Após incluir o boleto os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia poderão ser editados para boletos em aberto e não remetido.

       3.            No cadastro de Boleto | Processo Alteração Global de Boleto foi disponibilizado os campos Tipo de Juros ao dia, Juros ao Dia, Carência Juros e Multa ao Dia

## Vídeo

600400

divs
