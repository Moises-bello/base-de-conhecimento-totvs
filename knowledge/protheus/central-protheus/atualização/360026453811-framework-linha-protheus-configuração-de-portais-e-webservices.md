---
article_id: 360026453811
category: Atualização
content_hash: 7b22063d6784dcccdf5aa3553ab27a0e9f086f981d700d715def96cd450a0bfc
fetched_at: '2026-06-28T22:42:21.225661+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Configuração de Portais e WebServices
type: support-article
updated_at: '2024-07-08T19:41:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026453811-Framework-Linha-Protheus-Configura%C3%A7%C3%A3o-de-Portais-e-WebServices
---

**Dúvida**Como configurar um portal ou webservice no Protheus?  
   
 **Ambiente**Protheus - AppServer - A partir da versão 11  
  
**Solução**O Portal Protheus disponibiliza serviços na Web para agilizar e facilitar o compartilhamento de informações entre seus clientes, fornecedores, parceiros, usuários internos e externos; toda a comunicação entre os servidores Web e os servidores Corporativos é efetuada através de Web Services.  
  
Para habilitar os **WebServices** é necessário que o Serviço **HTTP** esteja ativo. Este serviço permite que as informações sejam publicadas na **WEB**.  
Assim, a configuração inicia-se habilitando o serviço HTTP e configurando a porta aos quais todos os outros serviços dependentes deste irão utilizar para a publicação das informações.  
  
Observação: Os serviços devem ser configurados pelo WIZARD (**SRVWIZARD**), pois a cada módulo WEB instalado são descompactados arquivos importantes no diretório informado na configuração. Estes arquivos são de extensão exclusiva da Microsiga, os **\*.MZP**, e que apenas com o Wizard será possível a correta instalação.  
  
Aviso: Alteração de comportamento, efetiva a partir da **LIB Label 20170208**, com o font **XmlWsCvs.prw** de data igual ou superior a 29/03/2017, nas versões 11 e 12 do Protheus.  
Para atender a orientação de mercado, os serviços SOAP do Protheus não retornam mais o stack completo de error.log.  
Ao ocorrer um erro no sistema, é gerado um **SoapFault 500**, somente com a mensagem **Internal Server Error**. O envio do error.log pelo canal HTTP não será mais realizado.  
O erro ainda poderá ser verificado no sistema através dos arquivos de log do appserver.exe.  
Fonte: <http://tdn.totvs.com/pages/viewpage.action?pageId=311632028>  
  
Para configurar, siga o procedimento abaixo:  
1. Primeiramente, baixe os **Arquivos de Portais** no Portal do Cliente, e descompacte na pasta Systemload  
- Acesse o Portal do Cliente: [http://suporte.totvs.com](http://suporte.totvs.com/)  
- Clique em **Downloads**  
- Na opção Outras Linhas de Produto selecione **Protheus**  
- MICROSIGA PROTHEUS VERSÃO 12.1.XX (onde XX é a versão da sua release)  
- WEB FILES  
- Baixe o arquivo ARQUIVOS DE PORTAIS  
Obs.: se não estiverem aparecendo as versões, em **Filtros de pacotes** selecione **Todos pacotes disponíveis**  
  
2. Após baixar e descompactar o arquivo, abra o **Smartclient**, e no **Programa Inicial**, digite **SRVWIZARD  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025642631)**3. Clique 2 vezes em **Servidor Internet** (HTTP/FTP) para expandir, clique em **HTTP**, e verifique se a caixinha **Protocolo Habilitado** está marcada, e confirme a **Porta de Conexão** (recomendamos que seja diferente de 80, que é a porta padrão do HTTP, e é utilizada por serviços do Windows)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025643231)  
  
4. Após a confirmação, clique em **Módulos Web** e então clique em **Novo Módulo**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025627872)  
  
5. Em **Módulo Web**, selecione **WS - Microsiga Protheus Web Services**  
6.  Em **Nome da Instância** digite **ws**  
7. O **Diretório Raiz das imagens** será preenchido automaticamente  
  
8. Em **Selecione o Environment**, clique e selecione o ambiente do Protheus que será utilizado  
  
9. Marque a caixinha **Habilitar processos na Inicialização do Servidor**, e clique em **Avançar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025643651)**10. Na tela **Configuração de Hosts X Empresas/Filiais**, em **Hosts**, digite o endereço, porta e pasta da instância do Webservice, conforme exemplo: localhost:8079/ws (não digite o "http"). Caso o servidor não seja local, digite o IP do servidor.  
  
11. Em **Selecione a Empresa/Filial**, selecione a Empresa que estará vinculada a este Webservice, então clique em **Relacionar**. A ligação entre o Host e a Empresa será listada em **Relacionamentos**  
12. Clique em **Avançar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025628112)**13. Na tela **Configuração de usuários**, em **Mínimo Usuários** e **Máximo Usuários**, que é a quantidade de threads que será aberta em execução (Mínimo) e a quantidade de threads que será aberta em espera (Máximo), digite as quantidades desejadas e clique em **Finalizar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025644311)  
  
14. Será exibida uma janela de confirmação da criação do Módulo Web. Clique em **Sim**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025628572)  
  
15. Ao final será exibido um aviso solicitando a reinicialização do Protheus para que a configuração entre em vigor. Clique em **Fechar**16. Após configurar o **Webservice**, é necessário configurar o **Portal**. Clique novamente em **Módulos Web** e clique em **Novo Módulo**17. Em **Módulo Web** selecione **PP - Portal Protheus**  
18.  Em **Nome da Instância** digite **pp**  
19. O **Diretório Raiz das imagens** será preenchido automaticamente  
  
20. Em **Selecione o Environment**, clique e selecione o ambiente do Protheus que será utilizado  
  
21. Marque a caixinha **Habilitar processos na Inicialização do Servidor**  
22. Em **URL do Protheus Web Services**, preencha o endereço que foi criado na etapa anterior para o Webservice. No nosso exemplo: <http://localhost:8079/ws>  
  
23. Clique em **Avançar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025629152)**24. Na tela **Configuração de Hosts X Empresas/Filiais**, em **Hosts**, digite o endereço, porta e pasta da instância do Portal, conforme exemplo: localhost:8079/pp (não digite o "http"). Caso o servidor não seja local, digite o IP do servidor.  
  
25. Em **Selecione a Empresa/Filial**, selecione a Empresa que estará vinculada a este Portal (geralmente será exibida apenas uma opção **Todas as Empresas e Filiais**), então clique em **Relacionar**. A ligação entre o Host e a Empresa será listada em **Relacionamentos**  
26. Clique em **Avançar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025629332)**  
27. Na tela **Configuração de usuários**, em **Mínimo Usuários** e **Máximo Usuários**, que é a quantidade de threads que será aberta em execução (Mínimo) e a quantidade de threads que será aberta em espera (Máximo), digite as quantidades desejadas e clique em **Finalizar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025638872)  
  
28. Será exibida uma janela de confirmação da criação do Módulo Web. Clique em **Sim**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025655051)  
  
29. Ao final será exibido um aviso solicitando a reinicialização do Protheus para que a configuração entre em vigor. Clique em **Fechar**30. Após essa configuração, finalize o Totvs Wizard e reinicie o Protheus para que as alterações passem a vigorar. O arquivo **appserver.ini** será alterado com essas configurações, e a parte da configuração HTTP, WebService e Portal deve ficar semelhante ao exemplo abaixo:

```
#appserver.ini  
[HTTP]  
ENABLE=1  
PORT=8079  
PATH=C:\TOTVS 12\Microsiga\help-online  
Environment=P12  
   
[localhost:8079/ws]  
ENABLE=1  
PATH=C:\TOTVS 12\Microsiga\protheus_data\web\ws  
ENVIRONMENT=P12  
INSTANCENAME=ws  
RESPONSEJOB=JOB_WS_01010101  
DEFAULTPAGE=wsindex.apw  
   
[JOB_WS_01010101]  
TYPE=WEBEX  
ENVIRONMENT=P12  
INSTANCES=1,1  
SIGAWEB=WS  
INSTANCENAME=ws  
ONSTART=__WSSTART  
ONCONNECT=__WSCONNECT  
PREPAREIN=01,010101  
   
[ONSTART]  
JOBS=JOB_WS_01010101,JOB_PP  
   
[localhost:8079/pp]  
ENABLE=1  
PATH=C:\TOTVS 12\Microsiga\protheus_data\web\pp  
ENVIRONMENT=P12  
INSTANCENAME=pp  
RESPONSEJOB=JOB_PP  
   
[JOB_PP]  
TYPE=WEBEX  
ENVIRONMENT=P12  
INSTANCES=1,1  
SIGAWEB=PP  
INSTANCENAME=pp  
ONSTART=STARTWEBEX  
ONCONNECT=CONNECTWEBEX  
ONEXIT=FINISHWEBEX  
WEBSERVICELOCATION=http://localhost:8079/ws
```

31. Após reiniciar o Application Server, para testar se o serviço dos Webservices iniciou corretamente, abra o endereço do WebService no navegador (Internet Explorer, que é o navegador homologado para Portais e Webservices), conforme exemplo: <http://localhost:8079/ws>  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025656271)
