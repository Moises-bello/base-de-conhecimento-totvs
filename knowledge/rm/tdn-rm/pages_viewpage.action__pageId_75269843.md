---
content_hash: 354f463db9580e1dfee5c5d70dcbe73aff16ba6eb3058a3de76d2636c44df266
fetched_at: '2026-06-29T00:11:33.114674+00:00'
page_id: '75269843'
product: rm
source: tdn-rm
title: Integração do RM Reports X Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75269843
version: 47
---

# Índice

---

.\*ndice:

# Objetivo

---

       Este documento foi desenvolvido como guia para a integração do RM Reports x Protheus. O mesmo contempla os passos para a configuração do webservice RM, webservice Protheus e parametrização da comunicação entre ambos. Para seguir este manual faz-se necessário que os softwares RM e Protheus já estejam instalados e funcionando.

       Para o desenvolvimento do mesmo foram usados os seguintes softwares/versões:

* Protheus 11.8
* RM – Biblioteca 11.82.34

# Introdução

---

1. **Pré-Requisitos:**

* Instalação do **[Protheus](http://tdn.totvs.com/x/F4dzAQ)** na versão 11 ou superior e configuração do webservice do **[Protheus](http://tdn.totvs.com/x/F4dzAQ)**.
* Instalação da Biblioteca RM versão 11.80 ou superior. (Caso o cliente não utilize nenhum módulo da linha RM torna-se necessário uma base exemplo RM devidamente configurada).

# Preparar Banco de Dados

---

       Para o correto funcionamento da integração é necessário que sejam executados alguns passos no Banco de Dados.

Recomendável que esta preparação do banco de dados seja realizada por alguém com conhecimento em Banco de Dados, preferencialmente um DBA.

### Permissões na Base RM

falsePermissões na base RMPara Banco de Dados Microsoft SQL ServerPara Banco de Dados Microsoft SQL ServerPara Banco de Dados Microsoft SQL Server

Devem ser adicionados os seguintes Grants na base de dados RM:

sqltruePara Banco de Dados OraclePara Banco de Dados OraclePara Banco de Dados Oracle

Devem ser adicionados os seguintes Grants e Sinônimos na base de dados RM:

sqltrue

### Usuário no Banco de Dados

       É importante que exista um usuário igual em todas nas instâncias de banco de dados (RM e Protheus), ou seja, o mesmo nome de usuário e senha nas instâncias do RM e Protheus. É interessante também que estes usuários tenham permissão de SA ou DBA.

       É recomendável que este usuário seja utilizado na configuração da integração por parte do RM.

       No caso de bancos de dados MSSQL pode ser usado o usuário SA desde que o mesmo tenha as senhas iguais nas duas instâncias. Em caso de banco de dados Oracle, criar um usuário com prilégio DBA.

# Passos - Lado RM

---

**Importante:** Para que a integração funcione adequadamente é necessário que as fontes de dados RM e Protheus estejamdevidamente configuradas no servidor RM e Protheus. Ou seja, no caso de banco de dados SQL Server é necessário que o ODBC esteja apontando para os bancos de dados RM e Protheus, no caso de Oracle é necessário que o OracleClient esteja instalado no servidor e os serviços RM e Protheus configurados no mesmo.

### Arquivos de configuração

       1- Acesse o diretório da instação do RM, procure pela pasta RM.Net e busque todos os arquivos com extensão .config Obs.: Em uma instalação padrão do RM o caminho da pasta será: C:\totvs\CorporeRM\RM.Net.

        2- Abra os arquivos RM.Host.exe.config e RM.Host.Service.exe.config e adicione as linhas destacadas em vermelho no arquivo, para ficar com a mesma estrutura abaixo. Os campos em azul devem ser editados colocando suas respectivas informações:

falsePasso2Para Banco de Dados Microsoft SQL ServerPara Banco de Dados Microsoft SQL ServerPara Banco de Dados Microsoft SQL Server

Para banco de dados Microsoft SQL Server:

xmlExpanda para copiar o códigotrue





















]]>Para Banco de Dados OraclePara Banco de Dados OraclePara Banco de Dados Oracle

Para banco de dados Oracle:

xmlExpanda para copiar o códigotrue





















]]>

        3- Crie um arquivo com nome RM.Lib.Protheus.Server.dll.config dentro da pasta e copie o seguinte conteúdo dentro dele alterando as partes em azul com as respectivas informações:

falsexmlExpanda para copiar o códigotrue







http://:/wsdictionary/FWDICTIONARY.apw 
]]>

        4- Crie um arquivo com nome RM.Rpt.Protheus.Server.dll.config dentro da pasta e copie o seguinte conteúdo dentro dele alterando as partes em azul com as respectivas informações:

falsePasso4Para Banco de Dados SQL ServerPara Banco de Dados SQL ServerPara Banco de Dados SQL ServerxmlExpanda para copiar o códigotrue












http://
:
/wsdictionary/FWDICTIONARY.apw
]]>Para Banco de Dados OraclePara Banco de Dados OraclePara Banco de Dados OracleExpanda para copiar o códigotrue












http://
:
/FWDICTIONARY.apw
]]>

### Configurando o Serviço

       Após configurar todos os arquivos acima, faz-se necessária a configuração do serviço da RM.

       Por padrão o mesmo está configurado para “logar” como Network Service, porém é necessário que o mesmo esteja como LocalSystem. Para tal siga os passos abaixo:

1. Na pasta RM.Net busque o aplicativo RM.Host.exe
2. Execute o aplicativo como Administrador (clique como botão direto do mouse > Executar como Administrador
3. Será aberto um aplicativo minimizado na Aréa de Notificação, clique com o botão direito do mouse sobre ele > Configurar > Configurar Serviço

4. Na janela que se abriu, clique em Desinstalar:

5.  Em seguida selecione o usuário LocalSystem na lista de contas do sistema e clique em Instalar

6.  Se estiver tudo correto ficará como abaixo. Pode fechar a janela.

7. Teste o WebService acessando o endereço [http://127.0.0.1:8051/rptwebservicesserver/mex?wsdl](http://127.0.0.1:8051/rptwebservicesserver/mex)dentro do servidor. Caso tudo dê certo, deverá aparecer um schema XML no browser.

### Disponibilizar a fonte de dados no RM

       Após toda a configuração é necessário habilitar a fonte de dados Protheus para a geração de relatórios.

1. Acesse o RM e o ambiente Serviços Globais:
2. Dentro de Serviços Globais, acesse a pasta (aba) Ambientes, menu Parâmetros e opção Globais:
3. Na janela que se abriu, vá na pasta Gerador de Relatórios, busque o Provedor Protheus e clique duas vezes sobre ele:
4. Na nova janela marque o checkbox Ativo e clique em Ok e na janela anterior clique em Ok também:

# Passos - Lado Protheus

---

       Para a integração com o RM Reports não é necessário um Web Service específico, em testes realizados um Web Service convencional do Protheus foi o suficiente para suprir as necessidades do RM. Para fins deste material será demonstrado a criação do Web Service dedicado a integração.

É altamente recomendável criar um serviço exclusivo para “subir” o Web Service, isso evita perdas de desempenho na operação normal do sistema e em casos de manutenção ou parada no Web Service, não prejudica o restante da operação.

### Criando o WebService

1. Nos Parâmetros Iniciais do smartclient do Protheus, coloque as informações referentes a comunicação e ambiente do servidor que irá hospedar o webservice do RM e acesse o programa Server Wizard:
2. Dentro do Wizard, clique uma vez com cima de Módulos Web e em sequida clique na opção incluir na barra superior da janela:
3. Na janela que abriu preencha as informações conforme indicado abaixo e clique em Avançar:

* Módulo Web: WSR: Web Service Integração Totvs Reports
* Nome da Instância: Nome do WebService – O padrão adotado é WSR
* Diretório Raiz das Imagens: É o diretório onde o Web Service irá usar para armazenar imagens e outros arquivos – É recomendável deixar o padrão que é preenchido automaticamente
* Selecione o Enviroment: Ambiente do servidor onde irá “subir” o Web Service
* Habiliar processos na Inicialização do Servidor: Define se o job do Web Service irá iniciar junto com o serviço do appserver ou o mesmo deverá ser chamado manualmente – Altamente recomendável deixar marcado como habilitado.

4. No campo Host preencha com IP do servidor e porta do WebService (por padrão a porta adotada é 8090, porém pode ser mudada desde que seja atualizada no arquivo de configuração do RM), em seguida clique sobre a filial que irá ser amarrada a este endereço, clique em Relacionar e por fim Avançar:

5. Na tela seguinte preencha com 1 o campo Mínimo de Usuários e 999999 o campo Máximo de Usuários:

6. Na mensagem de confirmação que será exibida, confirme clicando em Sim.

7. Para finalizar a instalação reinicie o serviço do appserver onde o Web Service está instalado.

### Configurando a Comunicação

1. Acesse o configurador do Protheus
2. Dentro do configurador acesse o caminho Ambiente > Parâmetros:

3. Busque os parâmetros a seguir e preencha com as respectivas informações:

* MV\_RMWSPRT: Porta do Web Service RM (Padrão é 8051) – Neste campo preencha somente com o número, exemplo: 8051
* MV\_RMWSURL: Endereço do Web Service RM – Neste campo preencha somente com o IP ou nome do servidor RM, exemplo:192.168.0.21

### Chamar o Relatório RM no Protheus

       Esta etapa consiste em criar o atalho no menu do Protheus para chamar o relatório do RM.

1. Dentro do configurador abra o caminho Ambiente > Menus:

2. Desmaque o checkbox Todos os Menus, marque o checkbox do Menu desejado e clique em Ok:

3. Clique uma vez em cima do nome do menu escolhido e em seguida Adicionar:

4. Navegue na janela do lado direito até encontrar a pasta desejada para alocar o relatório, em seguida dê um clique simples no nome desta pasta e clique em Novo Item:

5. Preencha os campos Descrição, em seguida Módulo (módulo onde será executado o relatório), Tipo (Totvs Report) e por último clique no botão ... na opção Programa:

6. Na janela que se abriu marque o checkbox com o relatório desejado, clique em Confirmar e na janela anterior clique em Ok:

7. Terminada a inclusão dos relatórios, salve as alterações do menu clicando em Gerar na tela anteior, preenchendo com o nome do menu e em seguida Gerar novamente:

Obs.: As nomenclaturas padrões (“original” da Totvs e sem customização) de menus dos principais módulos do Protheus são:

* Ativo Fixo - SIGAATF
* Compras – SIGACOM
* Contabilidade – SIGACTB
* Estoque - SIGAEST
* Faturamento – SIGAFAT
* Financeiro – SIGAFIN

# Gerar Relatório no Protheus

---

### Tela Principal

       Após “chamar” o relatório desejado será exibida a tela a seguir:

       O grupo Tipo corresponde ao formato de arquivo que será gerado.

       O Local corresponde ao local onde o arquivo gerado será salvo.

### Filtros

Clique sobre o grupo Filtro, preencha o filtro desejado e clique em Ok

Exemplo da composição de um filtro:

Desejado:

* Todos os Pedidos de Compra entre 01/01/2014 e 01/05/2014
* Fornecedor 000002 e 000040

Estrutura do filtro:

(DT Emissão Maior ou Igual a 01/01/2014 e DT Emissão Menor ou Igual a 01/05/2014) e (Fornecedor Igual a 000002 ou Fornecedor Igual a 000040)

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

falsefalse

**Produto:** Framework

false

**Versão:** 11.80.XX

false

**Processo:** Totvs Reports

false

**Subprocesso:** Integração RM Reports X Protheus

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

**Douglas Maxwell de Oliveira**
