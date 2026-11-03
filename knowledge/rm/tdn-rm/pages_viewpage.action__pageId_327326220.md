---
content_hash: de529aa2cb18dfed0e4f94bb7bcce8a875d8ed3b3f268e4d2f88f778b1d22cda
fetched_at: '2026-06-29T00:08:48.617638+00:00'
page_id: '327326220'
product: rm
source: tdn-rm
title: 1420491 RMSAU-1538 DT Parâmetro geral para abrir primeiramente a tela de busca
  de pacientes na inclusão do agenda de cirurgias.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327326220
version: 4
---

# Parâmetro geral para abrir primeiramente a tela de busca de pacientes na inclusão do agenda de cirurgias.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Agenda de Cirurgias - Pesquisa de Pacientes |  |  | | --- | | **Rotina(s) envolvida(s)** | | Opções / Parâmetros / Parâmetros Gerais | |
| **Parâmetro(s):** | Carrega pesquisa de paciente na agenda de cirurgias (Aba Registro e Controle III) |
| **Tickets relacionados** | 1420491 |
| **Requisito:** | RMSAU-1538 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZPARAM |
| **Sistema(s) Operacional(is):** | Windows® |

## **Descrição**

Criação do parâmetro "Carrega pesquisa de paciente na agenda de Cirurgias" (Aba Registro e Controle III), com a finalidade de ao clicar na inclusão da agenda de cirurgias abrir primeiramente a tela de busca de pacientes.

## **Procedimento para Utilização**

Acessar o RM SAUDE, Opções / Parâmetros / Parâmetros Gerais

Selecionar a Aba Registro de Controle III

Em Agenda de Atendimento marcar a opção "Carrega pesquisa de paciente na agenda de Cirurgias", Clicar no Botão Grava e após fechar a tela .

Acessar Atendimento / Agendamento / Agenda de Cirurgias

Clicar em incluir um novo agendamento.

A tela apresentada deverá ser a tela de Pesquisa de Pacientes, e ao pesquisar e selecionar um paciente, o mesmo será carregado na tela de Agenda de Cirurgias.
