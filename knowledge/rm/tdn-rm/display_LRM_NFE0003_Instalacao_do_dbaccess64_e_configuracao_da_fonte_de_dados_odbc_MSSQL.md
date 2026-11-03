---
content_hash: a9952619a9a3cb91b622ee8b0c6c61fc9f772dde832fe16831968a2f45327a2b
fetched_at: '2026-06-29T00:08:10.191195+00:00'
page_id: '240302982'
product: rm
source: tdn-rm
title: NFE0003_Instalacao_do_dbaccess64_e_configuracao_da_fonte_de_dados_odbc_MSSQL
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0003_Instalacao_do_dbaccess64_e_configuracao_da_fonte_de_dados_odbc_MSSQL
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | Banco de dados MS SQL |
| **Ocorrência:** | Instalação do DBACCESS para Windows 64 bits e configuração da Fonte de Dados ODBC |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar na instalação do DBACCESS para Windows 64 bits e na configuração da fonte de dados ODBC. O DBACCESS é a atualização do TOPCONNECT , podendo ser utilizado um ou outro.  Não deve ser utilizado os dois ao mesmo tempo.  **IMPORTANTE:** Diferente do TOPCONNECT, devido o TOTVS DBACCESS já ser 64 bits, a fonte de dados ODBC deve ser criada em: **Acessar o Painel de controle | Ferramentas Administrativas |Fonte de Dados (ODBC).**  Duvidas quanto a criação da fonte de dados vide documento:  **Instalação:**  O totvsdbaccess\_4.2\_win64 não possui executável, para sua instalação, realize as instruções adiante.  Acesse o sistema como Administrador.  No Windows, clique Start (iniciar) | Computer (meu computador).  Na barra de endereço, informe %PROGRAMFILES% (%arquivos de programas%) e pressione ENTER.  Crie uma nova pasta clicando no botão direito  New (novo) + Folder(pasta).  Informe o nome TOTVSDBAccess64.  Copie e descompacte arquivo totvsdbaccess\_4.2\_win64\_aaaammdd.zip (onde aaaammdd se refere a build do produto) na pasta criada.  Para realizar o download do totvsdbaccess\_4.2\_win64\_aaaammdd.zip, Acesse o portal do cliente (<https://suporte.totvs.com/portal/p/10098/download>) | selecione a linha PROTHEUS e pesquise por DBACCESS.    **Instalar o TOTVS | DBAccess 64 bits como serviço do Windows:**  Acesse o prompt de comandos como Administrador.  Acesse o diretório base de instalação do TOTVS | DBAccess 64 bits | Utilize o comando cd %PROGRAMFILES%\TOTVSDBAccess64.  Execute o comando dbaccess64.exe -install.  Ao término o TOTVS | DBAccess estará configurado como um serviço do Windows.  **Remover o serviço do TOTVS | DBAccess 64 bits do Windows:** **Importante:** Antes de remover o serviço instalado, pare o serviço.  Acesse o *prompt* de comandos como **Administrador.**  Acesse o diretório base de instalação do TOTVS | DBAccess 64 bits | Utilize o comando **cd %PROGRAMFILES%\TOTVSDBAccess64.**  Execute o comando **dbaccess64.exe -remove.**  Ao término, o TOTVS | DBAccess não estará mais configurado como serviço do Windows. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
