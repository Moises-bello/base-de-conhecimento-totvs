---
article_id: 39473914475159
category: Escrita Fiscal - Configurador de Tributos
content_hash: a3823b1d76c565bac84c3504918a34d81c566ed1821fe92b5d86609feba4634d
fetched_at: '2026-06-28T22:39:17.156934+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular o
  Difal ec/87 base dupla no fisa170 com IBS/CBS ?
type: support-article
updated_at: '2026-04-02T15:48:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39473914475159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-Difal-ec-87-base-dupla-no-fisa170-com-IBS-CBS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914378903) Tempo aproximado para leitura:10:00mm  
  
**Dúvida**  
 Como calcular o Difal ec/87 base dupla no fisa170 com IBS/CBS ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Segue o exemplo de calculo de venda a consumidor final com base dupla para o Difal EC/87.

Venda de SP para MG

Valor da mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\*12% = 120,00

Base de calculo do DIFAL EC/87 = 1000,00-120,00= 880,00

880,00/0,82 = 1.073,17

1073,17\*18% = 193,17-120,00= 73,17

Base de calculo PIS/COFINS = 1000,00-120,00 = 880,00

PIS - 880,00\*1,65% = 14,52

COF - 880,00\*7,6% = 66,88

Base de calculo IBS/CBS = 1000,00-120,00-73,17-14,52-66,88 = 725,43

725,43\*0,10= 0,73

725,43\*0,90= 6,53

Parâmetros

MV\_Estado = SP

Cliente = MG

Tipo de cliente = Consumidor Final

TES

CFOP = 6108

ID tributos

ICMS  
DIFAL

PIS

COF

IBSEST

CBSFED

Regra de NCM = 3926.90.90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898561431)

Regra de base de calculo - ICMS

O:VAL\_mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914384791)

Regra de alíquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898567703)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914388759)

#### Regra de escrituração

Incidência = tributada

CST = 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898575127)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898577815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914398359)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914400023)

Perfil - Todas as UFS

Perfil participantes - TODOS

Perfil Operações - 6108

Perfil Produtos - 000027

ICMS00>

<orig>**0**</orig>

<CST>**00**</CST>

<modBC>**3**</modBC>

<vBC>**1000.00**</vBC>

<pICMS>**12.0000**</pICMS>

<vICMS>**120.00**</vICMS>

</ICMS00>

</ICMS>

**Regra de Base de calculo DIFAL**

( O:VAL\_mercadoria - VAL:icms ) / ( 1 - alíquota de 18% /100 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914402711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914404631)

Regra de alíquota

I:ALIQ\_NCM

Regra de escrituração

Incidência = tributado

CST = 00

Regra de Calculo Documentos fiscais - DIFAL

Aba detalhamento da formula de calculo/ Aba tributado

( base \* alíquota ) - Val: valor do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898595607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898598551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898600727)

Perfil Origem x destino = SP para MG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914411671)

<ICMSUFDest>

<vBCUFDest>**1073.17**</vBCUFDest>

<vBCFCPUFDest>**1073.17**</vBCFCPUFDest>

<pFCPUFDest>**0**</pFCPUFDest>

<pICMSUFDest>**18.0000**</pICMSUFDest>

<pICMSInter>**12.00**</pICMSInter>

<pICMSInterPart>**100**</pICMSInterPart>

<vFCPUFDest>**0**</vFCPUFDest>

<vICMSUFDest>**73.17**</vICMSUFDest>

<vICMSUFRemet>**0**</vICMSUFRemet>

</ICMSUFDest>

**Regra de Base de calculo do PIS/COFINS**

(O:val\_mercadoria - Val:icms )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898603159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898604823)

Regra de Alíquota

I:ALIQ\_NCM

Regra de escrituração do PIS

Incidência = tributado

CST = 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898606103)

Regra de escrituração do COFINS

Incidência = tributado

CST = 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898607895)

Regra de Calculo Documentos Fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898609175)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898613143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914421271)

Regra de Calculo Documentos Fiscais - COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914422295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898616599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898619671)

PIS>

<PISAliq>

<CST>**01**</CST>

<vBC>**880.00**</vBC>

<pPIS>**1.6500**</pPIS>

<vPIS>**14.52**</vPIS>

</PISAliq>

</PIS>

<COFINS>

<COFINSAliq>

<CST>**01**</CST>

<vBC>**880.00**</vBC>

<pCOFINS>**7.6000**</pCOFINS>

<vCOFINS>**66.88**</vCOFINS>

</COFINSAliq>

</COFINS>

**Regra de Base de Calculo - IBS/CBS**

( O:Val\_mercadoria - VAL:icms - VAL:difal - VAL:pis - VAL:cofins )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898620951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898622231)

Regra de alíquota - IBSEST

Informada = 0,10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914428311)

Regra de alíquota - CBSFED

Informada = 0,90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898625559)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914433175)

Regra de Calculo Documentos Fiscais - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473898627735)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914437399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914439831)

Regra de Calculo Documentos Fiscais - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914443287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914445207)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914446231)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914447895)

IBSCBS>

<CST>**000**</CST>

<cClassTrib>**000001**</cClassTrib>

<gIBSCBS>

<vBC>**725.43**</vBC>

<gIBSUF>

<pIBSUF>**0.1000**</pIBSUF>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vIBSUF>**0.73**</vIBSUF>

</gIBSUF>

<vIBS>**0.73**</vIBS>

<gCBS>

<pCBS>**0.9000**</pCBS>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vCBS>**6.53**</vCBS>

</gCBS>

</gIBSCBS>

</IBSCBS>

</imposto>

<vItem>**1000.00**</vItem>

Gravação dos impostos na CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473914449175)

Atualização do TSS conforme documentação

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)
