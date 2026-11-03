---
article_id: 360019141811
category: Portal de Gestão de Capital Humano
content_hash: d57fcf8f11c614b4384565151521cd20de5c7ed75e3e204003f3b34fd1f71316
fetched_at: '2026-06-28T22:42:58.888348+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao acessar o Portal não apresenta as opções
  do menu
type: support-article
updated_at: '2025-02-20T13:20:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019141811-RH-Linha-Protheus-PORTAL-GCH-Ao-acessar-o-Portal-n%C3%A3o-apresenta-as-op%C3%A7%C3%B5es-do-menu
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17124450754327) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Ao acessar o Portal GCH não apresenta as opções do menu.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Entre no módulo SIGATCF (18) e acesse o menu*Atualizações >Configurações > Web Services.*Ao entrar na rotina, clique em "Outras Ações" e Automático:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065991733)  
  
Depois, acesse o menu *Atualizações > Configurações > Menus*:  
  
**Observação:** Não é necessário efetuar nenhuma manutenção, apenas entrar na rotina e sair para carregar as informações.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064990654)  
  
Após realizar os procedimentos acima, entre no Portal Capital Humano e verifique se os **menus** são apresentados:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064990014)  
  
Há casos que, mesmo com essa configuração, os menus não são apresentados.  
Para esses cenários, orientamos que:  
- Verifique se as tabelas AI7, AI8 e AI9, tem o mesmo modo de acesso entre elas, de preferência compartilhadas CCC. As vezes é necessário recriar as tabelas AI7, AI8 e AI9 e depois refazer os passos abaixo:  
\* Entre no módulo SIGATCF (18) e acesse o menu *Atualizações >Configurações > Web Services.*\* Ao entrar na rotina, clique em "Outras Ações" e Automático:  
\* Depois, acesse o menu *Atualizações > Configurações > Menus*:  
**\* Observação:** Não é necessário efetuar nenhuma manutenção, apenas entrar na rotina e sair para carregar as informações.  
- Ter a *tag* Security=0 inserida no JOB do WS no appserver.ini conforme exemplo abaixo:

[localhost:85/ws33perfeeuufffff]  
ENABLE=1  
PATH=C:\PROTHEUS\_12\Microsiga\Protheus\_Data\_ctree\_2310\web\WS\_33\_PERF\_EEUUFFFFF  
ENVIRONMENT=2310\_PERF\_EEUUFFFFF  
INSTANCENAME=WS\_33\_PERF\_EEUUFFFFF  
RESPONSEJOB=JOB\_WS\_33\_PERF\_EEUUFFFFF\_01010100001  
DEFAULTPAGE=wsindex.apw

[JOB\_WS\_33\_PERF\_EEUUFFFFF\_01010100001]  
TYPE=WEBEX  
ENVIRONMENT=2310\_PERF\_EEUUFFFFF  
INSTANCES=1,2  
SIGAWEB=WS  
INSTANCENAME=WS\_33\_PERF\_EEUUFFFFF  
ONSTART=\_\_WSSTART  
ONCONNECT=\_\_WSCONNECT  
PREPAREIN=01,010100001  
**SECURITY=0**- Atualização do RPO do Portal GCH, [clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA);  
- Atualização dos *webfiles* via SRVWIZARD, veja como atualizar, [clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613-RH-Linha-Protheus-PORTAL-GCH-Como-Atualizar-os-arquivos-do-Portal#:~:text=O%20arquivo%20deve%20ser%20descompactado,para%20acatar%20os%20novos%20arquivos.).  
  
**IMPORTANTE**   
**SECURITY=0** conforme sugestões acima são aplicadas da versão 2310 pra baixo.   
Para versão 2410 em diante é obrigatório o uso do **SECURITY=1.**Deve ser configurado conforme acima mas com **SECURITY=1.**Para versão 2410 em diante é obrigatório aplicar a documentação abaixo:  
[Configuração portais GCH com autenticação **SECURITY=1**](https://tdn.totvs.com/pages/releaseview.action?pageId=563435668)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
