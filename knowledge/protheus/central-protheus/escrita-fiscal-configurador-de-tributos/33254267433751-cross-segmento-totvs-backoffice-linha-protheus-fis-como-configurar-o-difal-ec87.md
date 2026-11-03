---
article_id: 33254267433751
category: Escrita Fiscal - Configurador de Tributos
content_hash: a261b047537f410116095a5ca5f6ff66ff58dac7c8cbcd0b1184a990d92e9f1e
fetched_at: '2026-06-28T22:39:17.245858+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o DIFAL EC/87 com FECP no FISA170 base simples?
type: support-article
updated_at: '2025-11-04T22:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33254267433751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-DIFAL-EC-87-com-FECP-no-FISA170-base-simples
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267407383) Tempo aproximado para leitura: **00:10min**

**Dúvida**

**Como configurar o DIFAL EC/87 com FECP no FISA170 base simples?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310  
  
**Solução**

MV\_ESTADO = PR

MV\_PPDIFAL = {{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0},{2024,100,0},{2025,100,0}}

Cliente

RJ

Consumidor Final

A1\_CONTRIB = não

TES

CFOP = 5102

gera duplicata = sim

CST = 00

Cálculo

Valor da mercadoria = 1000,00

Base do ICMS = 1000,00\*12% = 120,00

Base do DIFAL EC/87 = 1000,00\*22% = 220,00-120,00= 100,00

Base do FECP = 1000,00\*2% = 20,00

FISA170

Id tributos

ICMS

DIFAL

FCPCMP

Cadastro de Regra de NCM = 40092290

ICMS

PR para RJ = origem = 0 - alíquota de 12%

DIFAL

PR para RJ = origem = 0 - alíquota de 20%

FCPCMP

PR para RJ = origem = 0 - alíquota de 2%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267407895)

Perfil de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267408791)

Perfil de Operações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280972695)

Perfil de Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280973335)

Perfil Origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280973975)

Regra de Base de calculo

ICMS / DIFAL / FCPCMP  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267411095)

Regra de Alíquota

ICMS / DIFAL / FCPCMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267412503)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267412887)

Regra de escrituração

ICMS / DIFAL / FCPCMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280976407)

Regra de Calculo - Documentos Fiscais

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280977687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267414039)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267414551)

DIFAL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280979735)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267415319)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280981527)

FCPCMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280981783)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280982551)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280983063)

Após criar a regra do FECP, alterar o Difal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267418391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267419159)

TES

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267419927)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280987927)

Emissão da Nota fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267421719)

CD2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254280990871)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33254267423767)
