---
article_id: 17802352397591
category: Escrita Fiscal - Configurador de Tributos
content_hash: 0e5b54843742babf44897372148bae8ee729024bc7a27d44b06aeb35a45ddeac
fetched_at: '2026-06-28T22:39:17.377140+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  o ICMS ST?
type: support-article
updated_at: '2026-03-19T13:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17802352397591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ICMS-ST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17802359654295) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Como calcular o ICMS ST pelo Configurador de Tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

O NCM sujeito a incidencia do calculo do ICMSST deve o ICMS configurado com a CST10, para gerar o XML de forma correta

A figura abaixo mostra o trecho do XML, correspondente ao grupo **Grupo N03 – Grupo Tributação do ICMS = 10**.

<ICMS10>

<orig>**0**</orig>

<CST>**10**</CST>

<modBC>**3**</modBC>

<vBC>**1000.00**</vBC>

<pICMS>**18.0000**</pICMS>

<vICMS>**180.00**</vICMS>

<modBCST>**4**</modBCST>

<pMVAST>**37.9300**</pMVAST>

<vBCST>**1379.30**</vBCST>

<pICMSST>**18.0000**</pICMSST>

<vICMSST>**68.27**</vICMSST>

</ICMS10>

</ICMS>

MV\_ESTADO = SP

Cliente = SP

Tipo cliente = Solidário

CFOP = 5910

Aliq. ICMS = 18%

Aliq. ICMS ST = 18%

MVA = 37,93%

TES

CFOP = 5401

Calculo

Mercadoria = 1000,00

Base de calculo do ICMS = 1000,00 \*18% = 180,00

Base de calculo do ICMS ST = 1000,00 \* 37,93% = 1379,30

1379,30 \*18% = 248,27

248,27-180,00= 68,27

Valor total da Nota fiscal = 1068,27

Ids Tributos

ICMS  
ICMS ST

PIS

COFINS

Cadastro de Regra de NCM = 2301.09.00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087059351)

**Regra de Base de calculo ICMS**

 O:VAL\_MERCADORIA -  O:DESCONTO +  O:FRETE +  O:SEGURO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087062935)

Regra de aliquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094712215)

Regra de escrituração do ICMS

Incidencia = tributado

CST = 10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094712983)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094713495)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087067927)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094715543)

Perfil origem x destino - 000002 - todas as UFS

Perfil Participante = TODOS

Perfil de Operação = CFOP 5401

Perfil Produto = 000068

**Regra de Base de calculo do ICMS ST**

( O:VAL\_MERCADORIA + O:DESPESAS + O:FRETE  ) \* I:MVA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094716567)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094718231)

Regra de aliquota a mesma

Regra de escrituração

Incidencia = tributado

CST = 10

total  NF = soma no total da nota e duplicata

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087072279)

Regra de Calculo Documentos Fiscais - ICMSST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087073175)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094722071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094723863)

Perfis os mesmos

**Regra de Base de calculo para PIS/COFINS**

 ( O:VAL\_MERCADORIA + O:DESPESAS + O:FRETE - O:DESCONTO ) -  VAL:600001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087085335)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094726551)

Regra de aliquota a mesma

Regra de escrituração PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094728087)

Regra de escrituração COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094729367)

Regra de Calculo Documentos fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087089175)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094731031)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094731543)

Regra de Calculo Documentos fiscais - COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087095959)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094733847)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087098775)

Calculo IBS /CBS - conforme carga inicial

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

Tributos

IBSEST

CBSFED

cClasstrib = 000001

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

Base de calculo do IBS/CBS

  ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

744,15 \*0,10 = 0,74

744,15\*0,90 = 6,70

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094736151)

CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152094737175)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152087102871)

CJ3\_CCT é gravado somente para o IBS/CBS

XML

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

IBSCBS>

<CST>**000**</CST>

<cClassTrib>**000001**</cClassTrib>

<gIBSCBS>

<vBC>**744.15**</vBC>

<gIBSUF>

<pIBSUF>**0.1000**</pIBSUF>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vIBSUF>**0.74**</vIBSUF>

</gIBSUF>

<gIBSMun>

<pIBSMun>**0**</pIBSMun>

<vIBSMun>**0**</vIBSMun>

</gIBSMun>

<vIBS>**0.74**</vIBS>

<gCBS>

<pCBS>**0.9000**</pCBS>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vCBS>**6.70**</vCBS>

</gCBS>

</gIBSCBS>

</IBSCBS>

</imposto>

<vItem>**1068.27**</vItem>

Boletim

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos>
