---
article_id: 360020837511
category: NFe - Nota Fiscal Eletrônica
content_hash: a012dd369876d9c1dea3aae905bf8b2cf39787758d68f6b1f88bf82a6916274f
fetched_at: '2026-06-28T22:40:03.263213+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  660 Rejeição  :
  CFOP de Combustível e não informado grupo de combustível da NF-e'
type: support-article
updated_at: '2025-06-11T12:20:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020837511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-660-Rejei%C3%A7%C3%A3o-CFOP-de-Combust%C3%ADvel-e-n%C3%A3o-informado-grupo-de-combust%C3%ADvel-da-NF-e
---

**Dúvida**

660 rejeição : CFOP de Combustível e não informado grupo de combustível da NF-e

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11545575048087)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11545713741975)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11546411964311)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada MATUCOMP.

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada MATUCOMP, abaixo documentação:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

Ocorre a rejeição 660, pois é **obrigatória** a informação do grupo de combustível para os CFOPs constantes no **Anexo XI.02** - CFOP de Combustível e Lubrificantes (**NT 2012/003**)

Complemento de combustível, para o **XML** a SEFAZ obriga somente 3 tags, **<cProdANP>** (**Código de produto da ANP**), **<UFCons>** (**Sigla da UF de consumo**) e <descANP> (Descrição do produto conforme ANP).

Após isso, **retransmita a nota.**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6793534357527)

Verifique o link abaixo para configurar os novos campos do complemento de combustíveis para o ICMS Monofásico:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2023.001](https://totvssuporte.zendesk.com/knowledge/articles/12928311594903/pt-br?brand_id=1509248)
