---
content_hash: bb72085f1dcff279646af72d54a60b478114d4e92276664e020ca2bc5d1330ba
fetched_at: '2026-06-29T00:06:22.542976+00:00'
page_id: '223920497'
product: rm
source: tdn-rm
title: Utilizando Excel como Fonte de Dados Externa
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Excel+como+Fonte+de+Dados+Externa
version: 154
---

# Utilizando Excel como Fonte de Dados Externa

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.80.XX e Superiores |
| **Ocorrência:** | Utilizando Excel como Fonte de Dados Externa |
| ****Passo a passo:**** | Objetivo  ---   Esta página tem por objetivo demonstrar como configurar uma Planilha de Excel para uso em fonte de dados externa. Como fazer  ---     Para utilizar uma Planilha de Excel como Fonte de Dados Externo, através do cadastro de consultas SQL, se deve, primeiramente, verificar algumas condições.    1ª O serviço do Host deve estar configurado para executar como administrador.   Alterando modo de execuçãoPropriedades do Arquivo  | 1. Acesse o diretório\* da instalação do host do sistema. 2. Selecione e edite o arquivo de host utilizado. 3. Clique com o botão direito do mouse e escolha a opção “Propriedades”.        \*  Padrão: "C:\totvs\CorporeRM\RM.Net" |  | | --- | --- |  Alterando Compatibilidade  | 1. Nas propriedades do arquivo selecione a guia “Compatibilidade”. 2. Na visão posterior marque a opção “Executar este programa como administrador” 3. Clique em OK. |  |  |  | | --- | --- | --- | --- |     2ª Depois de configurado o serviço do servidor de aplicação o ODBC deve ser configurado. Para isso, acesse: "Painel de Controle | Ferramentas Administrativas | Fontes de Dados (ODBC)".    Na aba **Fonte de Dados do Sistema**, clique em Adicionar, selecione a opção Microsoft Excel Driver (\*xls, \*xlsx, \*xlsm, \*xlsb) e clique em Concluir.    Na tela seguinte defina o nome da Fonte de Dados e selecione a planilha que servirá de fonte, clicando no botão "Selecionar pasta de trabalho". Feita a seleção clique em OK e conclua a criação da conexão ODCB.     ATENÇÃO   Caso o sistema operacional utilizado seja 64 bits é possível que possua duas versões do ODBC, a versão 32 e 64 bits. Verifique qual delas possui o driver do Excel disponível para uso.  Caso a versão utilizada do Microsoft Office seja 32 bits é necessário que o RM seja executado em 32 bits, deve-se então, executar o aplicativo CorFlags.exe para o RM.exe e o RM.Host.Service.exe.   Executando Corflags  | 1. Abra o prompt de comando do Windows e acesse a pasta de instalação do RM (Padrão "C:\totvs\CorporeRM\RM.Net") com o comando cd c:\totvs\CorporeRM\RM.Net 2. Execute o aplicativo CorFlags.exe para o RM.exe e para o RM.Host.Service.exe com os seguintes comandos:      1. CorFlags.exe RM.exe /32bit+    2. CorFlags.exe RM.Service.exe /32bit+ |  | | --- | --- |           ---     3ª Feita as configurações a cima já é possível configurar uma consulta SQL com fonte de dados de uma planilha de Excel.  No cadastro de consultas SQL clique no botão destacado para associar e/ou cadastrar uma Fonte de Dados Externa     BANCO DE DADOS EXTERNOPesquisa/Inclusão de uma fonte de Dados  | * Na tela seguinte é possível pesquisar por uma fonte de dados criada ou clique em Incluir para cadastrar uma nova conexão. |  | | --- | --- |  Criando Fonte de Dados  | 1. Na formulário seguinte preencha as informações da conexão e clique no botão destacado, para preencher as informações da string de conexão. 2. Na tela aberta, selecione a opção Microsoft ODBC Data Source e clique em OK. 3. Na tela de propriedades da conexão selecione a conexão criada no ODBC anteriormente, clique no botão Test Connection para testar a conexão, posteriormente clique em OK. |  |  |  | | --- | --- | --- | --- |     Salve as informações da fonte de dados cadastrada e selecione-a no lookup da pesquisa de fonte de dados.  No cadastro de consultas SQL o select criado deverá conter a seguinte estrutura:    Onde o NOME\_DA\_SHEET deve ser igual ao nome da Sheet desejada no arquivo do Excel, seguido pelo caractere $ (cifrão). Para selecionar os dados da planilha da imagem abaixo, o comando SQL deve ser formulado da seguinte forma:     | Planilha de Excel | Cadastro da consulta SQL associada a fonte de dados Excel | Resultado do Select | | --- | --- | --- | |  |  |  | |
| **Ambiente:** |  |
| **Observações:** | Caso a mensagem abaixo seja exibida, verifique se o Office instalado está executando na mesma versão que o RM (Host e RM.exe). Se o Office for 32 bits o RM também deverá executar em 32 bits para seu correto funcionamento. Nesta página há um explicativo desta ação. |

divs
