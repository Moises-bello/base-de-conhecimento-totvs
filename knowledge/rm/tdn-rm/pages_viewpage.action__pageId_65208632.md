---
content_hash: 2083893f89f36d0fc9ebaa36e21253de1891a639ecccf5857177ec3273063310
fetched_at: '2026-06-29T00:11:12.247082+00:00'
page_id: '65208632'
product: rm
source: tdn-rm
title: NF-e - Configuração Top Connect ORACLE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65208632
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.50* |
| **Processo** | **:** | Configuração Top Connect ORACLE |
| **Subprocesso** | **:** | Configuração Top Connect ORACLE |
| **Data da publicação** | **:** | 03/07/2013 |

**Instalação:**

O procedimento para a instalação é bastante simples, basta executar o instalador, e seguir os passos avançando “NEXT” até sua conclusão, um diretório será criado na pasta “Arquivos de Programas” no DISCO LOCAL.

**OBSERVAÇÃO:**  Caso a instalação esteja sendo realizada em uma maquina com sistema operacional diferente de Windows XP, será necessário realizar a instalação do TopConnect em modo COMPATIBILIDADE. Esta instalação é necessária para a criação do serviço TOP CONNECT, no gerenciador de serviços do sistema operacional (services.msc).

Para realizar a instalação em compatibilidade, basta clicar com o botão direito do mouse encima do instalador do Topconnect, aba compatibilidade, selecionando o flag “ Executar este programa em modo de compatibilidade “:

Após instalação, acesse a pasta raiz de instalação do Topconnect ( diretório default: C:\Arquivos de programas\TOPConnect 4.0 ) e edite o arquivo topconn.ini.

Abaixo da linha [ORACLE], adicione o diretório da OCI.DLL, que é uma DLL especifica do Oracle. No meu caso, o diretório da OCI.DLL é: ”clientlibrary=C:\oracle\product\10.2.0\db\_1\BIN\oci.DLL” .

Salve as alterações e reinicie o serviço Topconnect no gerenciador de serviços do sistema operacional.

**OBSERVAÇÃO: Deve ser criada uma instância no Oracle, para acesso a base de dados na maquina em que o Topconnect estiver sendo configurado.**

**IMPORTANTE: a chave NLS\_LANG deve ser observado onde para o TSS e o TOPCONNECT deve ser utilizado a chave NLS LANG AMERICAN\_AMERICA.WE8MSWIN1252, caso esteja diferente, gentileza realizar os seguintes procedimentos:**

• Ir no iniciar/executar, digitar regedit e teclar ok.  
• Apertar a tecla F3 e mandar localizar NLS\_LANG  
• Todas as chaves NLS\_LANG que estão como Brazilian... Deverão ser alterada para AMERICAN\_AMERICA.WE8MSWIN1252   
• Ir teclando F3 até terminar todas as NLS\_LANG.”

**Configuração do TopConnect:**

Para iniciar o aplicativo, é necessário que o serviço “TOPConnect 4.0 Server” esteja iniciado. Para verificar o status do serviço, acesse o gerenciador de serviços do sistema operacional (services.msc).

Ao iniciar o aplicativo, irá aparecer uma janela com o nome do servidor TopConnect, como mostra a figura abaixo com as portas “Servidor: localhost” e a “Porta:7890” como default:

Após clicar em OK, o TopConnect irá iniciar uma tela mostrando as informações de conexão com o banco de dados:

Na aba Configurações, sub aba Oracle, realize o preenchimento do usuário e senha para acesso a base de dados, lembrando que este usuário deve ter permissão administrador na base de dados a ser utilizada.

Deve ser marcado os flags “ Identificar queries para monitoração “ e “ Usar BLOB para campos MEMO “ para o correto funcionamento do Topconnect em base Oracle.

Após salvar as configurações do usuário, acesse a aba Assistentes, validação de conexão. Este processo é executado para testar a comunicação entre o Topconnect e base de dados.

Na etapa 3, será solicitado o preenchimento do nome do ambiente a ser testado. Preencha o nome da instância Oracle criada para acessar a base de dados.     

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica);
