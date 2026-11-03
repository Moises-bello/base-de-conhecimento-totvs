---
content_hash: f170d04ffece2341bb0120ace26e353fe9417349952a1745481c5ebe351e40f6
fetched_at: '2026-06-29T00:06:10.512459+00:00'
page_id: '203763623'
product: rm
source: tdn-rm
title: DT_Alteração_no_Processo_de_Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203763623
version: 3
---

# Alteração no processo de faturamento para permitir retornar após erro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Faturamento para convênios | |
| **Requisito (ISSUE):** | [PCREQ-7611](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7611 "PCREQ-7611") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle, MSSQL |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

 Foram realizadas alterações na tela de processamento de remessa, visando maior controle por parte do usuário. Após as modificações, usuário pode, mesmo após erro no processamento, retornar para o passo anterior do processo e refazer a seleção dos atendimentos que irão compor a remessa.

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

1. Na nova MDI, acesse o menu "Faturamento / Faturamento para convênios" e inclua uma nova remessa para um convênio qualquer.
2. Marque a remessa e clique em "Processos / Faturamento para convênios".
3. Na tela de processo, preencha os campos obrigatórios e avance para a seleção de contas.
4. Selecione as contas desejadas (uma das contas deve conter algum erro impeditivo para o processamento, como por exemplo, erro no credenciamento de prestador.) e processar a remessa.
5. Sistema apresentará os erros, retornando, entre outras informações, o numero do atendimento com problema.
6. Retorne para a tela anterior, desmarque o atendimento com problema e processar novamente. O processamento ocorrerá com sucesso.
