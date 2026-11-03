---
article_id: 360044715514
category: IMPLANTAÇÃO
content_hash: bbf951ef0b1029eec2e8219d2fcd1d7a92ec2f6b9efef0abf39a4631cd88c922
fetched_at: '2026-06-28T22:44:33.425777+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI e PROPERTIES.JSON
  para acesso ao MEU RH
type: support-article
updated_at: '2026-06-26T21:33:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514-RH-Linha-Protheus-MEU-RH-Como-configurar-o-APPSERVER-INI-e-PROPERTIES-JSON-para-acesso-ao-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18058078236823)**Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar o APPSERVER.INI e PROPERTIES.JSON para acesso ao MEU RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões.  
  
**Solução**  
Essas informações estão descritas passo a passo na [**DOCUMENTAÇÃO DE REFERÊNCIA DO MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421).

[0.0 Instalação e Configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=285648322)

* [0.2 Linha Protheus](https://tdn.totvs.com/display/NPR/0.2++Linha+Protheus)

  + [0.2.1 Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=532651492)

    - [Passo 1: Atualizando os arquivos](https://tdn.totvs.com/display/NPR/Passo+1%3A+Atualizando+os+arquivos)
    - [Passo 2: Amarrações de usuários](https://tdn.totvs.com/display/NPR/Passo+2%3A+Amarracoes+de+usuarios)
    - [Passo 3: Configurando REST](https://tdn.totvs.com/display/NPR/Passo+3%3A+Configurando+REST)
    - [Passo 4: Configurando *appserver* e *properties*](https://tdn.totvs.com/display/NPR/Passo+4%3A+Configurando+appserver+e+properties)
    - [Passo 5: Acessando o portal e app](https://tdn.totvs.com/display/public/NPR/Passo+5%3A+Acessando+o+portal+e+app)

Em todo caso, disponibilizamos abaixo exemplos da configuração utilizada internamente.  
  
**Obs.: Lembrando que as configurações mencionadas abaixo, tratam-se de exemplos nos quais foram configurados em ambiente padrão para testes.**  
  
Segue abaixo o exemplo da configuração do Meu RH no ***APPSERVER.INI*****:**  
  
[HTTP]  
ENABLE=1  
PORT=85  
PATH=C:\PROTHEUS\_12\MICROSIGA\Protheus\_Data\_ctree\_2210\web  
ENVIRONMENT=2210\_PERF\_EEUUFFFFF  
Compression=1  
  
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

Segue abaixo o exemplo da configuração do MEU RH no ***PROPERTIES.JSON*****.** O arquivo deve estar na mesma pasta onde estão os demais arquivos do **Portal MEU RH (arquivo anexo ao final deste documento):**  
  
**{**  
**"ERP": 3,**  
**"PROPS":**  
**{**  
**"baseUrl": "http://localhost:8080/rest01",**  
**"rootContext": "/01/"**  
**}**  
**}**  
  
**Importante:** No *rootcontext* tem que estar conforme acima, com a referência ao grupo/empresa, sendo mesmo conteúdo da chave *Preparein* do ini do cliente, já houveram casos que estavam diferente causando problemas, exemplo "01" sem as barras, o correto é "/01/"   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800650698263)**  
  
[**Qual deve ser o conteúdo do arquivo PROPERTIES.JSON**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314/)  
  
O **PROPERTIES.JSON** encontra-se na pasta com os arquivos do **Portal MEU RH,** que pode ser baixado na Central de *downloads*. Caso esteja configurando o MEU RH pela primeira vez, o ***PROPERTIES.JSON*** precisa ser renomeado de ***PROPERTIES\_EXEMPLO***para ***PROPERTIES*** antes de ser colocado dentro da pasta com os arquivos do Portal no ambiente.   
  
Segue exemplo:  
![properties.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9143742488599)  
  
[**Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
**Obs.: Segue anexo ao final este artigo, uma cópia do arquivo properties.json já renomeado.**  
  
**Saiba Mais**  
[**Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
