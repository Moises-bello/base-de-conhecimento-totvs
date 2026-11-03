---
article_id: 33250742421015
category: Escrita Fiscal - Configurador de Tributos
content_hash: 82785bf3f392cd523a8c6991d881a5d6ef516ab89574eef28aa1fa8aced94e12
fetched_at: '2026-06-28T22:39:17.093198+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  FIS - Como Configurar
  uma operação Isenta de ICMS  no Fisa170?
type: support-article
updated_at: '2025-11-14T21:34:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33250742421015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-uma-opera%C3%A7%C3%A3o-Isenta-de-ICMS-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697005463) Tempo aproximado para leitura: 05:00 **min**

**Dúvida**

**Como configurar uma operação Isenta de ICMS no Configurador de Tributos?**

Ambiente:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310

MV\_ESTADO = SP

Cliente = MG

Cadastro de Regra NCM = 84191200

SP para MG - origem = 0 - aliquota = 12%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742394903)

ID tributo

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742395671)

Perfil Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742396183)

Produto deve estar cadastrado no SB1 com origem / NCM preenchidos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697012759)

Perfil Operações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697013783)

Perfil Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742397591)

Perfil origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697014167)

Regra de base de calculo - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697014295)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742398615)

Regra de alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742400279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742402455)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742406551)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742406935)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697016599)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742407959)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742408087)

TES

Gera duplicata = sim

CST = 40

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250742411031)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697018519)

Gravação da SF3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250697018903)
