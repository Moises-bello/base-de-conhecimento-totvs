---
article_id: 40468684143127
category: Escrita Fiscal - Configurador de Tributos
content_hash: 6fb86364c62c77a45a2f0aaa97a813e337163e96078ab860c2e217970d8c9ccf
fetched_at: '2026-06-28T22:39:17.645373+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  Suframa com ICMS, PIS e COFINS desonerados no fisa170?
type: support-article
updated_at: '2026-05-14T16:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40468684143127-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-Suframa-com-ICMS-PIS-e-COFINS-desonerados-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684085143) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**

**Como configurar o Suframa com ICMS, PIS e COFINS desonerados no fisa170?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Exemplo de calculo do Suframa onde: o valor do PIS e COFINS deduz da base de calculo do ICMS e todos são desonerados.

**Memória de cálculo:**

Total da mercadoria: 1000,00   
**x 1,65% PIS = 16,50**  
**x 7,6% COFINS = 76,00**

Base para ICMS: Total dos produtos – PIS – COFINS  
= 1000,00- 16,50 -76,00  
= 907,50 =X **7% ICMS = 63,52**

Total da NF: Valor da mercadoria - Impostos desonerados

= 1000,00 – 16,50 – 76,00 – 63,52 = = 843,98

Parâmetro

|  |  |
| --- | --- |
| **MV\_DESCZF** | Indica se a filial calcula o desconto Suframa quando a venda for realizada para os estados beneficiados. = .F. |

TES

CFOP = 6109

**Importante**

Nas operações com SUFRAMA, por conta da variedade de cenários, é recomendado utilizar a configuração da TES sem calculo de impostos, evitando assim a possibilidade de variações nos resultados dos cálculos em decorrência de fluxos gerados pela TES.

Configurador de Tributos

ID tributos

ICMS

DZFICM

DZFPIS

DZFCOF

### **DZFPIS**

Regra de base de calculo

O:VAL\_mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684086167)

Regra de alíquota

Informada manualmente = 1,65%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684086807)

Regra de escrituração

Incidência = Isento

CST = 07

Total da nota fiscal = 03

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636376727)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636377239)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684088983)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684091799)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684093207)

### **DZFCOF**

Regra de Base de calculo

A mesma do PIS

Regra de alíquota

Informada manualmente = 7,6%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684095511)

Regra de escrituração

Incidência = Isento

CST = 07

Total da nota fiscal = 03

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636378007)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684099735)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684100375)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636380183)

Perfis os mesmos

### **DZFICM**

Regra de Base de calculo

O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684103703)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684104599)

Regra de alíquota

O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636385175)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684110359)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684111767)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636390935)

Motivo da desoneração = 7 = suframa

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684114711)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636392983)

Perfis os mesmos

Detalhamento da formula de calculo / tributado

( B:000003 \* A:000003 ) + ( O:VAL\_MERCADORIA - VAL:010002 - VAL:010003 ) \* ( A:000006 /100 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636393367)

### **ICMS**

Regra de base de calculo

O:VAL\_MERCADORIA - VAL:010002 - VAL:010003

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684116887)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636394775)

Regra de alíquota

Informada Manualmente = 7%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684117783)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684120471)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684120727)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684121623)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684121879)

Perfis os mesmos

Configurações do IBS/CBS - orientação no documento abaixo:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - FIS - Como calcular Suframa de forma Hibrida com cBenef ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40300010845975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-calcular-Suframa-de-forma-Hibrida-com-cBenef)

#### **Cbenef**

**Cadastro de Regra de Ajuste de Lançamento**

**Tabela Fisa156 = SP010840**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636400535)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468636401047)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684129047)

<NCM>**39269090**</NCM>

<cBenef>**SP010840**</cBenef>

<CFOP>**6109**</CFOP>

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684129687)

CD2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40468684130455)

XML

ICMS>

<ICMS40>

<orig>**0**</orig>

<CST>**40**</CST>

<vICMSDeson>**63.53**</vICMSDeson>

<motDesICMS>**7**</motDesICMS>

<indDeduzDeson>**1**</indDeduzDeson>

</ICMS40>

</ICMS>

<PIS>

<PISNT>

<CST>**07**</CST>

</PISNT>

</PIS>

<COFINS>

<COFINSNT>

<CST>**07**</CST>

</COFINSNT>

</COFINS>
