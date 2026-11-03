---
content_hash: 0dc9b720e4e17dee64eae678c001871a20bc9ea812ec64ab12be26387f9d08c7
fetched_at: '2026-06-29T00:08:22.191733+00:00'
page_id: '269081443'
product: rm
source: tdn-rm
title: 94976_Parametro_Validacao_Inadimplencia_Situacao_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/94976_Parametro_Validacao_Inadimplencia_Situacao_Matricula
version: 114
---

# CRIAÇÃO DE PARÂMETRO PARA VALIDAÇÃO DE INADIMPLÊNCIA NA SITUAÇÃO DE MATRICULA DO ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula Online no Portal* | *Matrícula Online no Portal* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado com usuário no portal;*  *2) Aluno matriculado no período letivo;*  *3) Período Letivo liberado para matrícula no portal;* |
| **Parâmetro(s):** | *Educacional | RM Portal | RM Portal - Matrícula | Portal - Matrícula / Geral 4/5 | Débitos financeiros | Bloquear alunos*  **Educacional | RM Portal | RM Portal - Matrícula | Portal - Matrícula / Geral 4/5 | Débitos financeiros | Verificar débitos em conta corrente**  ****Educacional | RM Portal | RM Portal - Matrícula | Portal - Matrícula / Geral 5/5 | Biblioteca | Bloquear alunos com débitos financeiros**** |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SSTATUS* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste nas validações de inadimplência na matrícula online, no portal, através de um novo parâmetro no cadastro de situação de matrícula, a fim de permitir que o aluno possa realizar a matrícula em disciplinas mesmo que ele esteja inadimplente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.15)* deste chamado.

## Procedimento para Utilização

É necessário que seja parametrizado no TOTVS Gestão Educacional a utilização de bloqueio para aluno inadimplentes.

 Existem dois parâmetros, no Educacional, que definem o uso de bloqueio de pendências financeiras:

* + Bloqueio de alunos com pendências financeira no TOTVS Gestão Educacional:

* + Bloqueio de alunos com pendências financeiras no TOTVS Gestão Bibliotecária:

Após a parametrização de uso de bloqueio de matrícula para alunos inadimplentes, será possível definir na Situação de Matrícula determinadas situações que podem liberar a realização de matrículas em disciplinas para o aluno, mesmo que hajam pendências financeiras.

O parâmetro "Validar inadimplência de aluno na matrícula pelo portal", no cadastro de Situação de Matrícula, permitirá os alunos que estiverem nessa situação possam realizar matrículas em disciplinas no portal. Porém, mesmo com a liberação o portal irá apresentar todos os débitos do aluno após a seleção do período letivo.

Situação de matrícula: ***Educacional | Currículo e Oferta | Situação de matrícula***

#### Matrícula Online:

divs
