---
article_id: 33541555451799
category: ADVPL - Web Service
content_hash: ec1feea6689cc122b475153b4519df8a070a3cf949076fbf43ac932f1961eb33
fetched_at: '2026-06-28T22:40:10.341676+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice - Linha Protheus - ADVPL- Restrições na atribuição
  das variáveis cEmpAnt e __cUserId
type: support-article
updated_at: '2025-07-22T11:41:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33541555451799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Restri%C3%A7%C3%B5es-na-atribui%C3%A7%C3%A3o-das-vari%C3%A1veis-cEmpAnt-e-cUserId
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33541580007447) Tempo aproximado para leitura: 5 minutos  
  
**Ocorrência**  
**A partir das releases 12.1.2510**, foram implementadas restrições na atribuição das variáveis globais **cEmpAnt** e **\_\_cUserId** no contexto de execução no **Protheus**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - a partir da versão 12.1.2510  
  
**Causa**  
As variáveis **cEmpAnt** (grupo de empresa) e **\_\_cUserId** (usuário) eram comumente atribuídas diretamente por desenvolvedores ou integradores para simular ou alterar o contexto de execução de serviços no **Protheus**. No entanto, essa prática oferece riscos de segurança e inconsistência, especialmente em ambientes com múltiplas empresas.  
Com a evolução do Framework e das práticas de segurança, essas variáveis **cEmpAnt** e **\_\_cUserId** não podem mais ser alteradas diretamente em chamadas.

**Importante:** A leitura dessas variáveis é permitida.  
  
**Solução**  
Troca de grupo de empresas ou usuário após abertura inicial.

* **Rotinas em geral:**  
  Mesmo após a autenticação e a preparação do ambiente, não será permitida atribuição diretamente as variáveis **cEmpAnt** ou **\_\_cUserId**.  
  Caso seja necessário verificar ou executar ações em outro grupo de empresas, ou com outro Usuário, a única forma suportada é por meio da função:

  ```
  RPCSetEnv(cRpcEmp, cRpcFil, cEnvUser, cEnvPass, cEnvMod)
  ```

  A chamada da **RPCSetEnv**() deve ser efetuada em uma nova *thread* aberta com as funções **StartJob**, **SmartJob** ou similares, passando os parâmetros corretos no início, respeitando as permissões e licenciamento do usuário e módulo informados.

  **Importante:** Não é recomendado o uso da **RpcSetEnv**() em *threads* de interface, isso pode causar consumo indevido de licenças e até falhas no ERP.

  **Saiba mais detalhes:**  
  [Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função que permite trocar a empresa em tempo de execução](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018521292)  
  <https://tdn.totvs.com/display/public/framework/RpcSetEnv>  
  <https://tdn.totvs.com/display/tec/StartJob>
* **Webservices REST:**  
  A inicialização do ambiente deve ocorrer por meio de autenticação e identificação do ambiente (**empresa/filial**) por meio do *Header* da requisição [**tenantId**].  
  As informações de ambiente e usuário são extraídas com base nesses parâmetros, respeitando a estrutura do serviço.

  **Importante**: Variáveis como **cEmpAnt** e **\_\_cUserId** não podem ser utilizadas para troca de contexto na execução.

  **Saiba mais detalhes no artigo:**  
  [Cross Segmento - TOTVS Backoffice - Linha Protheus - ADVPL - Abertura de ambiente em Web Service](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410465974167)
* **Webservices SOAP:**  
  No caso do **SOAP**, o ambiente é preparado conforme a configuração de **URIs** específicas para cada grupo de empresas, definida no **AppServer.ini**.  
  A diretiva [**PrepareIn**] do **AppServer.ini** é utilizada para configurar a preparação de ambiente para *threads* de execução.

  **Importante:** Como não existe a opção de configuração **PrepareIn=****ALL**, deve ser configurada uma [**HTTPURI**] diferente para cada grupo de empresas, pois o **SOAP** necessita de ambiente especialista por empresa e filial.  
  Variáveis como **cEmpAnt** e **\_\_cUserId** não podem ser utilizadas para troca de contexto na execução.

  **Consulte a documentação completa:**  
  [Configurar Portais e Webservices](https://tdn.totvs.com/display/public/framework/Configurar+Portais+e+Webservices)  
  [PrepareIn Rest - Appserver.ini](https://tdn.totvs.com/pages/releaseview.action?pageId=185747842)  
  [REST com ERP Microsiga Protheus](https://tdn.totvs.com/display/public/framework/02.+REST+com+ERP+Microsiga+Protheus)

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=954597455>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=918398030>
