---
article_id: 360036551414
category: Escrita Fiscal - CIAP
content_hash: e69a6361c553eeebe2a1c4f75e194ac263719a3a68a90af7681447c648a2bec1
fetched_at: '2026-06-28T22:39:34.013791+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: Entrada com Ativo - Desmembrando quantidades em itens
type: support-article
updated_at: '2025-02-04T19:08:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036551414-Entrada-com-Ativo-Desmembrando-quantidades-em-itens
---

**Dúvida**

Como utilizar o campo Desmem. IT. ATF. (F4\_BENSATF) em Nota Fiscal Entrada?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Informe no **Cadastro do TES** na aba Adm/Fin/custo no campo Desmem. IT. ATF. (F4\_BENSATF)

Indica se desmembra os item gerados no  
Ativo Fixo a partir da NF. Se igual a  
SIM, quando for lançado um item com  
quantidade 10 na NF, será gerado 10  
itens com quantidade igual a 1 no Ativo  
Fixo, se igual a NAO será gerado apenas  
1 item com quantidade igual a 10. Este  
parâmetro só terá efeito se o campo  
"Atual.Ativo "F4\_ATUATF" for igual a  
SIM.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047843414/mceclip0.png)
