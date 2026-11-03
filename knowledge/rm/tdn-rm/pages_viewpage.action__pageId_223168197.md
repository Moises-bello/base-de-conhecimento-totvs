---
content_hash: c7d0cf22190dcff0b87b305e8a55439cb0feacab2176a4f94e94037eaebbd39a
fetched_at: '2026-06-29T00:06:21.301353+00:00'
page_id: '223168197'
product: rm
source: tdn-rm
title: DT_Solicitação_de_Status_da_Autorização_TISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223168197
version: 128
---

# Solicitação de Status da Autorização TISS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Atendimento |
| **Rotina:** | |  | | --- | | **Rotina** | | Agenda de atendimentos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Atendimento Externo | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server / Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Implementação possibilita a realização da consulta do status de uma solicitação TISS enviada para Auditoria/Análise.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.8 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.8.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.  
   3. Na barra de menu superior, clique em DOWNLOAD.  
   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.8  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse **Atendimento / Agendamento / Agenda de atendimentos**.
2. Realize um agendamento informando um procedimento que necessite de auditoria do Convênio.
3. Com a solicitação em análise, após a aprovação ou reprovação do convênio, abra o agendamento e clique em **Solicitação/Cancelamento**.
4. Uma nova tela será aberta com as informações da guia TISS. Clique em **Status da autorização**.
5. O sistema fará o envio da solicitação de status (similar ao envio da solicitação) e, caso a solicitação tenha sido aprovada pelo Convênio, a guia é atualizada para o status "**Autorizada**". Caso o Convênio reprove, a guia é atualizada para "**Não autorizada**" e o processo será realizado como se fosse uma guia de solicitação de procedimento.
6. Caso a guia tenha sido autorizada, ao realizar o atendimento do paciente, o sistema irá lançar o procedimento escolhido na aba "**Guia/Autorização**" e na "**Elaboração de Conta**" e caso tenha co-participação, o sistema lançará os valores na aba "**Gastos Particulares**", da mesma forma que uma guia de solicitação normal.
7. É possível realizar o mesmo procedimento descrito acima diretamente na tela de atendimento do paciente, sendo necessário lançar uma guia na aba "**Guia autorização**". O restante do processo é o mesmo, ou seja, tendo um guia "**Em análise**", é necessário clicar em "**Status da autorização**".
8. Ao clicar no botão "**Status da autorização**" o sistema realizará o envio da guia de status e atualizará o status, lançando os honorários na conta do paciente caso seja "**Autorizada**" ou apenas atualizando para "**Não autorizada**".

divs
