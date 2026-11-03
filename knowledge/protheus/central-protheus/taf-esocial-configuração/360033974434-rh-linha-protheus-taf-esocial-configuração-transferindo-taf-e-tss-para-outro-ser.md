---
article_id: 360033974434
category: TAF - eSocial - Configuração
content_hash: e8677323bb6c4377798a71be776b711a0d7e333ba5482238ec649fccd722054c
fetched_at: '2026-06-28T22:45:14.411493+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Transferindo TAF e TSS
  para outro Servidor
type: support-article
updated_at: '2026-06-23T18:21:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033974434-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Transferindo-TAF-e-TSS-para-outro-Servidor
---

**Dúvida**Como realizar a migração do TAF e TSS para outro Servidor?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial -Todas as versões  
  
**Solução**1 - No servidor onde está instalado o TAF e o TSS,  copie as pastas TAF e TOTVSSPED ou TSS, pode compactar os arquivos enviar para o novo servidor.

2 - Atente-se para deixar os arquivos na mesma estrutura.   
**Exemplo:** C:\TOTVS\TAF; C:\TOTVSSPED;  
(Depende de cada estrutura que realizaram a instalação)

**Obs.:**Se estiver migrando o TAF e o TSS para outra unidade de disco, coloque o TAF e o TSS na nova unidade e modifique os arquivos de configurações para a unidade de disco atual.

**Configurando o****DBAccess:**3 - Verifique qual caminho o TAFDBAccess está alocado:   
**Exemplo:**  
C:\TOTVS\TAF\TafDbAccess64

4 - Localize o arquivo de configuração **dbaccess.ini**e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

**[SERVICE]**

**NAME=Taf-DbAccess64**  
**DISPLAYNAME=Taf-DbAccess64**  
  
5 - Procure pelo arquivo executável **dbaccess.exe**e crie um atalho para este aplicativo.

6 - Com o atalho criado, clique com o botão direto do mouse e acesse as **propriedades** do arquivo;

7 - No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:  
 **Exemplo:**   
![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044835113)

8 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**Configurando o TAF-WS:**9 -  Localize a pasta app que está dentro do diretório bin.  
**Exemplo:**   
C:\TOTVS\TAF\bin\app

10 - Localize o arquivo de configuração **appserver.ini**e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

**[SERVICE]**  
**NAME=TAF-WS**  
**DISPLAYNAME=TAF-WS**

Caso esteja alocando em outro unidade de disco, basta informar no arquivo à nova unidade no arquivo de configuração **appserver.ini.**  
  
**Obs.:**  
Se estiver mudando para a unidade **D:/** por exemplo, altere os parâmetros abaixo:  
  
[TAF]  
SourcePath=D:\totvs\TAF\apo  
RootPath=D:\totvs\TAF  
  
[General]  
InstallPath=D:\totvs\TAF  
  
Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

11 - Procure o arquivo executável **appserver.exe**e crie um atalho;  
  
  
12 - Com o atalho criado, clique com o botão direto do mouse e acesse as **propriedades** do arquivo;  
  
  
13 -  No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:  
  
**Exemplo:**![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044836833)  
  
14 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;  
  
  
**Configurando o APPSERVER do TAF**15 -  Localize a pasta appserver que está dentro do diretório bin.  
**Exemplo:**   
C:\TOTVS\TAF\bin\appserver

16 - Localize o arquivo de configuração **appserver.ini**e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

**[SERVICE]**  
**NAME=TAF-APPSERVER**  
**DISPLAYNAME=TAF-APPSERVER**

**Obs.:**  
Se estiver mudando para a unidade **D:/** por exemplo, altere os parâmetros abaixo:  
  
[TAF]  
SourcePath=D:\totvs\TAF\apo  
RootPath=D:\totvs\TAF  
  
[General]  
InstallPath=D:\totvs\TAF  
ConsoleFile=D:\totvs\TAF\bin\appserver\console.log

[HTTP]  
Path=D:\totvs\TAF\http-root

[UPDATE]  
PathWindows=D:\totvs\TAF\bin\smartclient\_update

Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

17 - Procure o arquivo executável **appserver.exe**e crie um atalho;  
  
  
18 - Com o atalho criado, clique com o botão direto do mouse e acesse as **propriedades** do arquivo;  
  
  
19 -  No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:  
  
**Exemplo:**![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044837033)  
  
20 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**Configurando o TSS:**21 - Verifique qual diretório de instalação do TSS;

22 - Localize a pasta appserver que está dentro do diretório bin.  
**Exemplo:**   
C:\totvssped\bin\appserver

23 - Localize o arquivo de configuração **appserver.ini**e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

**[Service]**  
**Name=TSS-APPSERVER**  
**DisplayName=TSS-APPSERVER**

**Obs.:**  
Se estiver mudando para a unidade **D:/** por exemplo, altere os parâmetros abaixo:  
  
[SPED]  
SourcePath=D:\totvs\TSS\apo  
RootPath=D:\totvs\TSS  
  
[General]  
INSTALLPATH=D:\totvs\TSS

[HTTP]  
PATH=D:\totvs\TSS\HTML

[UPDATE]  
PathWindows=D:\totvs\TAF\bin\smartclient\_update  
  
[localhost:5478/tssonline]  
PATH=D:\totvs\TSS\Html  
  
[localhost:5478]  
PATH=D:\totvs\TSS\web\ws

Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

24 - Procure o arquivo executável **appserver.exe**e crie um atalho;  
  
  
25 - Com o atalho criado, clique com o botão direto do mouse e acesse as **propriedades** do arquivo;  
  
  
26 -  No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:  
  
**Exemplo:**![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043974294)  
  
27 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**Configurando Banco de dados**28 - **SQL SERVER:**Acesse a documentação abaixo para configuração de conexão com o banco de dados SQL SERVER:  
[Criando Conexão via ODBC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)  
  
29 - **ORACLE:**Acesse a documentação abaixo para configuração de conexão com o banco de dados ORACLE:  
[Criando conexões com o banco de dados ORACLE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814)  
  
30 - Para validar a conexão com o banco de dados acesse o artigo abaixo:  
[Criando e testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)

31 - Ao criar o ambiente em seu novo servidor, acesse o configurador do TAF (SIGACFG):  
[TAF - CONFIGURADOR - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)

32 - Acesse os parâmetros do TAF:  
[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

33 - Pesquise o parâmetro **MV\_TAFREST** (Este parâmetro é responsável para integração entre RM e TAF) e edite-o colocando o IP e a porta do servidor da sua ***Web Service***:  
  
**Exemplo:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056955174)

34 - Em seguida, realize a alteração do parâmetro MV\_TAFSURL (Este parâmetro é responsável para comunicação entre TAF e TSS) e edite-o colocando o IP e a porta da configuração do TSS:

Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057829893)

35 - Se o TSS não comunicar com o TAF, realize novamente a configuração do Certificado Digital, conforme documentação abaixo:  
[Automação Fiscal - Configuração - Como configurar o Certificado Digital no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001814402-Automa%C3%A7%C3%A3o-Fiscal-Configura%C3%A7%C3%A3o-Como-configurar-o-Certificado-Digital-no-TAF)

36 - Verifique se no novo servidor não há bloqueios de porta ou configurações de firewall.
