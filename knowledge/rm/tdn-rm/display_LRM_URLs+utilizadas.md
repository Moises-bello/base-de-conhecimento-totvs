---
content_hash: 07f4389f382849190ab756d9dcf440fc5983bc0d34d6134ef3b583313010e1f9
fetched_at: '2026-06-29T00:05:52.802996+00:00'
page_id: '1060231153'
product: rm
source: tdn-rm
title: URLs utilizadas
type: documentation
url: https://tdn.totvs.com/display/LRM/URLs+utilizadas
version: 12
---

# **Índice**

---

2Índice

# **Objetivo**

---

Este documento lista as URLs utilizadas pelo ERP no consumo da integração com o SmartLink, sendo necessário permitir o acesso a esses endpoints para o correto funcionamento da integração.

Ressalta-se que essas URLs são de uso interno da integração entre o ERP e o SmartLink, não sendo necessário — e nem esperado — que o cliente realize chamadas diretas a esses endpoints fora deste contexto.

Caso esteja sendo utilizado um ambiente de homologação, seguir a seguinte *documentação: **[URLs utilizadas para ambiente de homologação](https://tdn.totvs.com/x/zHBAPw)***.

# **URLs**

---

## **URLs do SmartLink com *wildcards***

Se for possível utilizar *wildcards* para liberar as rotas, para a integração com o SmartLink basta utilizar as rotas abaixo:

* **Rotas do SmartLink**: https://\*.totvs.app
* **Rotas da Carol**: [https://app.carol.ai](https://app.carol.ai/)

## **URLs do SmartLink sem *wildcards***

Caso a utilização de wildcards não seja possível, é necessária a liberação de rotas individualmente:

### **URLs básicas**

* **Lista de URLs (Discovery):** <https://endpoint-registry.totvs.app/api/v1/services>
* **Autenticação**: <https://admin.rac.totvs.app/totvs.rac/connect/token>
* **Integração:** <https://credentialhelper.totvs.app>
* **API de Integração:** [https://api-credentialhelper.totvs.app](https://api-credentialhelper.totvs.app/)

### **Upstream Data Sharing**

* **Lista de entidades**: <https://provisioning.totvs.app/api/carol-definitions/v1/entities>
* **Ingestão de dados**: [https://ingestion-smartlink.totvs.app](https://ingestion-smartlink.totvs.app/)
* **Carol (v1):**[https://app.carol.ai](https://app.carol.ai/)
* **Credenciais (v1)**: <https://provisioning.totvs.app/api/carol-definitions/v1/carolcredentials>

### **Behavior Sharing**

* **Link:** [https://link.totvs.app](https://link.totvs.app/)
* **API**: [https://api-smartlink.totvs.app](https://api-smartlink.totvs.app/)

## **Login OIDC**

Rotas necessárias para o login OIDC:

* <https://accounts.totvs.app>
* <https://api-fluig.totvs.app>
* <https://app.fluigidentity.com>

Atenção

Além do domínio principal do **Identity**, é necessário realizar a liberação do seu **domínio do tenant**, pois é ele que o ERP utiliza internamente.

Ao acessar o **Identity**, é possível identificar o **domínio do tenant** diretamente pela URL exibida no navegador:

* [https://***SEUTENANT***.fluigidentity.com](https://SEUTENANT.fluigidentity.com)

## **Verificação de conexão com a internet**

O SmartLink utiliza o mecanismo de requisições HTTP a endpoints generate\_204, amplamente utilizados para validação de conectividade à internet, inclusive em sistemas operacionais e dispositivos móveis.  
Esses endpoints retornam HTTP 204 (No Content), sem payload, garantindo:

* + Baixo custo de rede
  + Segurança (nenhum dado sensível trafegado)
  + Alta confiabilidade para o cenário de conectividade

**Dessa forma, é obrigatório que pelo menos um desses *endpoints* esteja com acesso liberado pelo firewall.**

Os seguintes endpoints serão utilizados como providers de verificação:

* + <http://google.com/generate_204>
  + <http://gstatic.com/generate_204>
  + <http://clients3.google.com/generate_204>
  + <http://cp.cloudflare.com/generate_204>
  + <http://edge-http.microsoft.com/captiveportal/generate_204>

Se pelo menos um *endpoint* desta lista estiver liberado, ativo e com resposta bem sucedida, será considerado que existe conectividade ativa com a internet e a integração será processada.

Caso algum esteja bloqueado ou fora do ar, outro será utilizado para verificação.

Caso todos estejam bloqueados, será entendido que não existe conexão com a internet, a integração será interrompida e será aguardado o próximo pooling para realizar uma nova verificação.
