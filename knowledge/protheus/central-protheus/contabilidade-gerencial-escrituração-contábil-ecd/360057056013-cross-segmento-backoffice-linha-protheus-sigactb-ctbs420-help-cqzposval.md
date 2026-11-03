---
article_id: 360057056013
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 551060ad85d5f4a92efba7bc1cfb771e1c54b574186e84ef354e99f1ba8c9377
fetched_at: '2026-06-28T22:40:44.280092+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS420 Help: CQZPOSVAL '
type: support-article
updated_at: '2021-08-31T17:52:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057056013-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS420-Help-CQZPOSVAL
---

**Ocorrência**

Help : CQZPOSVAL

Problema : O valor do campo [Valor Elim.](CQY\_VLRELI)K310.não coincide com o total informado no painel [Registro K315:Empresas Contrapartes das Parcelas do Valor Eliminado Total].

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095603493/mceclip0.png)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade – A partir da versão P12

**Causa**

Ao incluir o Bloco diretamente no PGE veja :

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344294/mceclip1.png)

* K100

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344334/mceclip2.png)

* K110

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344354/mceclip3.png)

* K115

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095603833/mceclip4.png)

* K200

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095603873/mceclip5.png)

* K210

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344394/mceclip6.png)

* K300

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344414/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344454/mceclip8.png)

* K315

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093344474/mceclip9.png)

* Ao validar o arquivo apresentou o mesmo erro
* O Somatório das Parcelas da Contrapartida do Valor Eliminado Total (Registro K315) deve coincidir com o valor com o valor da Parcela do Valor Eliminado Total( Registro K310) , com sinal invertido

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095604013/mceclip10.png)

* Diante disso necessário verificar junto ao manual da receita a forma correta para lançar o bloco K

Veja também :

[Geração do Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050375913-MP-SIGACTB-ECD-Gera%C3%A7%C3%A3o-do-Bloco-K-?source=search)
