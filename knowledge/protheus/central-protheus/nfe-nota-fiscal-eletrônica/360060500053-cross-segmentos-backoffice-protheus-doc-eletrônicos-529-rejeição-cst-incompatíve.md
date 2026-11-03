---
article_id: 360060500053
category: NFe - Nota Fiscal Eletrônica
content_hash: d998b5e521f5f4484df3f59bfc81c7a7993d155fad43ac9a5513c4a45e1732d6
fetched_at: '2026-06-28T22:40:01.476585+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 529  Rejeição:
  CST incompatível na operação com Contribuinte Isento de Inscrição Estadual'
type: support-article
updated_at: '2021-09-09T20:39:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060500053--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-529-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual
---

**Dúvida**Como corrigir a rejeição abaixo:

529 Rejeição: CST incompatível na operação com Contribuinte Isento de Inscrição Estadual ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Se gerado no XML a TAG  ***indIEDest = 2,* conforme o exemplo abaixo:**

**![indiedest.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099067314/indiedest.png)**

A ***SEFAZ - Secretaria da Fazenda*** não aceita o ***CST***  do ICMS seja ***50 e 51*** para operação com ***Contribuinte Isento de Inscrição Estadual.***

1- Caso o ***contribuinte seja Isento***, altere a situação tributária do ICMS no campo ***Sit. trib. ICMS "F4\_SITTRIB"*** para **00, 10, 20, 30, 40, 41, 60, 70 ou 90.**

![20201208_114124.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101299453/20201208_114124.gif)

2- Se a situação tributária do ***ICMS 50 ou 51 estiver correta,*** altere o ***destinatário para Contribuinte ou Não contribuinte.***

**Contribuinte**

**![mceclip4.png](https://totvssuporte.zendesk.com/hc/article_attachments/360059972554/mceclip4.png)**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE**"A1\_IECONT"** em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte**"A1\_CONTRIB"** 1- Sim

![mceclip2.png](https://totvssuporte.zendesk.com/hc/article_attachments/360059972034/mceclip2.png)

**Não Contribuinte**

![mceclip0.png](https://totvssuporte.zendesk.com/hc/article_attachments/360059971394/mceclip0.png)

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE**"A1\_IECONT"** 1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte**"A1\_CONTRIB"** 2 - Não

![mceclip5.png](https://totvssuporte.zendesk.com/hc/article_attachments/360059973634/mceclip5.png)

3- Após isso, ***exclua a nota e gere novamente.***

* **Saiba mais:**

* ***Exceção 1:*** A regra de validação acima não se aplica para o CST=50Suspensão, nas operações com CFOP de conserto ou reparo (CFOP 1915, 1916, 2915, 2916, 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 1912, 1913, 5912 e 5913)
* Remessa para Industrialização por encomenda (1901, 2901, 5901 e 6901).

* ***Exceção 2:*** A regra de validação acima não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016.

* ***Exceção 3:*** A critério da UF, a regra de validação acima não se aplica para CST=51-Diferimento em operações internas (idDest=1) quando o destinatário for Pessoa Jurídica (tag:dest/CNPJ).

* **Exceção 4:** Esta regra não se aplica na emissão da NFA-e nas operações internas, a critério da UF.

* **Validação da Sefaz:**

![529_Rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408184169495/529_Rejei__o.JPG)
