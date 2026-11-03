---
article_id: 360028686011
category: NFe - Nota Fiscal Eletrônica
content_hash: f8a5aeb75bbf47bdea34737663a451fe3363b304164c369a4e88de6400252ba0
fetched_at: '2026-06-28T22:40:03.789984+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 232 Rejeição :
  IE do destinatário não informada'
type: support-article
updated_at: '2025-06-25T12:08:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028686011-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-232-Rejei%C3%A7%C3%A3o-IE-do-destinat%C3%A1rio-n%C3%A3o-informada
---

**Dúvida**Como solucionar a rejeição abaixo ?

232 Rejeição : IE do destinatário não informada  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Essa rejeição é um retorno da **Sefaz**, quando gera a rejeição 232 é necessário destacar a **inscrição estadual** do destinatário no XML.

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11548651723671)

* **Saiba mais**

Segue os campos de cadastro de **IE e CNPJ** no Protheus:

* **Cadastro de Cliente:**

**Contribuinte  indIEDest = 1**

1- Preencha a inscrição estadual no campo  **Ins. Estad.  A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Deixo o conteúdo campo **Destaca IE** - ***A1\_IENCONT***  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte** **A1\_CONTRIB** **1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972034)

**Isento** **indIEDest = 2**

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  **Ins. Estad.  A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2-  O campo **Destaca IE *A1\_IENCONT*  em branco**

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte A1\_CONTRIB   1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972034)

**Não Contribuinte indIEDest = 9**

1- Preencha a inscrição estadual no campo  Ins. Estad.  **A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE ***A1\_IENCONT***  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **A1\_CONTRIB**   2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059973634)

* **Cadastro de Fornecedor:**

**indIEDest = 1 Contribuinte**

1- Preencha a inscrição estadual no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772435922967)

2- Preencha o campo ***Contribuinte A2\_CONTRIB=1***

![contribuinte_forn.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772461471639)

**Isento** **indIEDest = 2**

1- Deixe em ***branco ou Preencha com literal Isento*** o campo de inscrição estadual no campo  Ins. Estad.  **A2\_INSCR**

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772435922967)

2-  O campo Contribuinte **A2\_CONTRIB**   em branco

![ISENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772538123543)  
     ​  
  
     ​  
**Não Contribuinte indIEDest = 9**  
     ​

1- Preencha a inscrição estadual ou deixe em branco no campo  ***Ins. Estad.  A2\_INSCR***

![fornecedor_inst_estadual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772435922967)

2-  O campo Contribuinte **A2\_CONTRIB = 2 Não**

**![contrib_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4772951310615)**

* **Validação da Sefaz:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029099352)

Obs: Em alguns casos é necessário deixar o parâmetro MV\_HISTTAB = .F. para não buscar o histórico de alteração cadastral da tabela AIF.
