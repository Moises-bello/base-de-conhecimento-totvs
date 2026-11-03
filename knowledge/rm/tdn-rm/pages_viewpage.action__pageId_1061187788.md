---
content_hash: e10d004642922cb0c514ae8cc1253fa75205e0f0e65bde3869ebd806443ea929
fetched_at: '2026-06-29T00:05:52.900068+00:00'
page_id: '1061187788'
product: rm
source: tdn-rm
title: URLs utilizadas para ambiente de homologação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1061187788
version: 3
---

# **Índice**

---

2Índice

# **Objetivo**

---

Este documento lista as URLs utilizadas pelo RM em ambiente de **homologação** na integração com o SmartLink, sendo necessário permitir o acesso a esses endpoints para o correto funcionamento da integração.

# **URLs**

---

## **URLs do SmartLink com *wildcards***

Se for possível utilizar *wildcards* para liberar as rotas, basta utilizar as rotas abaixo:

* **Rotas do ambiente de homologação**: https://\*.staging.totvs.app
* **Rotas da Carol**: [https://app.carol.ai](https://app.carol.ai/)

## **URLs do SmartLink sem *wildcards***

Caso a utilização de wildcards não seja possível, é necessária a liberação de rotas individualmente:

### **URLs básicas**

* **Lista de URLs (Discovery):** [https://endpoint-registry.staging.totvs.app/api/v1/services](https://endpoint-registry.totvs.app/api/v1/services)
* **Autenticação**: [https://admin.rac.](https://admin.rac.totvs.app/totvs.rac/connect/token)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app/totvs.rac/connect/token](https://admin.rac.totvs.app/totvs.rac/connect/token)
* **Integração:** [https://credentialhelper.](https://credentialhelper.totvs.app)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app](https://credentialhelper.totvs.app)
* **API de Integração:** [https://api-credentialhelper.](https://api-credentialhelper.totvs.app/)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app](https://api-credentialhelper.totvs.app/)

### **Upstream Data Sharing**

* **Lista de entidades**: [https://provisioning.](https://provisioning.totvs.app/api/carol-definitions/v1/entities)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app/api/carol-definitions/v1/entities](https://provisioning.totvs.app/api/carol-definitions/v1/entities)
* **Ingestão de dados**: [https://ingestion-smartlink.](https://ingestion-smartlink.totvs.app/)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app](https://ingestion-smartlink.totvs.app/)
* **Carol (v1):**[https://app.carol.ai](https://app.carol.ai/)
* **Credenciais (v1)**: [https://provisioning.](https://provisioning.totvs.app/api/carol-definitions/v1/carolcredentials)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app/api/carol-definitions/v1/carolcredentials](https://provisioning.totvs.app/api/carol-definitions/v1/carolcredentials)

### **Behavior Sharing**

* **Link:** [https://link.](https://link.totvs.app/)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app](https://link.totvs.app/)
* **API**: [https://api-smartlink.](https://api-smartlink.totvs.app/)[staging.](https://endpoint-registry.totvs.app/api/v1/services)[totvs.app](https://api-smartlink.totvs.app/)

## **Login OIDC**

* **Rotas**:
  + [https://accounts.staging.totvs.app](https://accounts.totvs.app)
  + [https://api-fluig.staging.totvs.app](https://api-fluig.totvs.app)
  + <https://app.customerfi.com>

Atenção

Além do domínio principal do **Identity**,é necessário realizar a liberação do seu **domínio do tenant**, pois é ele que o RM utiliza internamente.

Ao acessar o **Identity**, é possível identificar o **domínio do tenant** diretamente pela URL exibida no navegador.

* https://**SEUTENANT**.customerfi.com
Atenção

Caso o ambiente utilizado seja o **Identity de homologação**, será necessário possuir um ambiente de **License Server de homologação** e realizar alguns ajustes no **ERP (RM)**:

1. Configurar o ambiente com um License Server de homologação nos Parâmetros Globais;
2. Executar o seguinte update no banco de dados:

   sqlUpdate

Após seguir estes passos, é necessário reiniciar o serviço do Host.
