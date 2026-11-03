---
article_id: 33258846776727
category: Escrita Fiscal - Configurador de Tributos
content_hash: 852ef3d805abec213b7d3d3dc5fdd87534e277deaa8684934e80727876e92c97
fetched_at: '2026-06-28T22:39:17.130555+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular ICMS
  ST com IPI base dupla Consumidor Final no Fisa170?
type: support-article
updated_at: '2025-11-14T21:57:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33258846776727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-ICMS-ST-com-IPI-base-dupla-Consumidor-Final-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895290647) Tempo aproximado para leitura: 00:10**min**  
**Dúvida**

**Como calcular ICMS ST com IPI base dupla Consumidor Final no Fisa170?**  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310

**Solução**

**Memória de Cálculo**

Valor da mercadoria = 3412,18

Base de calculo do IPI = 3412,18\*6,5% = 221,79

Base de calculo do ICMS = 3412,18+221,79 = 3.633,97 \*12% = 436,06

Base de cálculo do DIFAL ST = 3633,97-436,06 = 3.197,91

3197,91/0,78 = 4099,88

4099,88 \*22% = 901,97-436,06 = 465,91

MV\_ESTADO = SP

Cliente = RJ

Consumidor Final

CFOP

6401

CST = 10

gera duplicata = sim

ID tributo

ICMS

ICMSST

FCPST

IPI

Cadastro de Regra de NCM = 70072900

Origem = 0

ICMS

SP para RJ - alíquota = 12%

IPI

SP para \*\* - alíquota = 6,5%

ICMS ST

SP para RJ - alíquota = 20%

FCPST

SP para RJ - alíquota = 2%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895291287)

Perfil de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846725143)

Cadastro na SB1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846725399)

Perfil de Operações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846726295)

perfil de Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846726935)

Perfil Origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846727575)

Regra de Base de calculo

IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895295383)

Regra de Alíquota

IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895296023)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846729751)

Regra de escrituração

IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895296919)

Regra de Cálculos Documentos Fiscais = 000016

IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846731159)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846731927)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895300247)

Regra Base de Calculo

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895301015)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846733463)

Regra de Alíquota

A mesma

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846736151)

Regra de Calculo - Documentos Fiscais = 000017

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846736791)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846737815)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846739863)

Regra de Base de Calculo - ICMSST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895303063)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846743191)

Regra de Alíquota

a mesma do Cadastro de Regra de NCM

Regra de Alíquota

Alíquota de 22%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846743447)

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895305367)

Regra de Calculo Documentos Fiscais = 000018

ICMSST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895308439)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846744983)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895313047)

Regra de Base de Calculo

FCPST

A mesma do ICMSST

Regra de Alíquota

A mesma

Regra de Escrituração

FCPST

A mesma do ICMSST

Regra de Calculo Documentos Fiscais - FCPST = 000019

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895313943)

SEM REGRA DE ESCRITURAÇÃO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846745879)

Após criar o FCPST , vamos colocar a regra complementar no ICMSST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846746263)

Alterar em detalhamento da formula de calculo - aba tributo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895315863)

TES

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846748311)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258846749591)

Documento de Saídas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895318295)

CD2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895318679)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258895319703)
