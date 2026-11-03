---
article_id: 360060684834
category: Gestão de Distribuição (SIGAOMS)
content_hash: 2e3ab1be7da286a13d1d3caf9f042896a78499b185acf074fa6cd27ef6381cc2
fetched_at: '2026-06-28T22:45:49.698596+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como habilitar o LOG de integração do TOTVS
  OMS e TOL/TRE
type: support-article
updated_at: '2025-04-02T18:17:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-Log%C3%ADstica-Linha-Protheus-OMS-Como-habilitar-o-LOG-de-integra%C3%A7%C3%A3o-do-TOTVS-OMS-e-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20294506240663)Tempo aproximado para leitura: **00:02:24 min**  
**Dúvida**Como habilitar o **LOG de integração** do **TOTVS OMS** e **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para facilitar a analise das informações enviadas e recebidas na integração **TOTVS** **OMS** e **TOL/TRE**, desenvolvemos uma função para gerar mensagens auxiliares, informações de *query* e conteúdos de variáveis para o **Console.log** do **PROTHEUS.**Para utilizar essa funcionalidade, abaixo descrevemos os itens que deverão ser habilitados:

* No arquivo **Appserver.ini**, acrescente os **três parâmetros** abaixo, na seção do **ambiente** que irá se logar e no ambiente que realizará a integração.  
  Exemplo:  
  **LOGCPLOMS=.T.**  
  **FWFRAME\_TRACELOG=1**  
  **LOGTIPOMS=CONSOLE**O parâmetro **LOGTIPOMS**, define a forma de saída das mensagens, podendo ser **CONSOLE** ou **ARQUIVO**. Como ***default*** o Sistema irá gerar no **Console.log do Appserver.**  
  Caso desejar separar as mensagens e salvar com o nome do arquivo igual a **omscpl.log** dentro da pasta *system*, informe **ARQUIVO** no parametro **LOGTIPOMS.**Para **implantação ou análise de desempenho dessa integração**, recomendamos utilizar o parâmetro **LOGTIPOMS=CONSOLE**. Em ambientes com grande volume de dados, a opção **LOGTIPOMS=ARQUIVO** pode causar lentidão nos processos de integração.
* Na seção **General**, acrescente as seguintes linhas abaixo:   
  **ConsoleLog=1** - Habilitar para que o ***trace*** seja gerado no arquivo **Console.log** do **PROTHEUS**. **ConsoleFile=C:\Protheus\log\console\_p12.log** - Informar o caminho que será gerado o **Console.log** do **PROTHEUS.**  
  **ConsoleMaxSize=524288** - Informar o tamanho máximo do **Console.log** do **PROTHEUS.**

Exemplo do arquivo **Appserver.ini:****[General]**CHECKSPECIALKEY=0  
**CONSOLELOG=1**  
InstalPath=C:\Protheus  
buildkillusers=1  
**ConsoleFile=C:\Protheus\log\console\_p12.log**  
**ConsoleMaxSize=524288**  
MAXSTRINGSIZE=5  
  
**[Protheus12]**  
SourcePath=C:\Protheus\apo\prd  
RootPath=C:\Protheus\data  
StartPath=\system\  
RpoDB=TOP  
RpoLanguage=Portuguese  
RpoVersion=120  
LocalFiles=ADS  
SpecialKey=P12\_DL  
LocalDBExtension=.dbf  
PictFormat=DEFAULT  
DateFormat=DEFAULT  
RegionalLanguage=BRA  
**FWFRAME\_TRACELOG=1**  
TDSView=1  
TOPMEMOMEGA=1  
DBDataBase=MSSQL  
DBServer=localhost  
DBPort=8060  
DBALIAS=Totvs12  
**LOGCPLOMS=.T.  
LOGTIPOMS=CONSOLE****[Protheus12WEB]**  
SourcePath=C:\Protheus\apo\prd  
RootPath=C:\Protheus\data  
StartPath=\system\  
RpoDB=TOP  
RpoLanguage=Portuguese  
RpoVersion=120  
LocalFiles=ADS  
SpecialKey=P12\_DL   
LocalDBExtension=.dbf  
PictFormat=DEFAULT  
DateFormat=DEFAULT  
RegionalLanguage=BRA  
**FWFRAME\_TRACELOG=1**  
TDSView=1  
TOPMEMOMEGA=1  
DBDataBase=MSSQL  
DBServer=localhost  
DBPort=8060  
DBALIAS=Totvs12  
**LOGCPLOMS=.T.  
LOGTIPOMS=CONSOLE**Com as configurações acima, será gerado o **Console.log** do **PROTHEUS** com as mensagens de integração entre o **TOTVS OMS** e **TOL/TRE**.**Importante**Caso utilize mais de um ambiente, onde terá mais de um arquivo **Appserver.ini**, atentar para que as configurações acima sejam incluídas em todos arquivos **Appserver.ini** envolvidos na integração do **TOTVS OMS** e **TOL/TRE.** **Saiba mais**Mais informações poderão ser acessadas no *link*:  
[TOTVS OMS x TOL/TRE - Geração do Log de integração - OMSXCPL - via Console do Protheus.](https://tdn.totvs.com/pages/releaseview.action?pageId=663844058)   
[TOTVS OMS x TOL/TRE - Geração de arquivo de LOG](https://tdn.totvs.com/pages/releaseview.action?pageId=592058894)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-SIGAOMS-x-TOTVS-Log%C3%ADstica-Cockpit)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
