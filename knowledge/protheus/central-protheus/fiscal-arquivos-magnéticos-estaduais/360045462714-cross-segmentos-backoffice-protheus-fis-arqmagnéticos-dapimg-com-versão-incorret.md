---
article_id: 360045462714
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: df6cb2f84a93989a1fcd9816ee2600ddd7d843fe8c87f8bd79c850398d1fe187
fetched_at: '2026-06-28T22:42:11.873571+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos- DAPIMG COM VERSÃO
  INCORRETA
type: support-article
updated_at: '2022-08-18T14:16:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045462714-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DAPIMG-COM-VERS%C3%83O-INCORRETA
---

**Dúvida**Estou gerando o arquivo da DAPIMG, porém está gerando com a versão incorreta: 1.00.00

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063521294/mceclip2.png)

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80

**Solução**Identificado o problema esta no validador da DAPIMG.  
  
Na tela principal do validador o campo: **Consistir** não valida a versão da DAPIMG, ao importar o arquivo gerado pelo Protheus.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064507593/mceclip3.png)

Mas por dentro da apuração, ao clicar no mesmo botão **Consistir** ele faz a validação da versão alterando para correta.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064502793/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063521054/mceclip0.png)
