---
content_hash: 37f113306601d44523102ed92fa9778a276f112d64119401023881e8ed9b7ee9
fetched_at: '2026-06-29T00:08:23.226500+00:00'
page_id: '269552793'
product: rm
source: tdn-rm
title: MSAU-3083 DT Inclusão Nome Social Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269552793
version: 113
---

# Inclusão do Nome Social do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Internação | | Registro de Atendimento Externo | | Painel de Classificação de Risco | | Painel de Atendimentos Eletivos | |
| **Banco(s) de Dados:** | Sql Server e Oracle |
| **Tabelas Utilizadas:** | SZPACIENTE |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Conforme a  **[DECRETO Nº 8.727, DE 28 DE ABRIL DE 2016](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/DEC%208.727-2016?OpenDocument),**foi incluído no cadastro do paciente, o campo Nome Social. Esse campo quando preenchido, que será apresentado nas telas de Registro de Internação e Registro de Atendimento Externo.

No Painel de Atendimentos Eletivos e Classificação de Risco ao invés de apresentar o nome do paciente a ser chamado na grid, será exibido o nome social se esse existir, caso contrário seguirá apresentando o nome do paciente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da biblioteca 12.1.13.130 deste chamado.

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse Atendimento / Internação / Registro de Internações.

O sistema apresenta a tela de registro de internação, verifique que na tela possui o campo Nome Social a ser informado

       2.            Acesse Atendimento / Pronto Atendimento/Ambulatório/ Registro de Atendimento Externo.

O sistema apresenta a tela de registro de internação, verifique que na tela possui o campo Nome Social a ser informado.

       3.            Acesse Atendimento / Pronto Atendimento/Ambulatório/ Toten de Pronto Atendimento

Chame uma senha para o painel de classificação de Risco e uma para o painel de Eletivos

       4.            Acesse Atendimento / Pronto Atendimento/Ambulatório/ Painel de Classificação de Risco ou Eletivos

Chame a senha e insira um paciente informando o seu nome social. Nas grid do painel será apresentada a informação do Nome Social se essa existir no cadastro do Paciente.

divs
