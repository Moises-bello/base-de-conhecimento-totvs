---
content_hash: 4cbb3d49d7ae871c5916d4e1702745dc25605ffa029ee0a933988bb6aaf43861
fetched_at: '2026-06-29T00:08:38.533364+00:00'
page_id: '285661931'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-34 DT Concessão de Bolsas Futuras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285661931
version: 111
---

# CONCESSÃO DE BOLSAS FUTURAS EM PERÍODOS DIFERENTES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM.** |
| **Segmento:** | *Educacional.* |
| **Módulo:** | **Totvs Educacional.** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Concessão de Bolsas Futuras* | **Concessão de Bolsas Futuras** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de concessões de bolsas** | **Cadastro de concessões de bolsas** | | **Cadastro de habilitação de concessão de bolsa futura** | **Cadastro de habilitação de concessão de bolsa futura** | | **Cadastro de serviço de concessão de bolsa futura** | **Cadastro de serviço de concessão de bolsa futura** | | **Assistente de concessão de bolsas futuras** | **Assistente de concessão de bolsas futuras** | | **Inclusão de bolsas concedidas no contrato do aluno** | **Inclusão de bolsas concedidas no contrato do aluno** | |
| **Cadastros Iniciais:** | *Alunos Cursos / Habilitações dos Alunos (Ensino Superior) Serviços Bolsas Bolsas por período letivo Contratos Parcelas* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *N/A* |
| **País(es):** | *Todos os países* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SCONCESSAOBOLSA, SCONCESSAOBOLSACOMPL, SCONCESSAOBOLSAHABALUNO,*  *SCONCESSAOBOLSAHABFILIAL, SCONCESSAOBOLSASERVICO, SBOLSAALUNO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

A fim de permitir a inclusão de mais de uma concessão de bolsa futura para uma mesma bolsa, mesmo aluno em períodos de datas (data inicial e data final) diferentes, foram alteradas as chaves primárias das tabelas relacionadas a concessão de bolsa bem como validações dos períodos (data inicial e data final) na inclusão da concessão. A inclusão da bolsa no contrato também passará a fazer as validações pertinentes às inclusões de bolsas (manuais ou via processo de inclusão). Foram acrescentados os campos **IDCONCESSAOBOLSA** que será um identificador para concessão de bolsa nas tabelas relacionadas à concessão (**SCONCESSAOBOLSA**, **SCONCESSAOBOLSAHABFILIAL**, **SCONCESSAOBOLSAHABALUNO**, **SCONCESSAOBOLSASERVICO**, **SCONCESSAOBOLSACOMPL**). Esse campo passou a fazer parte das chaves primárias das tabelas citadas bem como das chaves estrangeiras das tabelas com a tabela principal de concessão **SCONCESSAOBOLSA**. Esse identificador passou a ser um campo autoincrementável por coligada controlado por uma linha na **GAUTOINC** com **CODAUTOINC** = '**IDCONCESSAOBOLSA**'. Foram feitas somente alterações no comportamento do sistema não sendo necessária nenhuma alteração em tela.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado.
2. Para versões anteriores à 12.1.18 (11.82, 12.1.15, 12.1.16 ou 12.1.17), será necessário executar o script de marcação '**CN.2017.07\_03**' que realizará as alterações necessárias no banco de dados e passará a informar para o sistema que o mesmo aceitará mais de uma concessão da mesma bolsa para o mesmo aluno em períodos diferentes. A marcação citada deverá existir na **GSCRIPT** para que o sistema tenha o comportamento proposto, caso contrário, mesmo com a atualização do patch desse chamado, o sistema continuará se comportando da forma antiga, ou seja, permitindo somente uma concessão para uma mesma bolsa e mesmo aluno.

## Atualizações na base de dados

1. *Acréscimo do campo IDCONCESSAOBOLSA na tabela SCONCESSAOBOLSA e alteração da chave primária da tabela para (CODCOLIGADA, IDCONCESSAOBOLSA)*
2. *Criação de um índice utilizando a chave antiga (CODCOLIGADA, RA, CODBOLSA)*
3. *Acréscimo do campo IDCONCESSAOBOLSA na tabela SCONCESSAOBOLSACOMPL e alteração da chave primária da tabela para (CODCOLIGADA, IDCONCESSAOBOLSA)*
4. *Criação da chave estrangeira entre SCONCESSAOBOLSACOMPL e SCONCESSAOBOLSA utilizando os campos* *(CODCOLIGADA, IDCONCESSAOBOLSA)*
5. *Acréscimo do campo IDCONCESSAOBOLSA na tabela SCONCESSAOBOLSAHABALUNO e alteração da chave primária da tabela para (CODCOLIGADA, IDCONCESSAOBOLSA, IDHABILITACAOFILIAL)*
6. *Criação da chave estrangeira entre *SCONCESSAOBOLSAHABALUNO* e SCONCESSAOBOLSA utilizando os campos* *(CODCOLIGADA, IDCONCESSAOBOLSA)*
7. *Criação de um índice utilizando a chave antiga (CODCOLIGADA, RA, CODBOLSA, IDHABILITACAOFILIAL)*
8. *Acréscimo do campo IDCONCESSAOBOLSA na tabela SCONCESSAOBOLSAHABFILIAL e alteração da chave primária da tabela para (CODCOLIGADA, IDCONCESSAOBOLSA, IDHABILITACAOFILIAL)*
9. *Criação da chave estrangeira entre *SCONCESSAOBOLSAHABFILIAL* e SCONCESSAOBOLSA utilizando os campos* *(CODCOLIGADA, IDCONCESSAOBOLSA)*
10. *Criação de um índice utilizando a chave antiga (CODCOLIGADA, RA, CODBOLSA, IDHABILITACAOFILIAL)*
11. *Acréscimo do campo IDCONCESSAOBOLSA na tabela SCONCESSAOBOLSASERVICO e alteração da chave primária da tabela para (CODCOLIGADA, IDCONCESSAOBOLSA, CODSERVICO)*
12. *Criação da chave estrangeira entre *SCONCESSAOBOLSASERVICO* e SCONCESSAOBOLSA utilizando os campos* *(CODCOLIGADA, IDCONCESSAOBOLSA)*
13. *Criação de um índice utilizando a chave antiga (CODCOLIGADA, RA, CODBOLSA, CODSERVICO)*
14. *Inserção de registros na GAUTOINC para identificadores de concessões de bolsas com o código de autoinc IDCONCESSAOBOLSA por coligada*
15. *Preenchimento dos campos identificadores de concessão nas respectivas tabelas*

## Diagrama atualizado (DER)

## Alterações em telas e funcionalidades

1. Alteração do campo "Inserir bolsa automaticamente" para "Concessão ativa" no cadastro de concessão de bolsas futuras
2. Alteração do campo "Inserir bolsa automaticamente" para "Concessão ativa" no assistente de concessão de bolsas futuras
3. Ajustado também o ícone exibido ao término do processo do assistente de Concessão de bolsas futuras para que se comporte da seguinte maneira:

   1 - Se NÃO existirem mensagens de erro ou advertência no log, sistema exibirá o ícone de execução com sucesso.

   2 - Se existir no log somente mensagens de erro, sistema exibirá o ícone de execução com erros.

   3 - Para qualquer outra situação que não se enquadre nas situações descritas acima, sistema exibirá o ícone de advertência.
4. Permissão de se inserir a mesma bolsa para um mesmo aluno em períodos distintos.

## Vídeo

* *Vídeo hospedado no youtube e inserido no template por meio da macro **Widget Connector**.*

*\*\* Canal do youtube e software de vídeoem definição.*

|  |  |
| --- | --- |
| **Título do Vídeo:** | *Disponibilizado pelo Marketing.* |
| **Introdução:** | *Disponibilizado pelo Marketing.* |
| **Passo a Passo:** | *Capturar diretamente do sistema.* |
| **Finalização:** | *Disponibilizado pelo Marketing.* |

divs
