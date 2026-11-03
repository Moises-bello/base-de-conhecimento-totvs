---
article_id: 360005005711
category: NFe - Nota Fiscal Eletrônica
content_hash: 2e0de2a0991a281e57791af59778209c61271bb5530c0a705e8513a288c12302
fetched_at: '2026-06-28T22:40:00.068471+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar o
  FECP FCP OU FECOEP no XML e no DANFE
type: support-article
updated_at: '2025-07-28T18:49:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005005711-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-o-FECP-FCP-OU-FECOEP-no-XML-e-no-DANFE
---

**Dúvida**

Como destacar o FECP FCP OU FECOEP no XML e no DANFE ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

No Protheus será apresentada alíquota total :

* **Exemplo: 18 % + 2 % do FCP****(obs: as nomenclaturas da descrição variam de acordo com o Estado esse print é apenas um exemplo)**

**![PLANILHA_FINANCEIRA.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006789912)**

**IMPORTANTE:**

**No sistema é destacado dessa forma, pois no SPEDFISCAL a alíquota é ICMS + FCP**

* **No XML a Sefaz para NFe 4.00 criou as TAGS para o FCP então as alíquotas e valores serão separados:**

**![NT_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006789932)**

**![NT_FECP_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006789952)**

**![XML_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006789972)**

1- Para gerar informação nas TAGS **infAdProd e infAdFisco** habilitar o parâmetro no configurador**MV\_IMPFECP = .T.**

**![mv_impec.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825691)**

2- Exclua a nota e gere novamente.

* **Exemplo:**

**![infadpros.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006790052)**

**![infadfisco.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006790072)**

* **Na impressão do Danfe** será levado apenas alíquota **de 18 % referente ao ICMS sem o FECP e do FCP será levado em descrição do Prod./SERV. e** informações complementares:

**![danfe_fecp.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825731)**

**IMPORTANTE:**

Para a impressão no Danfe do conteúdo gerado na **infAdProd**habilitar o parâmetro no configurador MV\_IMPADIC = .T.

![MV_IMPADIC.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825751)

* **Conforme a nota técnica 2016.002\_v\_1.61 página 76 os valores do FCP devem ser gerados em  informações adicionais do produto e na TAG infadfisco:**

**![FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825851)**

* **Essa informação consta no boletim do TDN:**

[DSERTSS1-68 DT NF-e Implementação da versão 4.00](http://tdn.totvs.com/pages/viewpage.action?pageId=318604074)

**IMPORTANTE:**

Quando houver Difal + FECP não haverá o mesmo destaque, pois, ao calcular o Difal as TAGS são diferentes do previsto na nota técnica:

* **<vBCUFDest>** **Base do FCP**
* **<pFCPUFDest>** **Percentual do FCP**
* **<vFCPUFDest>****Valor do FCP**

**![CD2_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825891)**

**Exemplo Grupo do Difal:**

**![DIFAL_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825911)**

* A única mensagem prevista para esse grupo de **Difal + Fcp** prevista pela Sefaz:

**<infCpl>** Valor do ICMS relativo ao Fundo de Combate a Pobreza - FCP da UF de destino: R$ 20.00. Valor do ICMS  Interestadual para a UF de destino: R$ 48.00. Valor do ICMS Interestadual para a UF do remetente: R$ 12.00.**</infCpl>**

* **Saiba Mais:**

Para **UF do RJ** quando há **D****iferimento com FECP essa regra não se aplica das alíquotas** serem **subtraídas**conforme o parecer da consultoria do link abaixo:

[Diferimento com FECP RJ](https://tdn.totvs.com/pages/releaseview.action?pageId=516211871%20)

* Exemplo do **Diferimento Parcial:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085152953)

* Exemplo do **Diferimento 100 por cento:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083965994)**
