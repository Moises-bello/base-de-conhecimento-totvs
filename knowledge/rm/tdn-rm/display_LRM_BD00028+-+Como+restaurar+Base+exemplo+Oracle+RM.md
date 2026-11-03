---
content_hash: dfb35862254440dedc73fccbef74346119f8998abd1ab4acf406705e284af52a
fetched_at: '2026-06-29T00:10:26.693488+00:00'
page_id: '514438251'
product: rm
source: tdn-rm
title: BD00028 - Como restaurar Base exemplo Oracle RM
type: documentation
url: https://tdn.totvs.com/display/LRM/BD00028+-+Como+restaurar+Base+exemplo+Oracle+RM
version: 5
---

# 

# Objetivo

Demonstrar os procedimentos para restauração de Base de Dados CorporeRM Oracle.;.

* O Oracle Server é utilizado para realizar a restauração da Base de Dados Oracle, sendo indispensável para este procedimento;
* O procedimento abaixo considera a Base de Dados exemplo (disponibilizada no portal do cliente), porém o processo de restauração pode ser utilizado para outros arquivos *dumps* (dmp) como a Base de Dados Vazia ou um backup da produção;
* O exemplo abaixo corresponde a backup da versão 12.1.19, porém esse mesmo procedimento pode ser utilizado para as versões subsequentes;

* **As mudanças de releases do CorporeRM podem caracterizar a necessidade alteração no scripts acesso.sql, tbspace.sql e usuarios.sql. Sendo assim, sempre utilize os scripts atualizados que são juntamente com o instalar da Base de Dados Oracle ou acesse o link de Acerta Usuário: <https://tdn.totvs.com/pages/releaseview.action?pageId=270904221>**

.

00Passo a Passo111ª Passo

* Crie uma pasta dentro do "**C:**" com a seguinte nomenclatura RMxx

Onde se lê xx refere-se a versão do RM, exemplo: **RM19** (Refere-se a versão 12.1.19 do RM);

* **No Portal do Cliente são disponibilizados para download as Bases de Dados Vazias/Exemplo Oracle. Após o download e instalação os arquivos correspondente estarão disponíveis no diretório TOTVS\CorporeRM\BaseDados\Oracle.**

* Copie os arquivos **tbspace**.sql, **usuarios**.sql, **acesso**.sql e **Exemplo12119**.zip.

Caso esteja fazendo restauração de uma base RM vazia, copie o arquivo BASEVAZIA12119 ao invés de EXEMPLO12119.

* Cole os arquivos dentro da pasta criada no diretório(C:\**RM19**) criado.

22ª Passo

* Dentro do diretório (C:\**RM19**) crie uma pasta chamada "**tbspace\_arq**', esta pasta irá conter alguns arquivos necessários para restauração da base de dados Oracle.

Para saber mais sobre tablespaces veja este link: [Tablespaces](https://www.devmedia.com.br/administracao-oracle-com-tablespaces-datafiles-e-gerenciamento-de-usuarios-e-privilegios/32271)

* No menu iniciar procure por "**Assistente de configuração de banco de dados**"

* Ao apresentar está tela clique em "**Próximo**".

* Ao apresentar a tela de operações, selecione a opção "**Criar um banco de dados Oracle**" | Próximo.

* Deixe a opção "**Finalidade geral ou processamento de transação**" marcada e clique em Próximo.

33ª Passo

* Na Identificação do banco de dados, informe o nome da base de dados desejada. No exemplo abaixo o nome da base de dados será **RM19**em seguida clique em **Próximo**.

* Na aba "Enterprise Manager" desmarque a opção "**Configurar o Enterprise Manager**".

* Na aba "Tarefas de manutenção automática" desmarque a opção "**Ativar tarefas de manutenção automática**" e clique em **Próximo**.  
  + Na tela de Credenciais do Banco de dados, marque a opção "**Usar a mesma senha Administrativa para todas contas**":
    - Senha: **rm**
    - Confirma senha: **rm**
  + Ao clicar em próximo será apresentado uma tela referente a politica de privacidade de complexidade de senhas, somente confirme apertando em "**SIM**".
44ª Passo

* Próximo;

* Desmarque a opção "**Especifique a Área de recuperação flash**" e clique em próximo;

* Próximo;

* Na aba Memória, deixe marcado a opção "**Típico" e no campo Tamanho da Memória (SGA e PGA)"** informe o valor "**300**" que se refere a **10%**;
* Na aba Dimensionamento, o campo Processos informe o valor "**300**".
55ª Passo

* Ainda na tela de Parâmetros de Inicialização, na aba Conjuntos de caracteres, marque a opção "**Escolha na lista de conjuntos de caracteres**" e desmarque a opção "**Mostrar apenas conjuntos de caracteres recomendados**";
  + No campo "**Conjunto de Caracteres de banco de dados**' informe a opção "**WE8ISO8859P1 - ISO 8859-1 Europa Ocidental**".
* Na mesma tela, o campo Conjunto de Caracteres Nacionais, informe o a opção "**AL16UTF16 - Conjunto de caracteres Unicode UTF-16 Universa**l";
* Idioma Default: **Inglês**;
* Território Default: **Estados Unidos.**

* **Próximo.**
66ª Passo

* Na tela de "**Armazenamento do banco de dados**" clique em "**Próximo**";

* Na tela de "**Opção de Criação**"  clique em "**Finalizar**".

* Será apresentado uma tela para confirmação, somente clique em "**OK**".

* Após clicar em OK, será apresentado a tela de inicialização da criação do Banco de dados Oracle.

* Ao finalizar a criação clique em "**Sair**" .

77ª Passo

* + Clique no atalho do teclado **Windows + R** e digite "**services.msc**" e clique em "**OK"** ou vá no menu Iniciar e pesquise por "**Serviços**".

* Ao abrir o services.msc procure por "**OracleServiceRM19**" e inicie o serviço da base Oracle.
* Certifique-se que os serviços do Oracle estão ativos também "**OracleOraDb11g\_Home1ClrAgent**" e "**OracleOraDb11g\_Home1TNSListener**"

88ª Passo

* Abra o SQLPlus ou qualquer programa para conectar com a base de dados Oracle.

Preencha os seguintes campos no SQLPlus:

User: **sys**

Password: **rm**

Marque a opção "**Bypass tnsnames.ora"**

Host: informe seu **servidor**

TCP Port: por padrão e a porta **1521**

SID: **nome da base de dados Oracle** (no nosso caso e **RM19**)

Marque "**Use Service Instead of SID**"

Mode: **SYSDBA**

Safety: **None (Development)**

* Clique em**"OK".**

99ª Passo

* Ao conectar com a base de dados Oracle criada (**RM19**), é necessário rodar o script "**tbspace**" dentro da pasta **RM19** criada no**C:**
* Altere o diretório do Datafile para a pasta que criamos nos primeiros passos**"tbspace\_arq".**

1010ª Passo

* Vamos agora rodar o script de **usuário** que esta dentro do diretório C:\RM19 que criamos.

1111ª Passo

* Vamos agora rodar o comando "**grant**" que é basicamente utilizado para criar um **alias ou instância** para ser utilizado no comando de restauração da base de dados.

Onde se lê "**X**" e "**Y**" informar o nome da base de dados oracle **RM19;**

**O caminho do arquivo .dmp,**iremos extrair o arquivo**EXEMPLO12119.zip**dentro do diretório**"C:\RM19"**criado, em seguida renomeie o arquivo extraio para **RM19** (nome da base de dados).

CREATE OR REPLACE DIRECTORY **X** AS '**Caminho do arquivo .dmp**';

GRANT READ, WRITE ON DIRECTORY **Y** TO rm;

\*\*\*\*\*\*\* Como fica o comando \*\*\*\*\*\*\*

CREATE OR REPLACE DIRECTORY RM19 AS 'C:\RM19';  
GRANT READ, WRITE ON DIRECTORY RM19 TO rm;

1212ª Passo

* Agora vamos realizar a restauração da base de dados Oracle.

1. Crie um arquivo texto com o seguinte comando:  
     
   impdp system/rm@**NomeDaBaseDeDadosOracle** schemas=RM Version=10.2 directory=**NomeDaBaseOracle** dumpfile=**NomeDoArquivoDmpInformaNoDiretorioCriado**.dmp logfile=**NomeDaBaseDeDadosOracle**.log
2. Salve o arquivo dentro do diretório **C:** com o nome de "**impdp"**e a extensão deste arquivo será**".bat";**
3. Abra o "**Prompt de comando"** e digite o seguinte comando "**cd\"**
4. Após digite**impdp.bat**e tecle enter, assim irá começar a restauração da base de dados Oracle em sua maquina.
5. Após digitar o comando será necessário aguardar que o processo termine o prompt de comando irá fechar automaticamente ao final do processo.  
   Arquivo **impdp** para download abaixo:

250

1313ª Passo

* Ao finalizar o processo de restauração da base de dados o **Prompt de comando** será fechado automaticamente, assim deve-se rodar o ultimo script o de "**acesso.sq**l" que está dentro do diretório criado no **C:\RM19**.

* Ao terminar de executar o script de **acesso**, atualize os scripts da base de dados no**RM no atualizador** e seja feliz .
1Dicas Oracle101 - Como achar o arquivo TNSNAMES.ORA

**Dúvida**

Como localizar o arquivo TNSNAMES.ORA?

**Solução**

Para localizar o arquivo de configuração TNSNAMES.ORA, realize os passos a seguir:

1. Clique em INICIAR/EXECUTAR do windows;

2. Digite CMD e clique em OK;

3. Na tela de comandos, digite o comando TNSPING NOME\_DA\_BASE, conforme imagem:

4. Será exibido a mensagem conforme a imagem abaixo, o caminho está indicado pela seta:

5. Copie esse caminho até no Executar do Windows e clique em OK:

**Importante:**Note que somente o caminho foi copiado, não o sqlnet.ora. Outra informação importante é que o caminho pode variar de uma máquina para outra.

6. Os arquivos serão listados nessa pasta, conforme imagem abaixo:

**Observação:** Este arquivo é responsável pela configuração da forma de comunicação entre client oracle e banco de dados.

02 - Erro: O provedor 'OraOLEDB.Oracle' não está registrado na máquina local

**Dúvida**

Erro ao tentar conectar ao RM ou outro programa: O provedor 'OraOLEDB.Oracle' não está registrado na máquina local.

**Solução**

Acesse o diretório do Oracle via CMD como administrador;

Obs.: O arquivo que iremos registrar está dentro da pasta **bin.**Provavelmente o arquivo estará no diretório acima, caso não, pesquise dentro da pasta C:\Oracle\_64 o arquivo "OraOLEDB11.dll" (Caso o Oracle instalado seja o oracle 10g o nome do arquivo será "OraOLEDB10.dll").

* Após acessar a pasta execute o comando no CMD:

regsvr32 OraOLEDB11.dll

\*\*\*\* Pronto agora irá conseguir acessar bases de dados Oracle.

OBS.: Verifique se o RM.exe está executando em 32 bits ou 64 bits, caso esteja executando como 64 bits execute o comando abaixo no CMD como administrador.

* Acesse a pasta do RM utilizando o comando CD;
* Execute o comando "corflags rm.host.exe /32bit+";
* Fim .
