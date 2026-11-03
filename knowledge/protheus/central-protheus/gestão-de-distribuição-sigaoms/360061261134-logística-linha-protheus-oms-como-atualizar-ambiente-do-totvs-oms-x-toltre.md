---
article_id: 360061261134
category: Gestão de Distribuição (SIGAOMS)
content_hash: e3070cea51af2cf204bce5e5a39df387cfdebdc46059dfce74c8f9bdc7701958
fetched_at: '2026-06-28T22:45:49.600242+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como atualizar ambiente do TOTVS OMS x TOL/TRE
type: support-article
updated_at: '2022-10-17T20:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061261134-Log%C3%ADstica-Linha-Protheus-OMS-Como-atualizar-ambiente-do-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:06 min**  
**Dúvida**Como atualizar ambiente do **TOTVS OMS** quando tem integração com o **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para atualizar o ambiente **TOTVS OMS** disponibilizamos o **Pacote Acumulado do Módulo**, que contém todas as atualizações liberadas. Esse pacote é oficial e **homologado pela TOTVS**.  
  
Segue *link*: **[Pacotes de Atualização - TOTVS OMS - P12](https://tdn.totvs.com/x/QVQxIQ)**  
  
**Importante:**  
Caso utilize mais de um ambiente, podendo existir mais de um arquivo **Appserver.ini** envolvidos na integração do **TOTVS OMS x TOL/TRE**, atentar para que o **RPO seja atualizado em ambos ambientes.** Verificar o **parâmetro SourcePath** nos arquivos **Appserver.ini**.  
  
Exemplo:  
  
**[Protheus12]**  
**SourcePath=C:\Protheus\apo\prd**  
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
FWFRAME\_TRACELOG=1  
TDSView=1  
TOPMEMOMEGA=1  
DBDataBase=MSSQL  
DBServer=localhost  
DBPort=8060  
DBALIAS=Totvs12  
LOGCPLOMS=.T.  
  
**[Protheus12WEB]**  
**SourcePath=C:\Protheus\apo\prd\web**  
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
FWFRAME\_TRACELOG=1  
TDSView=1  
TOPMEMOMEGA=1  
DBDataBase=MSSQL  
DBServer=localhost  
DBPort=8060  
DBALIAS=Totvs12  
LOGCPLOMS=.T.  
  
**Saiba mais**Mais informações poderão ser acessadas no *link's*:   
[Logística - Linha Protheus - OMS - Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-SIGAOMS-x-TOTVS-Log%C3%ADstica-Cockpit)  
[Logística - Linha Protheus - OMS - Como habilitar o Console.log do PROTHEUS com mensagens auxiliares na integração do TOTVS OMS e TOL/TRE](https://totvssuporte.zendesk.com/knowledge/articles/360060684834/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360060684834)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
