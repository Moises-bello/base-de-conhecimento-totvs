---
article_id: 360028437812
category: Portal de Gestão de Capital Humano
content_hash: dff35b6cd61aa854d455c5e1e0f834bbf438eda706230740d3b93d680ee7cfe8
fetched_at: '2026-06-28T22:42:58.983691+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Envio de WorkFlow solicitações do portal
  GCH / App MeuRH
type: support-article
updated_at: '2024-05-16T21:18:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028437812-RH-Linha-Protheus-PORTAL-GCH-Envio-de-WorkFlow-solicita%C3%A7%C3%B5es-do-portal-GCH-App-MeuRH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18195299094935) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como configurar o envio de workflow para as solicitações do Portal GCH ou App Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano e App Meu RH – Todas as versões  
  
**Solução**Para fazer o envio de *workflow* das solicitações, siga os respectivos passos:  
  
1 - Localize o arquivo **WFSOLICPORTAL.HTML** que provavelmente está em sua pasta **WEB/PP e coloque dentro da pasta Protheus\_Data/*Workflow;***  
2 - No **appserver.ini** deve conter a **sessão [*MAIL*}** com as seguinte informações:

[MAIL]  
Protocol=SMTP  
authLogin=0  
authNTLM=0  
authPlain=0  
ExtendSMTP=1  
TLSVersion=3  
SSLVersion=2

3 - Configuração da conta de *e-mail* pela rotina no SIGACFG, **Ambiente >Workflow > Contas de E-mail:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001647462)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102708953)

4 - Configuração *Proxy* no **SIGACFG** na rotina: **Ambiente > *E-mail/Proxy* > Configurar:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001695301)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001647542)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102709053)  
  
5 - Liberação da sua **conta de *e-mail* para *app's* menos seguros**, por exemplo, ***Gmail***:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100541834)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048600233)

Após isso, será disparado o ***WorkFlow no e-mail***.  
Exemplo: Solicitação de Férias (qualquer outra rotina que contemple esta funcionalidade).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18195097661463)  
  
6 - Amarre as contas de ***e-mail*** no cadastro de participantes tabela RD0 e no Cadastro de funcionários tabela SRA.  
  
Após essas configurações, **a cada solicitação no portal será enviado um *e-mail* para o participante** como informativo a respeito desta solicitação.  
  
**OBS:** O *workflow* do Portal serve somente como acompanhamento e **não executa aprovações**, sendo necessário **o usuário logar no portal para aprovar/reprovar.**  
  
Exemplo de configuração:  
***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011628402)*****IMPORTANTE:**Cabe ressaltar que, neste processo não há Pontos de Entrada para customização dessa funcionalidade.**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
