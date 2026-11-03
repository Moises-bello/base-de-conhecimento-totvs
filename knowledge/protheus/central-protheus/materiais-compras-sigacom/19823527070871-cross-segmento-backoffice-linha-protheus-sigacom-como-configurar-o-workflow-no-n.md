---
article_id: 19823527070871
category: Materiais - Compras (SIGACOM)
content_hash: 3c11a72679cd773e7432f171b074735b000dfcc5628728fe04bad56a9401f990
fetched_at: '2026-06-28T22:41:10.550070+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o
  WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?
type: support-article
updated_at: '2026-05-19T12:51:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19823518893335) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**  
Com o workflow integrado ao Novo Fluxo de Compras - NFC, as experiências dos compradores e até mesmo dos fornecedores serão incríveis! Existem duas formas de utilizar o workflow:

- **Todos** usuarios **compradores** do sistema **utilizam** a **mesma** **caixa de** **e-mail** para disparo dos formularios aos fornecedores, nessa opção permite que o fornecedor "responda" o e-mail em caso de alguma dúvida porém toda comunicação ficará centralizada em uma caixa de e-mail;

- **Cada** usuario **comprador** poderá ter sua **propria** **caixa** **de e-mail** personalizada para disparo dos formularios aos fornecedores, permitindo assim que o fornecedor "responda" o e-mail em caso de dúvidas diretamente ao comprador que solicitou aquela compra **(Configuração Opcional) -** [Clique aqui e aprendar como configurar com essa opção!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559)

**Ou,** para configurar workflow utilizando a mesma caixa de e-mail para todos usuarios compradores, realize as configurações destacadas abaixo:

**Passo 1:**

* Acessar o módulo do configurador (SIGACFG) > Ambiente > WorkFlow > Contas de e-mail > Incluir

Exemplo de configuração do e-mail do GMAIL:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19823643284631)

Após criar a caixa do e-mail, preencher o nome da caixa (**Cx Correio**) no parâmetro **MV\_NFCPOBX**

**MV\_NFCPOBX -**Defineo nome da Caixa de Correio (WF7\_PASTA), que será utilizada para envio do Workflow do NFC. 

**Importante:** Por motivos de segurança, a Google descontinuou a configuração de aplicativos menos seguros. Assim, será necessária uma configuração de senhas para uso do workflow (exclusivo google). Essa nova configuração é a "Senhas de App”, aprenda criar [clicando aqui.](https://www.youtube.com/watch?v=wGikJth4dN0&t=14s)

Mais informações [clique aqui.](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail?spaceEditingRestriction=true)

**Passo 2:**

* **Crie** uma nova **pasta** **dentro** da **Protheus\_Data** para receber os arquivos de configuração do NFC, exemplo: C:\TOTVS\Protheus2310\Protheus\_data**\workflow** (nome da pasta Workflow)
* Acesse o NFC com **usuário** **administrador**;
* Clique no botão de perfil (ícone a direita, na parte superior da tela), para exibir os submenus existentes. Clique no menu com o nome **Wizard WebService/Parâmetros**.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19825253506455)
* **Primeira Etapa:**   
  - Informe o nome da pasta criada acima. Exemplo: **\Workflow;**  
  - Faça o download dos arquivos .html e extraia na pasta informada acima  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19824776506391)

Importante: Caso seu ambiente esteja hospedado no Cloud, as configurações a seguir precisam ser verificadas junto ao CLOUD, solicitar o IP + Porta para realizar a configuração.

* **Segunda Etapa:**  
  - Informe o **IP publico** do servidor do Workflow, **Exemplo**: **http://**10.173.14.166  
  **IMPORTANTE**: É obrigatório inserir **http://** antes do IP+Porta  
  - Informe a porta do WorkFlow, **Exemplo**: 8082  
  - Informe o nome do ambiente onde o Workflow é executado, **Exemplo**: P2310  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19825768835863)  
    
  - Informe IP/porta do servidor de workflow, Exemplo: **http://10.173.14.166:8082**  
    
  **Terceira Etapa:**  
  - Apenas será validado se a porta MultiProtocolPort está ativa no INI;  
    
  **Quarta Etapa:**  
  - Insira as configurações do servidor de e-mail exatamente como foi configurado na **Passo 1,** avance até a última etapa;  
    
  **Última Etapa:**  
  - A rotina irá sugerir algumas **configurações** **minimas** para que sejam **inclusas** no **appserver.ini (Configuração obrigatória)**, essas configurações são referente a todas etapas realizadas no wizard. Vale ressaltar que o **wizard** **NÃO** altera **nenhuma** **configuração** no **INI**, **esse** **processo** **deve** **ser** **realizado** **manualmente** pelo adminstrador responsável pelo ambiente Protheus  
    
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
PATH=C:\TOTVS\Protheus2310\Protheus_data\workflow  ;Indica o local de leitura dos arquivos inseridor no passo 2;
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

Parabéns! Seu workflow está configurado e pronto para uso no Novo Fluxo de Compras - NFC está pronto para uso, aproveite ao máximo essa nova experiência!

Para maiores informações sobre o NFC acesse: [Novo Fluxo de Compras: Guia de Referências](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

**SAIBA MAIS EM :**

[**PÁGINA CENTRALIZADORA COMPRAS**](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[**Mais Artigos Materiais - Compras (SIGACOM)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
