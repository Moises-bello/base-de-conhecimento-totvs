---
article_id: 360043357693
category: LOGIN
content_hash: b8431b3bfbb458da7885d3fc7d0bdb47235922a0192159f395d3adab24cc9271
fetched_at: '2026-06-28T22:44:40.704905+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que fazer quando acesso o Link do MEU RH e
  a página fica carregando em Looping
type: support-article
updated_at: '2026-01-23T21:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043357693-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-acesso-o-Link-do-MEU-RH-e-a-p%C3%A1gina-fica-carregando-em-Looping
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17269644884375) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
O que fazer quando acesso o Link do Meu RH e a página fica carregando em *Looping*  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Caso acesse o *link* do Portal MEU RH e a página ficar carregando em *Looping,* você deverá conferir novamente as configurações:  
**![tela_MEU_RH_looping.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7659235368983)**  
  
Esses casos ocorrem por problemas **do usuário do SIGACFG estar bloqueado,** configuração do **appserver.ini** ou do **properties.json.**  
  
Relacionado ao usuário, entrar no **módulo 18 - SIGATCF > Atualizações > Configurações > Usuários > Genéricos** para saber qual é o código do usuário do **SIGACFG** vinculado conforme *print* abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17269342094487)  
  
Sabendo qual o código do usuário entrar no **módulo 99 - SIGACFG > Usuário > Senhas > Usuários > Alterar** e confirmar se realmente o mesmo esta bloqueado ou não conforme print abaixo. Caso esteja seria a causa do erro, avalie se deve desbloquear o usuário ou definir outro usuário no **cadastro de Usuários Genéricos** do **módulo 18 - SIGATCF** conforme citado nos passos acima.![](https://centraldeatendimento.totvs.com/hc/article_attachments/17269638563991)  
  
Relacionado as demais sugestões citadas, valide novamente sua configuração do Portal conforme documentação abaixo.  
[**Configurando o serviço** ***REST*** **via APWebWizard**](https://tdn.totvs.com/display/public/NPR/Passo+3%3A+Configurando+REST)  
  
O primeiro passo é verificar se o serviço ***REST***está ativo:  
  
Para identificarmos se o serviço ***REST*** está carregando adequadamente, verificamos se é possível realizar o carregamento dos serviços via *browser*.  
  
No exemplo abaixo, foi utilizada a porta **6663** do ***REST*** e o nome da ***URL*** definida **/rest99:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7658681845015)  
  
Segue abaixo um exemplo de configuração do MEU RH no **APPSERVER.INI**

[HTTP]  
ENABLE=1  
PORT=85  
PATH=C:\PROTHEUS\_12\MICROSIGA\Protheus\_Data\_ctree\_2210\web  
ENVIRONMENT=2210\_PERF\_EEUUFFFFF  
Compression=1  
TIMEOUT=9999   
SESSIONTIMEOUT=9999  
CACHE-CONTROL=NO-STORE  
SECURITY=0  
  
[localhost:85/01]  
ENABLE=1  
PATH=C:\PROTHEUS\_12\MICROSIGA\Protheus\_Data\_ctree\_2210\web\1\_MeuRH  
ENVIRONMENT=2210\_PERF\_EEUUFFFFF  
INSTANCENAME=MEURH  
DEFAULTPAGE=index.html  
  
[HTTPV11]  
ENABLE=1  
Sockets=HTTPREST  
TIMEOUT=9999  
ADVPL=1  
Stateless=1  
  
[HTTPREST]  
Port=8080  
URIs=HTTPENV01  
SECURITY=1  
IPsBind=  
  
[HTTPENV01]  
URL=/rest01  
PrepareIn=01  
Instances=2,5,1,1  
CORSEnable=1  
AllowOrigin=\*   
EnableKeepAlive=0  
Public=fwjwt/refresh\_token,auth,setting/companySettings  
  
[RESTCONFIG]  
restPort=8080  
RefreshTokenTimeout=300  
meurhLog=1  
  
[RESTJOB]  
MAIN=HTTP\_START  
ENVIRONMENT=2210\_PERF\_EEUUFFFFF  
  
[ONSTART]  
JOBS=RESTJOB  
REFRESHRATE=120  
EBUGMSG=1

Segue abaixo o exemplo da configuração do MEU RH no **PROPERTIES.JSON.** O arquivo deve estar na mesma pasta onde estão os demais arquivos do **Portal MEU RH (arquivo anexo ao final deste documento):**  
  
**{**  
**"ERP": 3,**  
**"PROPS":**  
**{**  
**"baseUrl": "http://localhost:8080/rest01",**  
**"rootContext": "/01/"**  
**}**  
**}**  
  
**Importante:** No *rootcontext* tem que estar conforme acima com referência ao grupo/empresa mesmo conteúdo da chave *Preparein* do ini do cliente ja tivemos casos que estavam diferente causando problemas exemplo "01" sem as barras, o correto é "/01/"   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864331576471)**  
  
[**MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314/)  
  
O arquivo **PROPERTIES.JSON**fica gravado na pasta dos arquivos web do Portal MEU RH, no exemplo abaixo foram gravados na pasta ***web*** dentro da **Protheus\_data**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864472108695)  
  
Para o acesso ocorrer adequadamente é importante manter o RPO e Arquivos do Portal MEU RH atualizados, caso tenha dúvidas, verifique os artigos abaixo:  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
  
**Obs: Caso utilize** ***Broker*** **no seu ambiente:**  
**Adicione na chave do Broker** **HTTP/HTTPS** **a** ***tag*****:****USING\_COOKIES=0**  
  
Se somente no **App** ficar processando e não abrir, no app entre em Configurar > Ambiente > Meus Ambientes > Selecione o nome do seu ambiente > Editar ambientes e valide se no Campo **URL** a paralavra **?restport** esta com a letra **"p"** minúscula, o correto é estar somente com **"P"** Maiúsculo.  como exemplo: **?restPort**.  
  
Vale ressaltar que, o Meu RH inicialmente precisa estar acessível como *localhost*, IP interno do servidor.  
Depois, deverão configurar o acesso externo via IP ou DNS público, conforme artigo como apoio:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/18893492234903>   
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUIpara acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
