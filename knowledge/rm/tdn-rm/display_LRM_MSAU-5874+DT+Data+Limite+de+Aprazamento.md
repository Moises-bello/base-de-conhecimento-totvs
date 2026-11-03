---
content_hash: 1901fad36fb61a562aacf8df5edee76efdf80058568f341d9f769a7fd464649a
fetched_at: '2026-06-29T00:08:28.890677+00:00'
page_id: '271863946'
product: rm
source: tdn-rm
title: MSAU-5874 DT Data Limite de Aprazamento
type: documentation
url: https://tdn.totvs.com/display/LRM/MSAU-5874+DT+Data+Limite+de+Aprazamento
version: 113
---

# Data de Limite de Aprazamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prescrição Médica | Prontuário Eletrônico - Prescrição Médica | |
| **Parâmetro(s):** | Menu Opções / Parâmetros / Parâmetros Gerais aba Prontuário Eletrônico, sub aba Prescrição: parâmetro "Não gera horário de aprazamento igual ao horário limite". |
| **Issue:** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5MSAU-5874 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro "**Não gera horário de aprazamento igual ao horário limite**" para quando o horário final do aprazamento selecionado pelo médico for exatamente igual ao horário limite, o último horário será cortado do aprazamento.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções/ Parâmetros / Parâmetros Gerais**.
2. Acesse a aba **Prontuário Eletrônico** e a sub aba **Prescrição**.
3. Marque o parâmetro "**Não gera horário de aprazamento igual ao horário limite**".

## Procedimento para Utilização

**Exemplo:**

1. Após estar com o parâmetro marcado, acesse o menu **Prontuário** e escolha o paciente desejado.
2. Na aba **Prescrição Médica**, clique para incluir uma nova prescrição.
3. Prescreva um item com a frequência desejada.
4. Caso a frequência termine exatamente no mesmo horário do horário limite parametrizado nos parâmetros gerais, o sistema não irá gerar o último horário de aprazamento.

divs
