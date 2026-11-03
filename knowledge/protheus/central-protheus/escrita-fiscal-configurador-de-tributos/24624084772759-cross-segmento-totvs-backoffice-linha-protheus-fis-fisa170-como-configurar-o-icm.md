---
article_id: 24624084772759
category: Escrita Fiscal - Configurador de Tributos
content_hash: 8a00100976dab0719ba9c6641132b632fbce3871e9c35a4f08af0e0c42abff84
fetched_at: '2026-06-28T22:39:17.428790+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  o ICMS ST pauta e FECP ST separados para vendas internas no DF?
type: support-article
updated_at: '2025-11-14T21:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24624084772759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-ICMS-ST-pauta-e-FECP-ST-separados-para-vendas-internas-no-DF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084677015) Tempo aproximado para leitura: 08:00**min** **Dúvida**Como configurar o ICMS ST pauta e FECP ST separados para vendas internas no DF pelo Configurador de Tributos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Valor da mercadoria = 119,52

Valor da pauta = 171,84

Cálculo

Base de calculo do ICMS = 119,52 \*20% = 23,90

Base de calculo do FECP = 119,52\*2% = 2,39

Base de calculo da ICMS ST Pauta = 171,84 \*20% = 34,37

34,37-23,90 = 10,47

Base de calculo do FECP ST = 171,84\*2% = 3,44

3,44-2,39 = 1,05

Legislação

https://tdn.totvs.com/pages/releaseview.action?pageId=726513846

Configurações

MV\_ESTADO = DF

Cliente = DF

 UF X UF

DF para DF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084678295)

Fisa170

Regras por NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075093655)

Perfil do Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084691223)

Perfil da operação = 000030

Perfil do Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075097623)

Perfil origem / destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084695575)

Regra de Base de calculo do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084698391)

Regra Alíquota do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075104151)

Regra de escrituração do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075105047)

Regra de Calculo - Documentos Fiscais ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084702487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075108375)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075110039)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084705687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084706711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075115287)

FECP do ICMS

A mesma regra de base de calculo

Regra de alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084709527)

Regra de escrituração a mesma do ICMS

Regra de Calculo - Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084710679)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075117975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075118871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075119895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075121047)

Base de Calculo do ICMS ST Pauta

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084715927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084718999)

Regra de Alíquota - 20%

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084719639)

Regra de Calculo - Documentos fiscais - ICMS ST Pauta

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075125527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075126935)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075128471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075130903)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075132695)

Regra de Base de calculo do FECP ST a mesma do ICMS ST Pauta

Regra de Alíquota - 2%

Regra de Escrituração a mesma do FECP ST

Regra de Calculo - Documentos Fiscais - FECP ST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084744087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075135767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075136279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075137559)

TES

Calcula ICMS = não

L fiscal ICMS = não

CFOP = 5403

CST = 10

Agrega valor = sim

Agrega solid. = não

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624075139607)

XML

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624084758551)
