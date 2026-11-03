---
article_id: 19837259521559
category: Materiais - Compras (SIGACOM)
content_hash: 39904bc8c78be44301375e241a62c31d119d468532081b88040971c013bd02ef
fetched_at: '2026-06-28T22:41:10.563009+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o
  WorkFlow utilizando o e-mail dos compradores no envio dos formulários no Novo Fluxo
  de Compras - NFC (PGCA010)?
type: support-article
updated_at: '2024-07-05T14:41:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-utilizando-o-e-mail-dos-compradores-no-envio-dos-formul%C3%A1rios-no-Novo-Fluxo-de-Compras-NFC-PGCA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19837259426455) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como configurar o WorkFlow utilizando o proprio e-mail do comprador para envio dos formulários de cotação no Novo Fluxo de Compras - NFC (PGCA010)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**Para permitir que cada comprador utilize sua propria caixa de e-mail no processo de cotação junto ao seu fornecedor, será necessario algumas configurações que vamos detalhar nos passo-a-passo abaixo:

**Passo 1:**

* Habilite o parâmetro MV\_PGCWF;

**Passo 2:**

* **Crie** uma nova **pasta** **dentro** da **Protheus\_Data** para receber os arquivos de configuração do NFC, exemplo: C:\TOTVS\Protheus2310\Protheus\_data**\workflow** (nome da pasta Workflow)

**Obs.:** Esse caminho será utilizado para gravação dos arquivos templates gerados pelo workflow

* Acesse o NFC com **usuário** **administrador**;
* Clique no botão de perfil (ícone a direita, na parte superior da tela), para exibir os submenus existentes. Clique no menu com o nome **Wizard WebService/Parâmetros**.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837291406231)
* **Primeira Etapa:**   
  - Informe o nome da pasta criada acima. Exemplo: **\Workflow;**- Faça o download dos arquivos .html e extraia na pasta informada acima![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837280814871)
* **Segunda Etapa:**  
  - Informe o **IP publico** do servidor do Workflow, **Exemplo**: **http://**10.173.14.166  
  **IMPORTANTE**: É obrigatório inserir **http://** antes do IP+Porta  
  - Informe a porta do WorkFlow, **Exemplo**: 8082  
  - Informe o nome do ambiente onde o Workflow é executado, **Exemplo**: P2310  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837306535063)  
    
  - Informe IP/porta do servidor de workflow, Exemplo: **<http://10.173.14.166:8082>**
* **Terceira Etapa:**  
  - Apenas será validado se a porta MultiProtocolPort está ativa no INI;
* **Quarta Etapa:**  
  - Insira as configurações do servidor de e-mail, **Exemplo**: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19839659214231)****![](https://centraldeatendimento.totvs.com/hc/article_attachments/19839659233687)****IMPORTANTE:** As informações acima são apenas exemplos de configuração para servidor de e-mail google, outros servidores podem ter informações diferentes;
* **Última Etapa:**- A rotina irá sugerir algumas **configurações** **minimas** para que sejam **inclusas** no **appserver.ini (Configuração obrigatória)**, essas configurações são referente a todas etapas realizadas no wizard. Vale ressaltar que o **wizard** **NÃO** altera **nenhuma** **configuração** no **INI**, **esse** **processo** **deve** **ser** **realizado** **manualmente** pelo adminstrador responsável pelo ambiente Protheus  
    
  Exemplo de Configuração com base dos dados utilizados nas etapas anteriores:

Copie e insira no seu ambiente o exemplo abaixo, altere as informações em **negrito**para informações do seu ambiente, tais como: 

```
;-------------------------------- WEBSERVICE - PGC --------------------------------------------  
  
[HTTP]  
ENABLE=1  
PATH=C:\TOTVS\Protheus2310\Protheus_data\http-root  
PORT=8082  
ENVIRONMENT=P2310  
INSTANCES=1,10  
XFRAMEOPTIONS=ALLOW-FROM *  
UPLOADPATH=\web  
  
[10.173.14.166:8082]   ;Esse é endereço público utilizado pelo workflow  
enable=1  
port=8082  
PATH=C:\TOTVS\Protheus2310\Protheus_data\workflow  ;Indica o local de leitura dos arquivos gerados no passo 2;  
environment=P2310  
responsejob=WF_INDEX  
DEFAULTPAGE=wsindex.apw  
PREPAREIN=ALL  
  
[WF_INDEX]   
TYPE=WEB  
environment=P2310  
INSTANCES=1,10  
SIGAWEB=WF  
INSTANCENAME=WF  
ONSTART=STARTWEBEX  
ONCONNECT=CONNECTWEBEX  
ONEXIT=FINISHWEBEX  
  
[MAIL]  
Protocol=SMTP  
ExtendSMTP=1  
SSLVersion=3  
AuthLOGIN=1  
AuthPLAIN=1  
TLSVersion=3  
  
[OnStart]  
jobs=WF_INDEX
```

**Passo 3:**

* Vincule o e-mail do comprador no cadastro de usuário **(Obrigatório);**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837306545943)

* Acesse o NFC utilizando o usuário comprador que deseja realizar a configuração
* Clique no botão de perfil (ícone a direita, na parte superior da tela), para exibir os submenus existentes. Clique no menu com o nome **Wizard E-mail comprador.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837291429399)**
* **Primeira Etapa:**- Informe o nome do Comprador que será utilizado no Remetente do e-mail;  
    
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19837280833303)**
* **Segunda Etapa:**- Informe a senha do e-mail do Comprador;
* **Importante:** Por motivos de segurança, a Google descontinuou a configuração de aplicativos menos seguros. Assim, será necessária uma configuração de senhas para uso do workflow (exclusivo google). Essa nova configuração é a "Senhas de App”, aprenda criar [clicando aqui.](https://www.youtube.com/watch?v=wGikJth4dN0&t=14s)

  Mais informações [clique aqui.](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail?spaceEditingRestriction=true)
* **Terceira Etapa:**  
  - As configurações do servidor de e-mail (SMTP / IMAP) será carregada automaticamente devido a configuração realizada na **Quarta Etapa do Passo 2,** clique em "próximo" para concluir a configuração;  
    

  Parabéns! Seu workflow está configurado e pronto para uso no Novo Fluxo de Compras - NFC está pronto para uso, aproveite ao máximo essa nova experiência!

  Para maiores informações sobre o NFC acesse: [Novo Fluxo de Compras: Guia de Referências](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

  **SAIBA MAIS EM :**

  **[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

  **[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)**
