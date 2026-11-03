---
article_id: 360028543032
category: NFe - Nota Fiscal Eletrônica
content_hash: 2d58c78210d9128d79c682086b9250cebb351329e4184255dbf5bcf2bd5f9a02
fetched_at: '2026-06-28T22:40:03.807639+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 233 Rejeição :
  IE do destinatário não cadastrada'
type: support-article
updated_at: '2025-06-18T14:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028543032-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-233-Rejei%C3%A7%C3%A3o-IE-do-destinat%C3%A1rio-n%C3%A3o-cadastrada
---

**Dúvida**Como solucionar a Rejeição 233 : IE do destinatário não cadastrada

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Essa rejeição é um retorno da **Sefaz**, ou seja caso o XML tenha gerado com a **IE** do destinatário correto, será necessário entrar em contato com a Sefaz.

O retorno da Sefaz pode ocorrer, por exemplo quando o destinatário possui uma **IE ISENTA, IE diferente do Sintegra** ou devido à uma inconsistência de Cadastro junto à SEFAZ.

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11722430872983)

Após isso alterar o cadastro de cliente com o IE correto, conforme o link abaixo:

* **Cadastro de Cliente:**

**Contribuinte  indIEDest = 1**

1- Preencha a inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo **Destaca IE*****A1\_IENCONT***  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte** **A1\_CONTRIB** **1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297118999)

**Isento** **indIEDest = 2**

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2-  O campo **Destaca IE *A1\_IENCONT*  em branco**

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte A1\_CONTRIB   1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297118999)

**Não Contribuinte indIEDest = 9**

1- Preencha a inscrição estadual no campo  Ins. Estad. **A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE ***A1\_IENCONT***  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **A1\_CONTRIB**   2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297122327)

* **Cadastro de Fornecedor:**

**indIEDest = 1 Contribuinte**

1- Preencha a inscrição estadual no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896287608087)

2- Preencha o campo ***Contribuinte A2\_CONTRIB=1***

![contribuinte_forn.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297126679)

**Isento** **indIEDest = 2**

1- Deixe em ***branco ou Preencha com literal Isento*** o campo de inscrição estadual no campo  Ins. Estad. **A2\_INSCR**

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896287608087)

2-  O campo Contribuinte **A2\_CONTRIB**   em branco

![ISENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896287611159)  
     ​  
  
     ​  
**Não Contribuinte indIEDest = 9**  
     ​

1- Preencha a inscrição estadual ou deixe em branco no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896287608087)

2-  O campo Contribuinte **A2\_CONTRIB = 2 Não**

**![contrib_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896287614103)**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029540072)

**Contribuinte**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297118999)

**Isento**  
​

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297118999)

**Não Contribuinte**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896297122327)

* **Validação da Sefaz:**

![233_Rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408236582295)
