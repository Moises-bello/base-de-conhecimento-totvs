---
content_hash: 5d8860ad331c5c8b32d5da34d753e564301be2741b91e27c495da230a28c5e13
fetched_at: '2026-06-29T00:06:10.461768+00:00'
page_id: '203763227'
product: rm
source: tdn-rm
title: DT_Correlação_SADT_MatMed_Guia_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203763227
version: 4
---

# Correlacionamento Entre MatMed, Exames e Guias

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios |  |  | | --- | | **Rotinas envolvidas** | | Elaboração de Contas | | Movimentação de Estoque | |
| **Parâmetro(s):** | 1 - "Opções / Parâmetros ./ Parâmetros Gerais / Faturamento II". Menu Relaciona MatMed a Exames".  2 - "Opções / Parâmetros / Integração RM Nucleus". Menu "Vincula Exame à Guia". |
| **Requisito (ISSUE):** | [PCREQ-7611](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7611 "PCREQ-7611") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | ORACLE, MSSQL |
| **Tabelas utilizadas:** | SZATENDMATMED, SZATENDSADT |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

   Elaboradas funcionalidades para possibilitar o correlacionamento entre MatMed, Exames e Guias.

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

Exibir, na geração do XML de SPSADT, os exames de acordo com as suas respectivas guias.

Foi criada a funcionalidade de vincular exame a uma guia:

Para vincular um SADT a uma guia, clique com o botão direito sobre o SADT desejado e selecione a opção “Vincula a uma guia”.

Selecione a guia desejada e clique em OK.

Relacione MatMed à Exames

Importante: Somente exames que estão associados à alguma guia, poderão ter MatMed relacionados.

Em Opções / Parâmetros / Parâmetros Gerais / Aba Faturamento II marque a opção ‘relaciona MatMed à exames’.

Em Opções / Parametros / Integração RM Nucleus inclua um novo tipo de movimentação, utilizando o tipo “Folha de Sala”.

Marque a opção “Vincula SADT a Exame".

Acesse o Menu “Estoques / Movimentação de Estoque” e inclua uma nova movimentação, utilizando o tipo recém criado.

Inclua um medicamento qualquer na movimentação e clicar em “confirmar todos os itens”.

Processe a movimentação.

Selecione o Exame da Conta, que terá os medicamentos relacionados e clique em OK.

Acesse a elaboração de contas do paciente e verifique o medicamento recém lançado. Deverá constar na aba “SADT Relac.”, o número da coluna “SEQDEBITOSADT” do exame selecionado.

Outra forma de selecionar o exame relacionado, é acessando a elaboração de contas, clicando com o botão direito do mouse no SADT desejado e selecionando a opção “Vincula a um Exame”.

Selecione o Exame desejado e clique em OK.

Feito isso, na geração do XML de SP/SADT, o sistema realizará a seguinte verificação:

1. Sistema irá verificar se os exames à serem lançado pertencem a alguma guia.
2. Caso pertençam, eles aparecerão na respectiva guia.
3. Caso não pertençam a nenhuma guia, aparecerão na primeira guia disponível da respectiva conta no XML.

   Quanto ao relacionamento dos MatMed com os exames, no momento da geração do XML, será realizada a seguinte validação:

1. Será verificado se o MatMed possui algum vinculo com exame.
2. Caso possua, será verificado se este exame possui vinculo com alguma guia.
3. Se possuir, o MatMed aparecerá na seção “Outras Despesas” da guia correspondente.
4. Se não possuir, será lançado na seção “Outras Despesas” da primeira guia da respectiva conta no XML gerado.
