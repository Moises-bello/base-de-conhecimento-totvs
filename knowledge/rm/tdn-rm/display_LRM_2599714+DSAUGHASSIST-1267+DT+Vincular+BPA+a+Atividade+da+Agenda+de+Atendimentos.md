---
content_hash: 217030fe6ddd4d6df69b012a2d886b3d82590377768e4ddccba323e745eb2531
fetched_at: '2026-06-29T00:09:09.156748+00:00'
page_id: '392501148'
product: rm
source: tdn-rm
title: 2599714 DSAUGHASSIST-1267 DT Vincular BPA a Atividade da Agenda de Atendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/2599714+DSAUGHASSIST-1267+DT+Vincular+BPA+a+Atividade+da+Agenda+de+Atendimentos
version: 2
---

# Vincular BPA a Atividade da Agenda de Atendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Atendimento | | Agenda de Atendimentos | | Lançamento de BPA | |
| **Parâmetro(s):** | Vincula BPA a Atividade da Agenda de Atendimento e gera automaticamente o lançamento de BPA quando for gerado um atendimento externo para agendamento com a atividade vinculada, sendo o convênio selecionado SUS. |
| **Ponto de Entrada:** | Agenda de Atendimentos |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação no sistema permite que o usuário crie a relação entre uma Atividade da Agenda de Atendimentos com Procedimentos do SUS. Com esta relação feita, o sistema deve lançar automaticamente os BPAs com os procedimentos associados, caso seja gerado um Atendimento Externo para o Agendamento com o convênio SUS. *O prestador do BPA é salvo automaticamente como o principal da unidade de faturamento, caso exista.*

## Associação Atividade Agenda - Procedimento SUS

### Passo 1:

Na MDI Delphi, Acesse **Cadastros > Uso Geral > Agendamento > Atividades**

### Passo 2:

Selecione uma Atividade e clique na aba **Procedimentos SUS**

### Passo 3:

Adicione um item, selecionando o procedimento e informando uma quantidade

## Criação do Atendimento Externo utilizando os Procedimentos associados na Atividade do Agendamento

### Passo 1:

Abra a **Agenda de Atendimentos** e crie um agendamento com a atividade onde os procedimentos do SUS foram incluídos.

### Passo 2:

Registre um Atendimento Externo para o agendamento criado.

### Passo 3:

Acesse **Faturamento > Faturamento SUS > Lançamento de Procedimentos BPA** e verifique se os BPAs foram lançados conforme cadastrados na Atividade.

Importante: Para o BPA ser lançado automaticamente, é necessário que a configuração abaixo esteja habilitada nos parâmetros gerais.
