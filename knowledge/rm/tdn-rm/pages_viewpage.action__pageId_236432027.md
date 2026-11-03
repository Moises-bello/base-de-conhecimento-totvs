---
content_hash: 15ca288f82d1de1b2af1c87bc1534fd60183047b0f3e26b5cb1988c0b3daf01f
fetched_at: '2026-06-29T00:08:06.063820+00:00'
page_id: '236432027'
product: rm
source: tdn-rm
title: TUMVK6_DT_Máscara_no_Celular_no_Agendamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236432027
version: 117
---

# Máscara no número de celular ao realizar um agendamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Agenda | |
| **Parâmetro(s):** | **Opções / Parâmetros / Parâmetros Gerais**, aba **Registro e Controle III,** parâmetro **"Utiliza máscara no Nº de celular ao Agendar."** |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | SZPARAM, SZAGENDAMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para que seja obrigatório informar um número de celular válido ou deixá-lo em branco.

## Procedimento para Utilização

1. Acesse **Opções / Parâmetros / Parâmetros Gerais**, aba **Registro e Controle III** e marque o parâmetro **"Utiliza máscara no Nº de celular ao Agendar."**
2. Acesse a **Agenda de atendimentos**.
3. Selecione uma agenda disponível.
4. Ao realizar o agendamento e não informar um número de celular válido(DDD+Número do telefone) , o sistema não permitirá salvar o agendamento até que se corrija o número ou deixe-o em branco.

divs
