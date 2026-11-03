---
article_id: 360054191294
category: TAF - eSocial - Atualização
content_hash: 9ef8dcc2de51061266307d6daf52b28124acf855364e4c43114eaba73f76097a
fetched_at: '2026-06-28T22:45:13.353443+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Configurando e aplicando
  pacotes pelo VSCODE
type: support-article
updated_at: '2026-06-23T20:38:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054191294-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Configurando-e-aplicando-pacotes-pelo-VSCODE
---

**Dúvida**Como aplicar pacote de correção via **VSCODE**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial -Todas as versões

**Solução:**1 - Baixe o VSCode através do link:  
<https://code.visualstudio.com/download>

**Obs.:** Escolha o sistema operacional de acordo onde será feita a instalação e faça o download.

**Atenção:**

Caso seja utilizado TAF Segregado: é necessário parar o serviço TAF-WS antes de executar os passos seguintes. 

Caso seja utilizado TAF como módulo do Protheus: verifique se o *appserver.ini* possui algum job na seção ONSTART, se possuir, será necessário comentar essa linha conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12442653515543)

Se tiver a porta multiprotocolo ativa, acesse o appserver.ini e comente os parâmetros conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12443177197463)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12443180831383)

Se não tiver a seção [APP\_MONITOR] basta adicionar conforme abaixo:  
[APP\_MONITOR]  
Enable=0

2 - Para instalar o VSCode, basta seguir com as orientações de acordo com o seu sistema operacional;

3 - Acesse o diretório C: do servidor no qual o processo de instalação está sendo executado e crie uma nova pasta de nome *VSCode*:

4 - Com o **VSCode** instalado, localize a opção extension (extensões) na barra lateral:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10488389072279)

5 - Na barra de busca, digite *Totvs Developer Studio for VSCode* e em seguida clique em *Install* para que o plugin seja instalado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10488512648983)

6 - Clique no menu ***Arquivo*** ***> Abrir Pasta*** e selecione a pasta criada anteriormente no diretório C: do seu servidor:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12442730657687)

7 - Após a instalação do plugin, será aberto uma tela de boas vindas conforme abaixo:

OBS: Para clientes que já possuem o vsCode configurado anteriormente, pode desconsiderar do passo 7 ao 11  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091551454)

8 - Informe o caminho do seu SmartClient, selecionando caminho do executável do SmartClient.exe:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091551654)

9 - Clique em *SAVE/CLOSE*:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091551874)

10 - Clique no *Plugin* da **TOTVS** e clique em **Add Server [+]** para configurarmos o plugin para aplicar os pacotes do TAF:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091552094)

11 - Ao clicar em adicionar servidor *(add server)*, crie um nome para o servidor, no exemplo, **TAF**, endereço do local da instalação do **TAF**. Se estiver configurando direto no servidor onde está instalado o TAF, pode-se colocar **LOCALHOST** e a porta da sua seção **[TCP]** do arquivo **appserver.ini** localizado na pasta **bin/appserver.**  
  
Clique em **SAVE/CLOSE:**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091552334)

12 - Repare que aparecerá o nome da conexão que foi criado. Clique em **Connect**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093712933)

13 - Abre o APPSERVER.INI da pasta BIN/APPSERVER, e verifique o nome do ambiente e digite-o nome do ambiente configurado. No nosso exemplo temos configurado o ambiente **TAF,** porém podem variar os nomes de ambientes de acordo com a configuração:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10489110698391)  
  
14 - Verificado o ***enviroment*** (ambiente),  insira o usuário e senha de acesso ao **TAF**:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402817183127)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091552414)

15 - Ative os LOG's se caso ocorrer algum problema na conexão ou aplicação do pacote, será necessário para identificação de erros. No VSCode, clique em ***View* (Ver) > *Output* (Saída):**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10489206472727)

16 - Conectando o servidor com sucesso, pare o serviço do **TAF-WS** e clique com o botão direito do *mouse,* em cima do serviço conectado, em seguida, selecione a opção **Patch Apply (Aplicar Patch)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25675468794903)

Na janela que será aberta, selecione o arquivo da patch, pela opção **"Escolher arquivo" (Choose Files)**.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093713093)

17 - Para consultar o log da aplicação do pacote, na janela abaixo deixe selecionado em **"Output"** ou "Saída" e "TOTVS LS"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006141401)

18 - Primeiro será feito uma validação no pacote a ser aplicado e a mensagem que indicará o sucesso da validação será "A patch foi validada"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668727016471)

19 - Assim que for validado sem erros o pacote, basta clicar em **"Apply/Close"**. Será informado a mensagem " A patch foi aplicada com sucesso" ao finalizar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668727022231)

20 - Volte as configurações como o ONSTART e as configurações da porta multiprotocolo e ative o TAF-WS.
