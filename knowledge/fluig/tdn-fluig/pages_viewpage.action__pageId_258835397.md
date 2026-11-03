---
content_hash: 13e5fc56a41c41cbbed3f53a5c2181f278566a1173e100a4f8b32ae3f1a0ad8f
fetched_at: '2026-06-28T21:35:23.794506+00:00'
page_id: '258835397'
product: fluig
source: tdn-fluig
title: BPM 092 - Como solucionar o erro "Batch update returned unexpected row count"
  ao movimentar solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258835397
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

Ao movimentar uma solicitação, o erro "*Batch update returned unexpected row count from update [0]; actual row count: 0; expected: 1*" é exibido em tela. Essa mensagem impede que a atividade seja movimentada.

# Causa

A causa desse erro ainda não foi identificada. Cada situação precisa ser analisada individualmente para que a equipe de manutenção providencie uma correção pontual.

# Solução

Se o erro acontecer na atualização 1.5.6 ou anteriores é necessário atualizar o fluig para uma versão mais nova disponível no Portal de Clientes. A partir da versão 1.5.7-EP5 foi criado um log em nível de *debug* para percorrer a sessão em busca de objetos que não foram feitos o *flush*.

samplestrue1fluig 1.5.13 ou inferior

Para isso, é preciso adicionar a seguinte classe no *debug* do servidor de aplicação com.datasul.technology.webdesk.workflow.business.BatchUpdateLogger

Com o serviço do fluig parado realize os passos abaixo:

* Editar o arquvo **standalone.xml** disponível em <instalacao\_fluig>\jboss\standalone\configuration;

* Procurar pela tag **<root-logger>**;

* Adicionar este código logo acima da tag **<root-logger>**;

java

]]>

* Iniciar o serviço do fluig novamente e simular o erro.

Quando o erro acontecer novamente, abra um chamado para o suporte fluig e envie o arquivo **server.log** e o arquivo **chrono.log** (ambos em <instalacao\_fluig>\jboss\standalone\log) para análise.

2fluig 1.6.0 ou superior

Para isso, é preciso adicionar a seguinte classe no *debug* do Servidor de Aplicação Wildfly: com.datasul.technology.webdesk.workflow.business.BatchUpdateLogger

Com o serviço do fluig parado realize os passos abaixo:

* Editar o arquvo **domain.xml** disponível em <instalacao\_fluig>\appserver\domain\configuration;

* Procurar pela tag **<root-logger>**;

* Adicionar este código logo acima da tag **<root-logger>**;

java

]]>

* Iniciar o serviço do fluig novamente e simular o erro.

Quando o erro acontecer novamente, abra um chamado para o suporte fluig e envie o arquivo **server.log** e o arquivo **chrono.log** (ambos em <instalacao\_fluig>\appserver\domain\servers\<server-fluig>\log) para análise.
