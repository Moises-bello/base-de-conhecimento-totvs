---
article_id: 40128147887895
category: Escrita Fiscal - Configurador de Tributos
content_hash: ce354073081fab41371c837a3ea947cb0da6c23e3b1c9cb0b666677c0b35967f
fetched_at: '2026-06-28T22:39:17.592118+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Como calcular FECP nas operações com ICMS no Fisa170?
type: support-article
updated_at: '2026-04-30T14:11:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40128147887895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-calcular-FECP-nas-opera%C3%A7%C3%B5es-com-ICMS-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114285079) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como calcular FECP nas operações com ICMS no Fisa170?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Essa documentação é um exemplo de calculo de FECP que pode ser usado para qualquer estado, observando a alíquota do FECP.

Exemplo

MV\_ESTADO = RJ

Cliente = RJ

Cadastro de Produtos = 000018

origem = 0

NCM = 3926.90.90

TES

5102

Configurador de tributos

ID tributos

ICMS

IPI

FECPIC

PIS

COFINS

IBS/CBS

Cadastro de Regra de NCM - 3926.90.90

ICMS - RJ para RJ - origem = 0 alíquota 20%

IPI - RJ para \*\* - origem = 0 alíquota 9,75%

FECPIP - RJ para RJ - origem = 0 alíquota 2%

PIS - RJ para \*\* - origem = 0 alíquota 1,65%

COFINS - RJ para \*\* - origem = 0 alíquota 7,6%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114286487)

#### **ICMS**

##### Regra de base de Calculo - ICMS

O:VAL\_mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174878999)

Regra de alíquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114296855)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174880535)

Regra de escrituração - ICMS

Incidência = tributado

CST = 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174881943)

Regra de calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114298647)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114299159)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174888983)

#### **FECP**

Regra de base de calculo a mesma do ICMS

Regra de alíquota

I:ALIQ\_NCM

Regra de escrituração

a mesma do ICMS

Regra de Calculo Documentos Fiscais - FECP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114308631)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114308887)

Perfis os mesmos

#### **IPI**

Regra de base de calculo IPI

O:VAL\_mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174878999)

Regra de alíquota

I:ALIQ\_NCM

Regra de escrituração - IPI

Incidência = tributado

total NF = 6

CST = 50

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174889751)

Regra de Calculo Documentos Fiscais - IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174890647)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114311959)

Perfis os mesmos

#### **PIS/COFINS**

Regra de Base de calculo PIS/COFINS

( O:VAL\_MERCADORIA + O:DESPESAS + O:FRETE - O:DESCONTO ) - VAL:001001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114312471)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114312855)

Regra de alíquota

I:ALIQ\_NCM

Regra de escrituração - PIS

Incidência = tributado

CST = 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174895895)

Regra de Calculo Documentos Fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114314519)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114315287)

Perfis os mesmos

Regra de escrituração - COFINS

incidência = tributado

CST = 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114316695)

Regra de Calculo Documentos Fiscais - COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174897815)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174898455)

Perfis os mesmos

#### **IBS/CBS**

Regra de Base de Calculo IBS/CBS

https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075

* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

Regra de alíquota - IBSEST

alíquota = 0,10

Regra de alíquota - CBSFED

alíquota = 0,90

Regra de escrituração

cClasstrib = 000001

**Pedido de Vendas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114318359)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114319511)

As informações são gravadas na CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174900503)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128114322711)

CD2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40128174902167)

Boletim

[**CFGTRIB - Cálculos no Configurador de Tributos**](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[**CFGTRIB - Perguntas e Respostas - Configurador de Tributos**](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Perguntas+e+Respostas+-+Configurador+de+Tributos)

[**CFGTRIB - Boas Práticas - Guia de Utilização do Configurador de Tributos**](https://tdn.totvs.com/pages/viewpage.action?pageId=825324804)

**TES -** [**https://tdn.totvs.com/pages/releaseview.action?pageId=928965724**](https://tdn.totvs.com/pages/releaseview.action?pageId=928965724)
