---
content_hash: 5f11164474f48b30111b59f2e3bd1ad692e41249d95639edf6a203b8f4bd4755
fetched_at: '2026-06-29T00:06:25.033952+00:00'
page_id: '224129544'
product: rm
source: tdn-rm
title: DT_Transferência_de_Dados_para_Tarefa_de_Producao
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224129544
version: 1
---

# TRANSFERÊNCIA DE DADOS DO PERÍODO DO FUNCIONÁRIO PARA TABELAS DE PRODUÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | *Configurações/Períodos* | *Transferência* | |
| **Versões/Release:** | *12.1.4* |

## Descrição

Essa implementação consiste em disponibilizar ao usuário uma forma de transferir os dados do período do funcionário para a tabela de produção parcialmente. Foi implementado uma tela de wizard onde o usuário pode realizar uma seleção dos funcionários que deseja transferir os dados de arquivo morto para as tabelas de produção. Um novo anexo foi inserido na tela de períodos denominado “Período do Funcionário”, onde o usuário poderá visualizar os funcionário que foram transferidos para as tabelas de produção.

## Procedimento para Utilização

O processo de **Transferir dados para tabela de produção** esta localizado na tela de Períodos. Para acessá-la deve-se utilizar a nova MDI através no menu **Configurações / Períodos.**

Na visão de períodos na coluna arquivo morto, o usuário poderá visualizar quando os dados foram transferidos parcialmente, sendo representados pelo ícone em destaque na imagem abaixo:

Ao realizar a transferência através do menu **Processos / Transferir** **dados para tabelas de produção**, o sistema irá exibir a tela de wirzard do processo.

A tela de wizard do processo de transferir dados para tabela de produção, permite ao usuário transferir os dados para todos os funcionários do período selecionado através do parâmetro **Transferir registros para tabela de produção** **de todos os funcionários**. Caso o usuário deseje relizar a transferência de um determinado funcionário poderá utilizar o componente se seleção e informar o funcionário desejado.

Para visualizar os funcionários que foram transferidos para a tabela de produção o usuário poderá acessar o menu **Anexo / Período** do Funcionário na tela de **Períodos.**
