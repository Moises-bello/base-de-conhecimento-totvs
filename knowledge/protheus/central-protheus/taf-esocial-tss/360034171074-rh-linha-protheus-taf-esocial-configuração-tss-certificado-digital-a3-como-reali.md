---
article_id: 360034171074
category: TAF - eSocial -TSS
content_hash: 4e33b504de70266e19e145aa58c137f983f79dd14e1d299499299e5863085aa9
fetched_at: '2026-06-28T22:45:21.941843+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - TSS - CERTIFICADO DIGITAL
  A3 - Como realizar a preparação do Certificado Digital e configurá-lo no TAF
type: support-article
updated_at: '2026-06-26T12:13:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034171074-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-TSS-CERTIFICADO-DIGITAL-A3-Como-realizar-a-prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-configur%C3%A1-lo-no-TAF
---

**Dúvida**Como realizar a preparação do Certificado Digital A3 no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração -TSS - Certificado A3 - Todas as versões  
  
**Solução**

**Atenção:**A instalação bem como a configuração do gerenciador do certificado no sistema operacional não é de responsabilidade da TOTVS, sendo necessário o prévio teste e validação de sua funcionalidade. Sugerimos que esta instalação e configuração seja realizada por um profissional com o conhecimento exigido pelo fabricante do Hardware.  
  
Se possível teste o acesso do Certificado Digital nos portais do eSocial ou eCAC.  
  
Para ambientes em *Cloud*, ou servidores virtualizados, não é possível a utilização do certificado A3. Dúvidas consulte nossa FAQ:  
[É possível configurar certificado A3, em ambiente Cloud e Servidores Virtuais?](https://tdn.totvs.com/pages/releaseview.action?pageId=329023719)

**Aviso:** Os passos a seguir são orientações necessárias que são exigidas para configurar o Certificado Digital A3 nos produtos TOTVS.

Sugerimos utilizar o software openSC para realização para os procedimentos à seguir. A instalação deste software deve ser na mesma máquina que o TSS está instalado:

1 - Após baixar o software openSC e instalar no seu SERVIDOR/MÁQUINA TSS, verifique o caminho que foi instalado o software;

2 - O sistema vai pedir o caminho absoluto da DLL. O caminho do repositório de DLL(s) é indicado pelo fabricante no momento da instalação do driver oficial. 

Uma dica para encontrar este arquivo é acessando o certificado pelo navegador FireFox, nele existe um módulo de acesso ao gerenciador físico e é possível verificar qual a DLL que ele utiliza.

Quando o certificado é importado no navegador Firefox é possível visualizar a DLL e o caminho usado pelo drive do fornecedor para gerenciamento do certificado, essa opção está disponível na opção ***“Dispositivos de Segurança”.***

***![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044247894)***

3 - Abra o *prompt* de comando e insira o código abaixo:  
  
**Exemplo:**  
C:\OpenSC\tools>pkcs11-tool.exe --module c:\windows\system32\etpkcs11.dll -l -O  
  
**Observação:** O caminho bem como a DLL de uso, será de acordo com o fornecedor do certificado;

4 - Durante o processo, irá solicitar a senha do Certificado;

5 - Assim que estiver tudo parametrizado, aperte *ENTER* e aparecerá as seguintes informações conforme exemplo abaixo:

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045172133)

6 - Nesse momento pare o serviço do TSS;

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044291414)

7 - Acesse o caminho da instalação onde está o TSS em seu servidor, e localize o arquivo appserver.ini.  
Geralmente os caminhos padrões é: "C:\totvs\TSS\BIN\appserver\appserver.ini" ou "C:\totvssped\BIN\appserver\appserver.ini" e abra o arquivo no bloco de notas ou algum outro editor de texto de sua preferência;

8 - Com o arquivo aberto, localize a sessão [SSLConfigure] e realize as seguintes alterações neste arquivo:   
  
[SSLConfigure]  
**HSM=1**  
Verbose=1  
SSL2=0  
SSL3=1  
TLS1\_0=1  
TLS1\_1=1  
TLS1\_2=1  
**MODULE = c:\windows\system32\etpkcs11.dll\***  
PassPhrase = senha\_do\_certificado  
**CertificateClient =slot\_0-label\_NOME\_DO\_CERTIFICADO\_DIGITAL:99999999999999\*\***  
**KeyClient=slot\_0-label\_NOME\_DO\_CERTIFICADO\_DIGITAL:99999999999999\*\***

**Importante:** O TSS é case sensitive, verifique se os diretórios estão em maiúculas ou minúsculas;

**\*MODULE = c:\windows\system32\etpkcs11.dll;** - (O Caminho da DDL de segurança [**Exemplo:** c:\windows\system32\etpkcs11.dll]);   
**\*\*CertificateClient =slot\_0-label\_NOME\_DO\_CERTIFICADO\_DIGITAL:99999999999999**  
**\*\*KeyClient=slot\_0-label\_NOME\_DO\_CERTIFICADO\_DIGITAL:99999999999999**  
ou  
**\*\*CertificateClient =slot\_0-id\_dados\_do\_id**  
**\*\*KeyClient=slot\_0-id\_dados\_do\_id**  
  
- Realizar a alteração no caractere do número referente ao SLOT se necessário, e informar os dados que foram apresentados na ferramenta openSC conforme ilustração abaixo:

SLOT:  
![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045174893)  
  
ID ou LABEL:![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045173873)

9 - Inicie os serviços do TSS;

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044292934)

10 - Assim que o TSS iniciar, verifique no arquivo console.log, localizado no mesmo diretório do appserver, se exibe o seguinte cenário:

![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044293794)

11 - **Atenção!** Quando for remover o certificado e repor ele novamente no servidor, o serviço do TSS deve ser reiniciado;

12 - Após preparação do Certificado Digital A3, vamos por fim configurá-lo no TAF.

13 - Clique em Atualizações e Wizard Config TSS;

14 - Em Rotina de Configuração do Ambiente TAF, clica em Avançar;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102709593)

4 - Verifique se o ambiente é Produção ou Homologação;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001695981)

5 - Selecione o tipo de Certificado(HSM) e preencha os campos SLOT, LABEL e a SENHA do Certificado e desça a tela;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001696001)

6 - Informe o caminho do módulo HSM ou o ID Hexadecimal

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001648242)

7 - Veja o nosso exemplo abaixo como deve ficar;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001648282)

8 - Clique em **Avançar** e veja se o mesmo foi configurado com sucesso e clique em **Finalizar**;

9 - Verifique no diretório de instalação do TSS e veja se foi criado a pasta HSM, conforme imagem;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102709733)

Se foi criado a pasta, o ambiente do TAF está preparado para realizar as transmissões das obrigações fiscais para o eSocial e/ou REINF.
