---
content_hash: 020f1d44b3abc572799dd24df7ce86c326c6ee5c461fc62906371d8ccdaa647e
fetched_at: '2026-06-29T00:11:12.298525+00:00'
page_id: '65209013'
product: rm
source: tdn-rm
title: NF-e - Configuração Top Connect MSSQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65209013
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***MSSQL* |
| **Processo** | **:** | Configuração Top Connect MSSQL |
| **Subprocesso** | **:** | Configuração Top Connect MSSQL |
| **Data da publicação** | **:** | 05/07/2013 |

**Instalação:**

O procedimento para a instalação é bastante simples, basta executar o instalador, e seguir os passos avançando “NEXT” até sua conclusão,um diretório será criado na pasta “Arquivos de Programas” no DISCO LOCAL.

**OBSERVAÇÃO:**  Caso a instalação esteja sendo realizada em uma maquina com o sistema operacional diferente de **Windows XP**, será necessário realizar a instalação do TopConnect em modo COMPATIBILIDADE. Esta instalação é necessária para a criação do serviço TOP CONNECT, no gerenciador de serviços do sistema operacional (services.msc).

Para realizar a instalação em compatibilidade, basta clicar com o botão direito do mouse sobre o instalador do Topconnect | Propriedades | aba compatibilidade - selecione o flag “ Executar este programa em modo de compatibilidade – **Widows XP** “:

                                        

**Criação da FONTE DE DADOS ODBC:**

Para utilizar o Topconnect em uma base SQL, é necessário configurar uma fonte de dados  ODBC,da seguinte maneira:

1- Acessar o Painel de controle | Ferramentas Administrativas |Fonte de Dados (ODBC).

Na pasta “**Fontes de Dados do Sistema**”, clicar em “Adicionar” e selecionar o DRIVER SQL SERVER. 

**OBSERVAÇÃO**: Caso o sistema operacional seja **64 Bits**, o caminho da fonte de dados é diferente:  C: |Windows |siswow64 |executar o arquivo ODBCAD32.exe.

2- Para adicionar o Driver é necessário informar os dados abaixo: \*Servidor – Informar o Servidor onde está instalado o Banco de Dados SQL.

3- A configuração do Logon deve ser parametrizada conforme abaixo e nos campos identificação de “Logon e Senha” deve ser preenchidos com seu usuário e senha de acesso ao  Banco de dados. 

4- Nesta tela deve-se marcar o parâmetro “Alterar o Banco de Dados” para, e selecionar uma Base de Dados válida (não é recomendada a utilização da base CORPORE, recomendamos que seja criada uma base especifica para os dados do TSS, onde o usuário utilizado no passo anterior tenha permissão total na mesma).

5- Nesta próxima etapa não é necessário alterar as configurações, basta finalizar e testar a conexão. 

6 – Verifique se foi criado seu ambiente como na imagem abaixo:

**Configuração do TopConnect:**

1 - Para iniciar o aplicativo, é necessário que o serviço “TOPConnect 4.0 Server” esteja iniciado. Para verificar o status do serviço, acesse o gerenciador de serviços do sistema operacional (services.msc).

Ao iniciar o aplicativo, irá aparecer uma janela com o nome do servidor TopConnect, como mostra a figura abaixo com as portas “Servidor: localhost” e a “Porta:7890” como default:

                                                                                                                                  

2 -  Após clicar em OK, o TopConnect irá iniciar uma tela mostrando as informações de conexão com o banco de dados:

3 - Na aba Configurações, sub aba Microsoft SQL, preencha os campos nome e senha com os dados do usuário utilizado para criação da fonte de dados ODBC:

4 - Após salvar as configurações do usuário, acesse a aba Assistentes | validação de conexão. Selecione o tipo de banco de dados.Este processo é executado para testar a comunicação entre o Topconnect e base de dados.

5 - Será solicitado o preenchimento do nome do ambiente a ser testado. Preencha o nome da fonte de dados ODBC criada, clique em finalizar logo em seguida OK:

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
