---
content_hash: 8fc4c702bbc80d9bb0ba5fb0504440ec5f6f7209d753a3edaccdc3757f2905ec
fetched_at: '2026-06-29T00:06:11.916121+00:00'
page_id: '204965374'
product: rm
source: tdn-rm
title: DT_Validação_de_Competência_de_Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=204965374
version: 3
---

# Validação da competência de faturamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento / Faturamento para Convênios | |
| **Parâmetro(s):** | Cadastros/Segurança/Perfis/Anexos/Parâmetros RM Saúde/Faturamento |
| **Requisito (ISSUE):** | [PCREQ-7607](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7607 "PCREQ-7607") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Realizada alteração do parâmetro para possibilitar o faturamento de competências para os seguintes modelos:

* Mês atual - Apenas deixa o usuário faturar utilizando a competência do mês atual.
* Mês anterior, atual e próximo - Deixa o usuário faturar além do mês atual, o anterior e o próximo.
* Qualquer competência - Deixa livre para o usuário faturar qualquer competência.

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

 

Cada perfil de segurança deve ser configurado caso o administrador do sistema necessite bloquear o faturamento por competências superiores ou inferiores à um mês. Para isso:

* + Acesse o cadastro de perfis em **Cadastros/Segurança/Perfis.**
  + Selecione um perfil, clique em **Anexos/Parâmetros RM Saúde.**
  + No grupo **Faturamento** escolha entre as opções disponíveis.

Por padrão, todos os perfis tem marcada a opção "**Qualquer competência**".

Ao realizar o processo de faturamento para convênios na MDI .NET (RM.exe) em "**Faturamento/Faturamento para Convênios**", é executado um wizard e no campo "**Competência**" o sistema validará o parâmetro acima e irá exibir uma mensagem de aviso se o usuário informar uma competência maior ou menor que a permitida.

Este campo "**Competência**" somente é exibido caso o convênio exija o faturamento por competência, marcando o parâmetro em: "**Cadastros/Faturamento/Condições contratuais com convênios/Aba Parâmetros II** **/ Exige faturamento por competência**".
