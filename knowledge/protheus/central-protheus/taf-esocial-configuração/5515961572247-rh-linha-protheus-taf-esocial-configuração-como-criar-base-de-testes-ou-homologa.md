---
article_id: 5515961572247
category: TAF - eSocial - Configuração
content_hash: c3c788835d1c01716744f27a842a18a6e13e3e09838651dc19ef67cee2e8533f
fetched_at: '2026-06-28T22:45:14.478966+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como criar base de testes
  ou homologação para o TAF
type: support-article
updated_at: '2024-05-29T17:06:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5515961572247-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-criar-base-de-testes-ou-homologa%C3%A7%C3%A3o-para-o-TAF
---

**Dúvida**Como criar base de testes ou homologação para o TAF  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**

1 - No servidor onde está instalado o TAF e o TSS, copie as pastas TAF e TOTVSSPED ou TSS, pode compactar os arquivos enviar para o novo servidor;

2 - Atente-se para deixar os arquivos na mesma estrutura.  
Exemplo: C:\TOTVS\TAF; C:\TOTVSSPED;

*(Cada ambiente deve possuir alguma estrutura diferente do que for exibido ou mostrado neste material porém o processo é o mesmo).*

**Configurando Banco de dados:**

Criar novo banco de dados de testes do TAF e caso queira recuperar os dados da base existente pode executar a tarefa. Se caso criar a base de testes com intuito de enviar os dados para o governo na base de homologação o recomendável é criar a base de dados sem ter informação;

3 - SQL SERVER: Acesse a documentação abaixo para configuração de conexão com o banco de dados SQL SERVER:  
[TAF - CONFIGURAÇÃO - Criando conexões via ODBC em 64 bits (Obrigatório)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)

4 - ORACLE: Acesse a documentação abaixo para configuração de conexão com o banco de dados ORACLE:  
[TAF - CONFIGURAÇÃO - Criando conexão com banco Oracle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814)

**Configurando o DBAccess:**  
5 - Verifique qual caminho o **TAFDBAccess** está alocado:  
**Exemplo:** *C:\TOTVS\TAF\TafDbAccess64*

6 - Localize o arquivo de configuração dbaccess.ini e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

*[SERVICE]*  
*NAME=Taf-DbAccess64-Homolog*  
*DISPLAYNAME=Taf-DbAccess64-Homolog*

7 - Procure pelo arquivo executável dbaccess.exe e crie um atalho para este aplicativo;

8 - Com o atalho criado, clique com o botão direto do mouse e acesse as propriedades do arquivo;

9 - No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:

**Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516382090263)**

10 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

11 - Para validar a conexão com o banco de dados acesse o artigo abaixo:  
[TAF - CONFIGURAÇÃO - Criando e/ou testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)

**Configurando o APPSERVER do TAF:**  
12 - Localize a pasta appserver que está dentro do diretório bin;

Exemplo: C:\TOTVS\TAF\bin\appserver

13 - Localize o arquivo de configuração appserver.ini e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

*[SERVICE]*  
*NAME=TAF-APPSERVER-HOMOLOG*  
*DISPLAYNAME=TAF-APPSERVER-HOMOLOG*

**Obs.:** Se estiver mudando para outra unidade de disco por exemplo do C:/ para a unidade D:/ por exemplo, altere os parâmetros abaixo:

*[TAF]*  
*SourcePath=D:\totvs\TAF\apo*  
*RootPath=D:\totvs\TAF*

*[General]*  
*InstallPath=D:\totvs\TAF*  
*ConsoleFile=D:\totvs\TAF\bin\appserver\console.log*

*[HTTP]*  
*Path=D:\totvs\TAF\http-root*

*[UPDATE]*  
*PathWindows=D:\totvs\TAF\bin\smartclient\_update*

Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

14 - Procure o arquivo executável appserver.exe e crie um atalho;

15 - Com o atalho criado, clique com o botão direto do mouse e acesse as propriedades do arquivo;

16 - No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516410589975)

17 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**Configurando o TAF-WS (REST):**

18 - Localize a pasta app que está dentro do diretório bin.  
Exemplo: C:\TOTVS\TAF\bin\app

19 - Localize o arquivo de configuração appserver.ini e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

*[SERVICE]*  
*NAME=TAF-WS-HOMOLOG*  
*DISPLAYNAME=TAF-WS-HOMOLOG*

Caso esteja alocando em outro unidade de disco, basta informar no arquivo à nova unidade no arquivo de configuração appserver.ini.

Obs.: Se estiver mudando para outra unidade de disco por exemplo do C:/ para a unidade D:/ por exemplo, altere os parâmetros abaixo:

*[TAF]*  
*SourcePath=D:\totvs\TAF\apo*  
*RootPath=D:\totvs\TAF*

*[General]*  
*InstallPath=D:\totvs\TAF*

Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

20 - Procure o arquivo executável appserver.exe e crie um atalho;

21 - Com o atalho criado, clique com o botão direto do mouse e acesse as propriedades do arquivo;

22 - No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516398284951)

23 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**(Opcional) Configurando o TSS:**  
*Criar serviço TSS, porém pode-se utilizar o TSS criado em produção.*   
*O XML enviado conterá informações da base de homologação caso transmitir os eventos para o governo.*  
*Caso deseja criar o serviço TSS bastar continuar os procedimentos abaixo:*

24 - Verifique qual diretório de instalação do TSS;

25 - Localize a pasta appserver que está dentro do diretório bin.  
Exemplo: C:\totvssped\bin\appserver

26 - Localize o arquivo de configuração appserver.ini e insira a informação abaixo, caso não exista no arquivo que tenha realizado o backup:

*[Service]*  
*Name=TSS-APPSERVER-HOMOLOG*  
*DisplayName=TSS-APPSERVER-HOMOLOG*

Obs.: Se estiver mudando para outra unidade de disco por exemplo do C:/ para a unidade D:/ por exemplo, altere os parâmetros abaixo:

*[SPED]*  
*SourcePath=D:\totvs\TSS\apo*  
*RootPath=D:\totvs\TSS*

*[General]*  
*INSTALLPATH=D:\totvs\TSS*

*[HTTP]*  
*PATH=D:\totvs\TSS\HTML*

*[UPDATE]*  
*PathWindows=D:\totvs\TAF\bin\smartclient\_update*

*[localhost:XXXX/tssonline]*  
*PATH=D:\totvs\TSS\Html*

*[localhost:XXXX]*  
*PATH=D:\totvs\TSS\web\ws*

Verifique qual unidade de disco está alocando e realize as alterações conforme as unidades de disco;

27 - Procure o arquivo executável appserver.exe e crie um atalho;

28 - Com o atalho criado, clique com o botão direto do mouse e acesse as propriedades do arquivo;

29 - No campo DESTINO onde é informado o endereço do aplicativo local, acrescente a palavra "-install" no final do endereço:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516407183639)

30 - Dê um duplo clique e automaticamente será criado o novo serviço no servidor;

**Acessando o TAF e realizando a configuração do CERTIFICADO DIGITAL:**  
31 - Acesse o TAF;

32 - Clique em Atualizações > Wizard Config TSS;

33 - Em Rotina de Configuração do Ambiente TAF, clica em Avançar;

34 - Verifique se o parâmetro está marcado conforme abaixo: 2 - Pré-Produção - Dados Reais:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516446925335)

35 - Selecione o tipo de Certificado(.pem, .pfx, .p12, etc...) Lembrando que o Smart eSocial não aceita certificado do tipo A3 e os arquivo tem que ser maior ou igual a 7kb. Clique no botão ... para a selecionar o Certificado Digital:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516480723095)

36 - Repare que ao acessar o certificado digital na sua máquina, no canto superior direito existe um link escrito Arquivos locais: clique aqui:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516487349399)

Selecione o certificado e clica em Salvar;

37 - Digite a senha do certificado digital:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516499602327)

38 - Caso o certificado possua outorga, antes de avançar, informe o CNPJ diferente do empregador, caso não possua outorga, pode deixar o campo em branco e clique em Avançar:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516519548567)

39 - Se o Certificado Digital não tiver algum problema, ele irá informar que foi configurado com sucesso e clica em Finalizar;

40 - Acesse os parâmetros do TAF:  
[Automação Fiscal - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

41 - Procure pelo parâmetro MV\_TAFAMBE e verifique se está com valor 2, se não estiver, coloque-o para 2. Valor 2 indica que o ambiente configurado é Pré-Produção - Dados Reais:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516509102487)

42 - Após configurar e verificar que o sistema está funcional, verifique as portas conforme material abaixo:

[Automação Fiscal - Configuração - Como verificar as portas utilizadas no TAF e TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5517111619991)
