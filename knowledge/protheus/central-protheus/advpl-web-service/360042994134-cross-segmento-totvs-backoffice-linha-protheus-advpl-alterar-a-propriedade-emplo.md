---
article_id: 360042994134
category: ADVPL - Web Service
content_hash: cda6516ae8bd0a3fa5698cd9a9ffdadb1247ca24431b5e398319d71a05400fa8
fetched_at: '2026-06-28T22:40:10.149056+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Alterar a propriedade
  employeeNumber via requisição API de usuários  '
type: support-article
updated_at: '2021-05-06T15:03:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042994134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-a-propriedade-employeeNumber-via-requisi%C3%A7%C3%A3o-API-de-usu%C3%A1rios
---

**Dúvida**Não estou conseguindo alterar a propriedade “**employeeNumber**", porém no  **Postman** eu recebo o **200OK.**

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Conforme a documentação este parâmetro diz respeito ao vínculo funcional.

As empresas aos quais o usuário tem acesso não podem ser alteradas via serviço, somente os grupos aos quais ele tem acesso.

Esta regra segue o protocolo **SCIM**.  
 **Saiba Mais**[API TOTVS(user)](https://api.totvs.com.br/apidetails/User_v1_000.json)  
[O serviço Rest users do Protheus (antigo criação de usuários utilizando Webservice REST)](https://tdn.totvs.com/pages/releaseview.action?pageId=274327398)
