---
article_id: 25623475431575
category: TAF - eSocial - Configuração
content_hash: 95cbd6d8bf96881c2c67109970e62bcba73e0c1e18cf3122e916fc4c458cf83a
fetched_at: '2026-06-28T22:45:14.444124+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial – Configurações - Como criar um appserver
  exclusivo.
type: support-article
updated_at: '2026-06-23T20:37:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25623475431575-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%B5es-Como-criar-um-appserver-exclusivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481791767) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como criar um appserver exclusivo, separado do ambiente principal, onde os possíveis erros serão direcionados somente para um arquivo console.log? Facilitando a interpretação e detecção de mensagens de erros do sistema.  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões

**Solução**

Muitos clientes utilizam balanceamentos, slaves, em sua infraestrutura, o que dificulta obter um arquivo console.log preciso, que demonstre os erros do sistema, para solucionar essa questão, este documento explica como criar um appserver separado dos apperver´s do ambiente.

**Dividiremos o passo a passo em processos.**

**Criando um appserver exclusivo:**

**1°** Realize cópia de uma das pastas appserver que já esteja configurada em seu ambiente.

Exemplo:

Neste caso, realizamos cópia da pasta com nome slave01 (cada ambiente possui o seu nome de pasta)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481793559)

**2°** Para melhor localização, alteramos o nome da pasta copiada para “EXCLUSIVO”.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481795735)

**3°** Acesse a nova pasta renomeada como “EXCLUSIVO” e abra o arquivo appserver.ini.

Localize o nome do ambiente que utiliza para acessar o sistema atualmente e “RENOMEIE”, orientamos utilizar também o nome “Exclusivo” para o novo ambiente. (Porém o cliente pode definir o nome que desejar).

Exemplo:

**Antes:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481797271)**

**Depois:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623475375383)**

**4°** Em seguida devemos mudar a porta **TCP**, utilize qualquer número que desejar, e que não esteja sendo utilizada em outros appserver´s;

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623475377687)

**5°** Altere também, o nome do ambiente na chave **app\_environment** que fica localizada no grupo **GENERAL** , insira o nome do novo ambiente: **Exclusivo**

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623475379223)

**6°** Como o objetivo do appserver exclusivo é adquirirmos um console preciso, é necessário ativar as chaves **TAFCONOUT** e **CONSOLELOG,** ambas localizadas no grupo **GENERAL.**

\*Caso não possua as chaves, crie as mesmas e ative.

**Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481809815)**

**7°** Após o appserver estar totalmente configurado, precisamos subir o serviço em modo console, para isso, precisamos criar um atalho.

Entre na pasta “EXCLUSIVO” do appserver que acabou de configurar;

Localize o arquivo appserver.exe

Clique com o botão direito do mouse e solicite “Criar atalho”:

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481812375)

Após manutenção, suba o serviço do appserver, em modo console, clicando duas vezes em cima do atalho que foi criado:

**Exemplo da tela que será apresentada:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481814423)**

**Alterando o Smartclient**

**8°** Precisamos alterar o Smartclient, devemos acessar a pasta smarclient, que já existente em seu sistema, e configurar o arquivo smartclient.ini, para fazer isso basta editar o arquivo smarclient.ini.

Em cima do arquivo smartclient.ini, clique com o direito do mouse e escolha “Editar”:

**Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623475387799)**

**9°** Começamos a configuração na chave **envserver**, localizada no grupo **“config”** acrescente o ambiente que acabou de criar, no nosso caso, chama-se **Exclusivo**.

**Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481817239)**

**10ª** Crie um novo grupo como o nome **“Exclusivo”**, contendo as chaves demonstradas abaixo:

\*\*O número da porta TCP deve ser o mesmo que inseriu no appserver.

**Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481818135)**

**11°** Após manutenção realizada no Smarclient, execute o mesmo (abra o Smartclient pelo atalho que já utiliza normalmente)

Na tela abaixo que será apresentada, realize os apontamentos utilizando as novas informações do ambiente exclusivo, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481819799)

**12°** Para validar se está utilizando o novo ambiente (appserver) criado, corretamente, após entrar no sistema, valide o nome apresentado no cabeçalho, no nosso caso, deve ser apresentado o nome “Exclusivo”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623481820823)

Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
