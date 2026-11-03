---
article_id: 8997492248343
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b0c417205ad42f926295648f1689b879733e7385414a6ee2b83fce435347983c
fetched_at: '2026-06-28T22:42:00.896460+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Bloco G não
  gera quando não há saídas tributadas no período.
type: support-article
updated_at: '2022-09-20T12:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8997492248343-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Bloco-G-n%C3%A3o-gera-quando-n%C3%A3o-h%C3%A1-sa%C3%ADdas-tributadas-no-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Ocorrência**Quando não há saídas tributadas no período, de forma que **não há apropriação do crédito**, o **bloco G** não é gerado pelo **Protheus**.  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Causa**

O **bloco G** não é gerado quando não há saídas tributadas no período, porque entende-se que nesse cenário **não há direito ao crédito**. Dessa forma, no mês em que não houver **ICMS Tributado**, o contribuinte ficará  sem direito ao valor da fração daquele mês e impossibilitado de recuperar este valor. 

Abaixo, segue parecer da nossa consultoria de segmentos acerca do tema:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525800597>

**Solução**Nesse cenário é gerado o **bloco G** apenas com os registros de abertura **G001** com o campo **02 - IND\_MOV** como **1 - Bloco sem dados Informados** e de encerramento **G990**.

Para que o **Protheus** entenda que em determinado período não houve direito ao crédito, mas que no mês posterior haverá apropriação normalmente, apenas pulando a parcela perdida é preciso realizar o processo do link abaixo quanto ao **CIAP**.

<https://totvssuporte.zendesk.com/knowledge/articles/360028699051/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F3600286>

Em seguida deve ser gerado o **Sped Fiscal** com **bloco G.**

Abaixo, exemplo de um **CIAP** que teve duas parcelas apropriadas e no terceiro mês não houveram saídas tributadas:

**Mês 01 - Apropriação da primeira parcela**

![](https://totvssuporte.zendesk.com/attachments/token/1pWh7FBSsrFhsVV26coVyYTMi/?name=image.png)

**Mês 02 - Apropriação da segunda parcela:**

![](https://totvssuporte.zendesk.com/attachments/token/rigtJWtEZx0J9UpHRdWkyvAUY/?name=image.png)

**Mês 03 - Não houveram saídas tributadas**

![](https://totvssuporte.zendesk.com/attachments/token/eCioePe5GpxZhe9JQkuYMGjlX/?name=image.png)

**Mês 04 - Apropriação da quarta parcela**

![](https://totvssuporte.zendesk.com/attachments/token/JRbyga31lYtX940nAE2mnUklL/?name=image.png)
