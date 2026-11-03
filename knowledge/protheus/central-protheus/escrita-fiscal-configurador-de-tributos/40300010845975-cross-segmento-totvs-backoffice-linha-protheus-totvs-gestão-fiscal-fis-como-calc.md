---
article_id: 40300010845975
category: Escrita Fiscal - Configurador de Tributos
content_hash: 471a3c70729865329aa23a2be3d6c3cea218c71bc39706c4c80d8b13008ca468
fetched_at: '2026-06-28T22:39:17.605862+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Como calcular Suframa de forma Hibrida com cBenef ?
type: support-article
updated_at: '2026-05-07T14:40:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40300010845975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-calcular-Suframa-de-forma-Hibrida-com-cBenef
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010808471) Tempo aproximado para leitura: **00:10mm**  
**Dúvida**  
Como calcular Suframa de forma Hibrida com cBenef ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**  
Nesse documento vamos demonstrar a configuração de um calculo de suframa pelo TES, IBS/CBS pelo configurador e cBenef pelo fisa140.

Exemplo:

SP para Manuas exemplo de calculo 1

<https://tdn.totvs.com/pages/releaseview.action?pageId=605019302>

#### **1)Venda para Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins (Pis e cofins descontado antes do calculo do ICMS).**

**Parâmetros**

MV\_SUFRAMA = .T.

MV\_RPCBIZF = .T.  (desconto de ICMS após o desconto de PIS e Cofins)

MV\_RPCBIUF = AM

MV\_DESCZF  = .T.

MV\_DESZFPC = .T.

MV\_DSZFSOL= .T.

MV\_IPIZFM = .T.

**Cadastros**

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido como Revendedor

Desc. P/ Suframa (A1\_CALCSUF) –  SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010809239)

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Não ou Em branco

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026075671)

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) –  SIM

Livro Fiscal ICMS (F4\_LFICM)  -  Outros

Material de Consumo (F4\_CONSUMO) –  Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  -  2

PIS/COFINS (F4\_PISCOF) -   AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) –  CALCULA.

Mot. Desone (F4\_MOTICM) - 7 suframa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026076183)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010812695)

### **Calculo**

Valor da mercadoria= 1000,00

Base de calculo do ICMS = 1000,00- 16,50-76,00 = 907,50\*7% = 63,53

Base de calculo do PIS/Cofins = 1000,00

1000,00\*1,65% = 16,50

1000,00\*7,6% = 76,00

Configurador de tributos

* IBS Municipal
* IBS Estadual
* CBS Federal
* IBS Municipal Regular
* IBS Estadual Regular
* CBS Regular

cClasstrib = 200022

Operação originada fora da Zona Franca de Manaus que destine bem material industrializado de origem nacional a contribuinte estabelecido na Zona Franca de Manaus que seja habilitado nos termos do art. 442 da Lei Complementar nº 214, de 2025, e sujeito ao regime regular do IBS e da CBS ou optante pelo regime do Simples Nacional de que trata o art. 12 da Lei Complementar nº 123, de 2006, observado o art. 445 da Lei Complementar nº 214, de 2025.

Regra de Base de calculo

O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026076951)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010815767)

Regra de alíquota

O:zero

100% redução

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026079767)

Regra de escrituração

incidência = isento

cclasstrib = 200022

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010818071)

**Cbenef**

Fisa156

SP010840 = Isenção - ZONA FRANCA DE MANAUS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026081815)

Fisa140

6109 - CST40 - SP010840 - reflexo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010821143)

Reflexo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010822167)

#### Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026083991)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300026084759)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010823831)

cbenef

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010824983)

<cBenef>**SP010840**</cBenef>

<CFOP>**6109**</CFOP>

Ao faturar a nota fiscal vai gerar a CD2 e CJ3

O parametro MV\_CSTGXML precisa estar configurado para não dar erro no XML

Atualizações do Sped

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40300010825623)

Transmissão

IBSCBS>

<CST>**200**</CST>

<cClassTrib>**200022**</cClassTrib>

<gIBSCBS>

<vBC>**0**</vBC>

<gIBSUF>

<pIBSUF>**0**</pIBSUF>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vIBSUF>**0**</vIBSUF>

</gIBSUF>

<gIBSMun>

<pIBSMun>**0**</pIBSMun>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vIBSMun>**0**</vIBSMun>

</gIBSMun>

<vIBS>**0**</vIBS>

<gCBS>

<pCBS>**0**</pCBS>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vCBS>**0**</vCBS>

</gCBS>

<gTribRegular>

<CSTReg>**200**</CSTReg>

<cClassTribReg>**200022**</cClassTribReg>

<pAliqEfetRegIBSUF>**0**</pAliqEfetRegIBSUF>

<vTribRegIBSUF>**0**</vTribRegIBSUF>

<pAliqEfetRegIBSMun>**0**</pAliqEfetRegIBSMun>

<vTribRegIBSMun>**0**</vTribRegIBSMun>

<pAliqEfetRegCBS>**0**</pAliqEfetRegCBS>

<vTribRegCBS>**0**</vTribRegCBS>

</gTribRegular>

</gIBSCBS>

</IBSCBS>
