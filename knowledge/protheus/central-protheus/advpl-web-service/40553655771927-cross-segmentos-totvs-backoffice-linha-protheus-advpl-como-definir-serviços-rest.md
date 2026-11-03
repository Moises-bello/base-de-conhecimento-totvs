---
article_id: 40553655771927
category: ADVPL - Web Service
content_hash: e018acf36f13638d9f58c312b34faa97ad81b014f6bead3fbce6bd412f5b5ea3
fetched_at: '2026-06-28T22:40:10.565451+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Como definir
  serviços REST disponíveis ou bloqueados no TLPPCORE
type: support-article
updated_at: '2026-06-11T11:07:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40553655771927-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-definir-servi%C3%A7os-REST-dispon%C3%ADveis-ou-bloqueados-no-TLPPCORE
---

No TLPPCORE, para definir quais serviços REST estarão disponíveis ou bloqueados, utiliza-se as funções OnAllow e OnBlock no arquivo de configuração do AppServer, aplicando métodos em TLPP para permitir ou bloquear APIs específicas do TLPPCORE.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40561766761751)Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como definir quais serviços REST (endpoints e métodos) estarão disponíveis ou bloqueados em um determinado ambiente no TLPPCORE?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – a partir da versão 12.1.2410.

**Solução**  
O REST permite que o usuário customize o comportamento padrão de atendimento de requisições do sistema. Para gerenciar, limitar ou bloquear APIs REST em um ambiente, a aplicação disponibiliza as funções de *callback* **OnAllow** e **OnBlock**.

Estas funções informam à aplicação (AppServer) exatamente quais APIs REST estarão habilitadas para uso.   
É importante ressaltar que a aplicação não permite o uso simultâneo de **OnAllow** e **OnBlock** no mesmo ambiente. Quando ambas estão configuradas, a função **OnAllow** tem precedência e a função **OnBlock** é sumariamente ignorada.

**Atenção**: Este recurso de filtragem é exclusivo para serviços REST executados sob a arquitetura TLPP (tlppCore). Ele não possui efeito sobre serviços REST tradicionais construídos em ADVPL ou API padrões do Protheus informadas na documentação abaixo:  
<https://api.totvs.com.br/>  
  
Compreenda a diferença lógica entre elas para escolher a melhor estratégia de filtragem:

* **OnAllow**: Define explicitamente as APIs que devem ser permitidas, bloqueando automaticamente todas as demais requisições.
* **OnBlock**: Especifica apenas as APIs que devem ser bloqueadas, permitindo o uso irrestrito de todas as outras

**Sequencia de Passos:**

1. Certifique-se de que o ambiente utiliza o **AppServer** na versão 24.3.1.1 (ou superior) em conjunto com o TLPPCORE 01.05.10 (ou superior).
2. Configure a chave **OnAllow** ou **OnBlock** exclusivamente na seção de Thread Pool relacionada ao servidor REST no arquivo de configuração. Caso a chave seja configurada nas sessões destinadas aos Slaves, ela será ignorada.
3. A função customizada em TLPP receberá um único parâmetro, a classe **oList**, que disponibiliza os métodos de definição:

   * Para bloquear totalmente o uso, aplique o método **oList:block( cEndpoint, cMethod ).**
   * Para permitir o uso, aplique o método **oList:allow( cEndpoint, cMethod ).**
   * Para apenas ocultar a API da listagem de serviços disponíveis, utilize o método oList:hide( cEndpoint, cMethod ).
4. Caso a lógica de negócio exija receber a lista de APIs no momento do *callback*, ative este recurso configurando a propriedade **{"OnBlockGetApiList":true}** ou **{"OnAllowGetApiList":true}** na chave **TlppData**.
5. Devido à criticidade, se ocorrer alguma exceção (*exception*) durante a criação da lista de bloqueios, o comportamento padrão impede que o **AppServer** seja iniciado. Para contornar essa trava, configure a chave em modo "Soft" incluindo **{"OnBlockSoft":false}** ou **{"OnAllowSoft":false}** na propriedade **TlppData**.

Exemplo de código TLPP utilizando **OnAllow**:

```
function U_onAllow( oList )
  local cEndpoint as character
  local cServiceName as character
  local nServicePort as numeric
  local cThreadPoolName as character
  local cUserData as character
  local jApis as json

  // Use os valores abaixo conforme sua necessidade de implementação
  cServiceName    := oList:getServiceName()
  nServicePort    := oList:getServicePort()
  cThreadPoolName := oList:getThreadPoolName()
  cUserData       := oList:getUserData()
  jApis           := oList:getApiList()

  // Para permitir ou ocultar algum serviço, utilize os métodos Sets
  cEndpoint := '/exemplo1/urn'
  oList:allow( cEndpoint, 'get'  )
  oList:allow( cEndpoint, 'post' )
  oList:hide(  cEndpoint, 'put'  )

  cEndpoint := '/exemplo2/urn'
  oList:allow( cEndpoint, 'get' )

return
```

Exemplo de código TLPP utilizando **OnBlock**:

```
function U_onBlock( oList )
  local cEndpoint as character
  local cServiceName as character
  local nServicePort as numeric
  local cThreadPoolName as character
  local cUserData as character
  local jApis as json

  // Use os valores abaixo conforme sua necessidade de implementação
  cServiceName    := oList:getServiceName()
  nServicePort    := oList:getServicePort()
  cThreadPoolName := oList:getThreadPoolName()
  cUserData       := oList:getUserData()
  jApis           := oList:getApiList() 

  // Para bloquear ou ocultar algum serviço, utilize os métodos Sets
  cEndpoint := '/exemplo1/urn'
  oList:block( cEndpoint, 'get'  )
  oList:block( cEndpoint, 'post' )
  oList:hide(  cEndpoint, 'put'  )

  cEndpoint := '/exemplo2/urn'
  oList:block( cEndpoint, 'get' )

return
```

Exemplo de Configuração de no Appserver.ini:

```
[HTTPSERVER]
Enable=1
Servers=SERVIDOR_REST_01

[SERVIDOR_REST_01]
Port=8080
Locations=LOC_SRV_01

[LOC_SRV_01]
Path=/
ThreadPool=THREAD_POOL_SRV_01

[THREAD_POOL_SRV_01]
Environment=Ambiente
MinThreads=1
; Configurações passadas para o tlppCore
TlppData={"OnAllowGetApiList":true}
UserExits=MEUS_USER_EXITS

[MEUS_USER_EXITS]
; Define a função ADVPL/TLPP que será chamada na subida do serviço
OnAllow=U_onAllow
```

**Saiba mais**  
[OnAllow](https://tdn.totvs.com/display/tec/OnAllow)  
[onBlock](https://tdn.totvs.com/display/tec/onBlock)  
[REST server (tlppCore)](https://tdn.totvs.com/display/tec/REST)  
[Criação de API REST em TLPP (REST TLPPCore)](https://totvssuporte.zendesk.com/knowledge/editor/01JTGSFTXVTWZY79CP41C3WC2E/pt-br?brand_id=1509248)  
[Configurações Avançadas](https://tdn.totvs.com/pages/viewpage.action?pageId=553330350)  
[Entendendo as novidades do REST](https://tdn.totvs.com/display/public/framework/Entendendo+as+novidades+do+REST)
