---
article_id: 4848554492439
category: Materiais - Compras (SIGACOM)
content_hash: 3d7ee8db54b11edc34515d3403725a86a890c5be2863e5f3a35d2518617761fa
fetched_at: '2026-06-28T22:41:11.614452+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como o Documento
  de Entrada verifica o Parâmetro MV_DATAFIN ?
type: support-article
updated_at: '2022-10-26T11:19:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4848554492439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Como-o-Documento-de-Entrada-verifica-o-Par%C3%A2metro-MV-DATAFIN
---

**Dúvida** **Como o documento de entrada verifica o parâmetro MV\_DATAFIN ?**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – A partir da versão 11.80  
  
**Solução**A rotina do documento de entrada ( **MATA103** ), verifica o conteúdo do parâmetro [**MV\_DATAFIN**](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=514730929), da seguinte forma :

O sistema procura pelo parâmetro **MV\_NFDTFIN ( parâmetro que determina como deve ser verificado o conteúdo do MV\_DATAFIN, se 1 pela data base do sistema ou se 2 pela data de emissão da nota )**

Quando o sistema não localiza dentro da SX6 esse parâmetro ele assume que o conteúdo é 1, ou seja, ele valida se a data base do sistema, está superior a data que consta no MV\_DATAFIN.

Para as situações onde é necessário que a data de emissão da nota seja verificada, é necessário que no **MV\_NFDTFIN esteja o conteúdo =2.**

Caso dentro da SX6 o parâmetro não exista, é possível criá-lo de forma manual. Abaixo os prints :

Acesse o Configurador -> Ambiente -> Cadastros -> Parâmetros -> Incluir

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848274766615/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848284699415/mceclip2.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848202030871/mceclip0.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848323617303/mceclip3.png)

*Considerando o exemplo abaixo :*

**MV\_DATAFIN**fechado em 31012022

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848353928343/mceclip4.png)**MV\_NFDTFIN = 2**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848390979095/mceclip5.png)**

Data base do sistema : **18.03.2022**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848422834967/mceclip6.png)**

Incluindo um documento de entrada, cuja data de **emissão é 15.01.2022**, ou seja, menor que a data que está no **MV\_DATAFIN**.

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848486988695/Sem_t_tulo.png)

Ao salvar o documento o sistema valida o conteúdo do MV\_DATAFIN e não permite a inclusão da nota de entrada.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848532195607/mceclip8.png)

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
