---
article_id: 360028342292
category: NFe - Nota Fiscal Eletrônica
content_hash: 5c736b363247db3a7e80c4600b89bce079f038114eea968e885be295cac55fff
fetched_at: '2026-06-28T22:40:03.853920+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 306 Rejeição :
  IE do destinatário não está ativa na UF'
type: support-article
updated_at: '2025-06-23T11:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028342292-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-306-Rejei%C3%A7%C3%A3o-IE-do-destinat%C3%A1rio-n%C3%A3o-est%C3%A1-ativa-na-UF
---

**Dúvida**

Como solucionar a rejeição abaixo ?

Rejeição: 306 IE do destinatário não está ativa na UF

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Essa rejeição é um retorno da **Sefaz**, ou seja caso o XML tenha gerado com a **IE** do destinatário correto, será necessário entrar em contato com a Sefaz.

O retorno da Sefaz pode ocorrer, por exemplo quando o destinatário possui uma **IE ISENTA, IE diferente do Sintegra** ou devido à uma inconsistência de Cadastro junto à SEFAZ.

É possível a consulta dos CNPJ e IE através de alguns sites da Sefaz conforme os links abaixo:

**Cadastro Centralizado de Contribuinte (CCC):**

**<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>**

**![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12388781280535)**

* **Cadastro de Cliente:**

**Contribuinte  indIEDest = 1**

1- Preencha a inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo **Destaca IE** ***A1\_IENCONT***  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte****A1\_CONTRIB** **1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877668887)

**Isento** **indIEDest = 2**

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2-  O campo **Destaca IE *A1\_IENCONT*  em branco**

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte A1\_CONTRIB   1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877668887)

**Não Contribuinte indIEDest = 9**

1- Preencha a inscrição estadual no campo  Ins. Estad. **A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE ***A1\_IENCONT***  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **A1\_CONTRIB**   2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877672855)

* **Cadastro de Fornecedor:**

**indIEDest = 1 Contribuinte**

1- Preencha a inscrição estadual no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877678743)

2- Preencha o campo ***Contribuinte A2\_CONTRIB=1***

![contribuinte_forn.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499837668887)

**Isento** **indIEDest = 2**

1- Deixe em ***branco ou Preencha com literal Isento*** o campo de inscrição estadual no campo  Ins. Estad. **A2\_INSCR**

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877678743)

2-  O campo Contribuinte **A2\_CONTRIB**   em branco

![ISENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877702295)  
     ​  
  
     ​  
**Não Contribuinte indIEDest = 9**  
     ​

1- Preencha a inscrição estadual ou deixe em branco no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877678743)

2-  O campo Contribuinte **A2\_CONTRIB = 2 Não**

**![contrib_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23499877713815)**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12389085905943)
