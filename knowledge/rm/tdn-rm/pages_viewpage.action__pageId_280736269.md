---
content_hash: 96b276b497339f8caa4e594a94e66a835de03367c640637d54227bf552182827
fetched_at: '2026-06-29T00:08:35.463838+00:00'
page_id: '280736269'
product: rm
source: tdn-rm
title: DT Médico Visualiza Todos os Pacientes em Observação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280736269
version: 113
---

# Médico pode Visualizar Todos os Pacientes em Observação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Risco | |
| **Cadastros Iniciais:** | Unidade de Atendimento deve estar permitindo realizar Classificação de Risco |
| **Parâmetro(s):** | Médico visualiza todos os pacientes em Observação e Finalizados no Atendimento Médico |
| **Banco(s) de Dados:** | SQL Server@, Oracle@ |
| **Tabelas Utilizadas:** | SZATENDIMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foi adicionado o parâmetro  "Médico visualiza todos os pacientes em Observação e Finalizados no Atendimento Médico" que selecionado, vai permitir que o Médico visualize na classificação de risco, todos os pacientes que estão aguardando em observação ou finalizados, não somente os pacientes que estão vinculados ao atendimento do médico, possibilitando esse, finalizar, transferir e visualizar o paciente em atendimento de outros médicos se assim desejar.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da biblioteca RM 12.1.16.122 deste chamado.

## Procedimento para Configuração

 **CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Na aba Classificação de Risco selecione o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Médico visualiza todos os pacientes em Observação e Finalizados no Atendimento Médico |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado |
| **Descrição:** | Permite o médico visualizar os pacientes que estão aguardando em observação para outros médicos ou que já foram finalizados. |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse com perfil médico a Classificação de Risco.

Previamente deve ser realizado o processo de chamada da senha para outros médicos até que esta esteja em observação

       2.            Na aba de Atendimento Médico será possível visualizar pacientes que estão aguardando em Observação ou com atendimento já finalizados que estão vinculados a outros médicos.

divs
