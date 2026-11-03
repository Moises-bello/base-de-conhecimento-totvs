---
content_hash: 46548ae051d363a2177bb3131e7af2cd42132a7d7a43a6fbf3aba47bba40440a
fetched_at: '2026-06-29T00:06:15.540516+00:00'
page_id: '211059106'
product: rm
source: tdn-rm
title: DT_Lançamento_Automático_de_Itens_Originados_na_Agenda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211059106
version: 3
---

# Lançamento automático de itens originados da agenda

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Atendimento |
| **Rotina:** | |  | | --- | | **Rotina** | | Agendamento  Agenda de atendimentos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros gerais | |
| **Parâmetro(s):** | Opções /Parâmetros /Parâmetros Gerais/ Empresa/ Lança procedimento do agendamento na conta do paciente para convênios sem WS TISS |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Com o parâmetro "Lança procedimento do agendamento na conta do paciente para convênios sem WS TISS" marcado, ao realizar um agendamento informando um procedimento e em seguida realizar o atendimento externo, o sistema deve criar uma guia TISS falsa para que o procedimento seja lançado na conta do paciente, utilizando o mesmo processo que hoje existe para guias TISS solicitadas e autorizadas via Webservice.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release 12.1.8

1. Aplique o pacote da release 12.1.8 e execute o agendamento de exames pelo assistente.

## Procedimento para Utilização

1. Acesse a tela de configurações gerais para marcar o parâmetro que será responsável por lançar os procedimentos na conta do paciente
2. Na aba **Empresa**, marque o parâmetro **Lança procedimento do agendamento na conta do paciente para convênios sem WS TISS**.
3. Realize um agendamento selecionando um procedimento.
4. Chame o atendimento externo através da agenda. Ao salvar o atendimento, na aba **Guia/Autorização** será possível visualizar a guia falsa criada para lançamento na conta do paciente.
5. Ao entrar na tela de elaboração da conta do paciente, na aba correspondente ao tipo de procedimento será possível visualizar o item lançado. Como o deste exemplo foi uma consulta, ele é exibido na aba Honorários.

divs
