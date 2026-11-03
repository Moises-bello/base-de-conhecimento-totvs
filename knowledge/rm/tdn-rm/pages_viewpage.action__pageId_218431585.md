---
content_hash: 559e8ce26cf652d07a466896baff50272af062edee70c294143cc9c340ec324d
fetched_at: '2026-06-29T00:06:18.465190+00:00'
page_id: '218431585'
product: rm
source: tdn-rm
title: TTLYJ2_DT_Validação_na_Inclusão_Novas_Contas_Faturamento_de_Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=218431585
version: 7
---

# Validação na Inclusão de Novas Contas no Faturamento de Convênios

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento de Convênios | |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Foi alterado as validações para a inclusão de novas contas na opção de Faturamento de Convênios, ao incluir uma nova conta são validadas as informações do atendimento, analisando se a Unidade de Atendimento desta nova conta está atrelada a mesma Unidade de Faturamento da remessa, é verificado também, o Tipo do paciente (Interno e Externo) e o Tipo da Guia.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.8.100 deste chamado.

## Procedimento para Utilização

       1.    No TOTVS Gestão Hospitalar (RM Saúde), acesse Faturamento / Faturamento para Convênios.

              O sistema apresenta a janela de remessas criadas.

       2.    Selecione uma remessa e clique em Processos / Faturamento de Convênios.

       3.    Ao apresentar a tela de Wizard, clicar em Avançar >.

       4.    Selecione Incluir Conta e clique em Avançar novamente.

              Será apresentado a tela de pesquisa de paciente

       5.     Selecione um Paciente e clique em Ok.

                      Nesse momento o sistema vai validar se a Unidade de Faturamento do paciente selecionado é a mesma da remessa, se o Tipo do Paciente é o mesmo e se o Tipo da Guia é o mesmo.

divs
