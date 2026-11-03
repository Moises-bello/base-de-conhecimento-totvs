---
article_id: 360034359093
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 70ec17f3d3df74a67afb3e83de6ed16fa14fa394bdf46a6647e128b3e0dfffbe
fetched_at: '2026-06-28T22:39:48.684172+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  Erro "DBCreateIndex
  Create index file error " ao Incluir Manutenção de Embarque.
type: support-article
updated_at: '2021-12-27T13:05:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034359093-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-DBCreateIndex-Create-index-file-error-ao-Incluir-Manuten%C3%A7%C3%A3o-de-Embarque
---

**Dúvida**Como corrigir o erro "Create index file error " ao Incluir Manutenção de Embarque ?  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**1 .Acesse o Configurador - Base de Dados - Dicionário - Base de Dados

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574094/mceclip0.png)

2. Em Dicionario de dados selecione a ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043462814/mceclip2.png).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044424613/mceclip1.png)  
  
3. Procurar por **EIM** ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574354/mceclip3.png) e selecione ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574434/mceclip4.png).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044424673/mceclip2.png)

4. Selecione ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574694/mceclip6.png)   .

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425133/mceclip5.png)

5. Selecione ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425253/mceclip7.png) no indices e alterar o campo **IX\_VIRCUST,** alterando para "**3 - Padrão do Sistema"** para todos os indices da tabela.

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425373/mceclip8.png)**

6. Após alteração, selecione Campos

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425633/mceclip10.png)**

7. Posicione no campo **EIM\_HAWB** e selecione ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043575194/mceclip12.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425793/mceclip11.png)

8. Marque o campo **EIM\_HAWB** como USADO na Aba Uso e Utilizado para todos os módulos na Aba Módulos. 

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425913/mceclip13.png)  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425973/mceclip14.png)  
  
Após essas alterações realize o procedimento novamente.
