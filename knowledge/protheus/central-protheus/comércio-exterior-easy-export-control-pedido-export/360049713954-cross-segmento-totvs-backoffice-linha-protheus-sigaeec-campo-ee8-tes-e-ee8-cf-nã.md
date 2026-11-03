---
article_id: 360049713954
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 1e5b2ac6a4d39feef321ae6e13ee0f750de67d0aa9b59da348f6d9371cd27b68
fetched_at: '2026-06-28T22:36:58.972180+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC -  Campo EE8_TES  e
  EE8_CF não são exibidos na Tela do Pedido de Exportação
type: support-article
updated_at: '2021-09-22T18:15:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049713954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Campo-EE8-TES-e-EE8-CF-n%C3%A3o-s%C3%A3o-exibidos-na-Tela-do-Pedido-de-Exporta%C3%A7%C3%A3o
---

**Dúvida**

Como apresentar os campo EE8\_TES e EE8\_CF  na tela do Pedido de Exportação?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**

1. Acesse o módulo SIGACFG em Base de Dados, selecione Dicionário / Base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025329791/mceclip0.png)

2. Selecione Dicionário de Dados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025309112/mceclip2.png)

3. Selecione a ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074998854/mceclip7.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025330191/mceclip3.png)

4. Selecione Procurar Por e informe a tabela EE8, após selecione Buscar. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074997694/mceclip0.png)

5. Posicione no camo EE8\_TES e selecione  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074997854/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076207413/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074998054/mceclip3.png)

6. Na Aba Uso, marque o campo como Usado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025310072/mceclip13.png)

7. Na Aba Módulos , marque o campo como Utilizado para todos os módulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025331191/mceclip14.png)

8. Posicione no camoEE8\_CF e selecione  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074997854/mceclip1.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076207573/mceclip4.png)

9. Na Aba Uso, marque o campo como Usado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025310072/mceclip13.png)

10. Na Aba Módulos , marque o campo como Utilizado para todos os módulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025331191/mceclip14.png)

11.  Acesse o módulo SIGACFG  - Ambientes - Cadastros - Parâmetros

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074998594/mceclip5.png)

12.  Parametros e selecione ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074998694/mceclip6.png)Procura por : MV\_EECFAT e ![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074999034/mceclip9.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076208213/mceclip8.png)

13. Selecione  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074997854/mceclip1.png)e habilite o parâmetro MV\_EECFAT = T

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076208333/mceclip10.png)
