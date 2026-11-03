---
article_id: 360029164011
category: NFe - Nota Fiscal Eletrônica
content_hash: 9f0d89444b7be75886ff5472d0f448db9650d6f32686ae00a0c2f1f4e2db344d
fetched_at: '2026-06-28T22:40:05.191859+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 624 Rejeição :
  IE Destinatário não vinculada ao CPF'
type: support-article
updated_at: '2025-06-23T11:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029164011-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-624-Rejei%C3%A7%C3%A3o-IE-Destinat%C3%A1rio-n%C3%A3o-vinculada-ao-CPF
---

**Dúvida**Como solucionar a rejeição abaixo:

624 Rejeição : IE Destinatário não vinculada ao CPF ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Essa rejeição é um retorno da **Sefaz**, ou seja caso o XML tenha gerado com CPF do destinatário correto, será necessário entrar em contato com a Sefaz.

O retorno da Sefaz pode ocorrer, por exemplo quando o destinatário possui uma **IE ISENTA, IE diferente do Sintegra** ou devido à uma inconsistência de Cadastro junto à SEFAZ.

É possível a consulta dos CPF e IE através de alguns sites da Sefaz conforme os links abaixo:

**Cadastro Centralizado de Contribuinte (CCC):**

**<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>**

**![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12381073703703)**

**Sefaz** **RS:**

**<http://www.sefaz.rs.gov.br/consultas/contribuinte>**

**Sefaz** **RJ:**

**<http://www4.fazenda.rj.gov.br/sincad-web/index.jsf>**

**Sefaz** **SP:**

**<https://www.fazenda.sp.gov.br/nfe/empresas/consulta/empresas.asp>**

* **Saiba mais**

Segue os campos de cadastro de **IE e CNPJ** no Protheus:

* **Cadastro de Cliente:**

**Contribuinte  indIEDest = 1**

1- Preencha a inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo **Destaca IE*****A1\_IENCONT***  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte****A1\_CONTRIB** **1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029427735)

**Isento** **indIEDest = 2**

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2-  O campo **Destaca IE *A1\_IENCONT*  em branco**

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte A1\_CONTRIB   1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029427735)

**Não Contribuinte indIEDest = 9**

1- Preencha a inscrição estadual no campo  Ins. Estad. **A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE***A1\_IENCONT***  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte**A1\_CONTRIB**   2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986022562071)

* **Cadastro de Fornecedor:**

**indIEDest = 1 Contribuinte**

1- Preencha a inscrição estadual no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029428119)

2- Preencha o campo ***Contribuinte A2\_CONTRIB=1***

![contribuinte_forn.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986022566167)

**Isento** **indIEDest = 2**

1- Deixe em ***branco ou Preencha com literal Isento*** o campo de inscrição estadual no campo  Ins. Estad. **A2\_INSCR**

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029428119)

2-  O campo Contribuinte**A2\_CONTRIB**   em branco

![ISENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029433367)  
     ​  
  
     ​  
**Não Contribuinte indIEDest = 9**  
     ​

1- Preencha a inscrição estadual ou deixe em branco no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986029428119)

2-  O campo Contribuinte**A2\_CONTRIB = 2 Não**

**![contrib_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986022567063)**

* **Validação da Sefaz:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030252052)
