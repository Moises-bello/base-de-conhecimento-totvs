---
article_id: 41483144616599
category: Escrita Fiscal - Configurador de Tributos
content_hash: ee1047bc2fe0320121745a6a2ac3808bd16b7daacad386aa9339c2b4d21dd69c
fetched_at: '2026-06-28T22:39:17.254975+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o IPI para revenda e consumo na entrada da nota fiscal?
type: support-article
updated_at: '2026-06-25T14:47:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41483144616599-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-IPI-para-revenda-e-consumo-na-entrada-da-nota-fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144549015) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
 Como configurar o IPI para revenda e consumo na entrada da nota fiscal?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
O exemplo abaixo de configuração de aliquota de IPI, será demonstrado utilizando o cadastro de Regra de NCM para a configuração da aliquota, de acordo com cada NCM

NCM = 3926.90.90 = 15%

MV\_ESTADO = SP

Fornecedor = SP

1a) Exemplo de configuração de mercadoria adquirida para comercialização

CFOP = 1102

ID tributos

ICMS

IPI

Cadastro de Regra de NCM = 3926.90.90 - IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160522519)

**ICMS**

Regra de base de calculo - ICMS

**O:VAL\_MERCADORIA - O:DESCONTO + O:FRETE + O:SEGURO + O:DESPESAS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160523159)

Regra de aliquota

I:ALQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144552599)

Regra de escrituração

Incidência = tributado

CST = 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160527255)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144556951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144558103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144566295)

**IPI**

Regra de base de calculo - IPI

**O:VAL\_MERCADORIA - O:DESCONTO + O:FRETE + O:SEGURO + O:DESPESAS**

Regra de aliquota

I:ALIQ\_NCM

Regra de escrituração

Incidência = tributado

CST = 00

valor total = 6

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144568727)

Regra de Calculo Documentos Fiscais - IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144570775)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144573079)

Perfis os mesmos

**IBS/CBS - configurados de acordo com o boletim**

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

Regra de Base de calculo

* Valor Origem (F27\_VALORI): 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160536471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144574999)

CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160538263)

2a) Mesmo produto agora adquirido para consumo

CFOP = 1556

**IPI**

Regra de base de calculo do IPI

**O:VAL\_MERCADORIA - O:DESCONTO + O:FRETE + O:SEGURO + O:DESPESAS**

Regra de aliquota

I:ALIQ\_NCM

Regra de Escrituração

Incidência = Outros

CST = 49

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160539287)

Regra de Calculo Documentos Fiscais - IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144577047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160547095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160549527)

**ICMS**

Regra de base de calculo do ICMS

( O:VAL\_MERCADORIA + O:SEGURO + O:FRETE + VAL:000053 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144580119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144582423)

Regra de aliquota

I:ALIQ\_NCM

Regra de Escrituração

Incidência = Outros

CST = 90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144584215)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144585367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144587159)

Perfis os mesmos

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483160557463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41483144590103)

todos os impostos calculados pelo fisa170 geram CJ3

Boletim

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos>

[CFGTRIB - Boas Práticas - Guia de Utilização do Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=825324804)
