---
article_id: 34900941734807
category: Escrita Fiscal - Configurador de Tributos
content_hash: b7c75e7c6a201a1cc59e61260b9a16cabb6f3b680bb34e0159c2a68294555a61
fetched_at: '2026-06-28T22:39:17.736098+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular
  Diferencial de alíquotas nas entradas base dupla para RJ?
type: support-article
updated_at: '2025-09-12T21:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34900941734807-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-Diferencial-de-al%C3%ADquotas-nas-entradas-base-dupla-para-RJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34900941709207) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Como calcular Diferencial de aliquotas nas entradas base dupla para RJ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
MV\_ESTADO = RJ

Fornecedor = SP

Valor da mercadoria = 250,00

base de calculo do icms = 250,00\*12% = 30,00

base de cálculo do diferencial de alíquotas = 282,05\*22% = 32,05

Base de calculo do fecp = 282,05\*2% = 5,64

RJ700000002 - Diferencial de aliquotas sobre material de consumo = 26,41

RJ700000006- Fecp sobre diferencial de aliquotas = 5,64

TES

CFOP = 2556

Material de consumo = sim

Gera duplicata = sim

ID tributos

ICMS

CMP

FCPCMP

Perfis

Perfil de Produto = 000010

000041

Perfil de Operação = 100001

CFOP = 2556

Perfil de Participantes = 000001

Todos os fornecedores

Perfil Origem x Destino = 000004

SP para RJ

Regra de Base de calculo ICMS

O:Valor \_mercadoria

Regra de Base de calculo CMP

( O:VAL\_MERCADORIA -  VAL:800001 ) / ( 1 - A:000026 / 100 )

Regra de Base de calculo FCP CMP

a mesma base

Regra de Aliquota ICMS

12%

Regra de Aliquota CMP

20%

Regra de Aliquota FCPCMP

2%

Regra de aliquota para majoração

22%

Regra de escrituração ICMS

CST = 90

Incidencia = outros

Regra de escrituração CMP

a mesma do icms

Regra de escrituração FCPCMP

sem regra de escrituração, pois será agregado junto com o CMP

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900941709975)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919340951)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919343127)

Regra de Calculo Documentos Fiscais - CMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919346327)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919347351)

Perfis os mesmos

Regra de Calculo Documentos Fiscais - FCPCMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919348247)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900941715991)

Perfis os mesmos

Alterar o CMP

Após criar a regra de calculo do FECP, acrescentar como majorado na regra do CMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900941716247)

Aba detalhamento da formula de calculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919350039)

Lançamento da nota fiscal de entradas com calculo do ICMS / CMP / FCPCMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900941717655)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900919351063)

O diferencial de alíquotas continua sendo gravado no campo F3\_ICMSCOM e FECP F3\_VFCPDIF

Boletins

FECP

<https://tdn.totvs.com/pages/releaseview.action?pageId=701693062>

CMP

<https://tdn.totvs.com/pages/releaseview.action?pageId=717702574>
