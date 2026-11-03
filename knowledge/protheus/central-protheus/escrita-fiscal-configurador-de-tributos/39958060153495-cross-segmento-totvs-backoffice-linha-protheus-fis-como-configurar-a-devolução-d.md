---
article_id: 39958060153495
category: Escrita Fiscal - Configurador de Tributos
content_hash: 6f7cc9057b374a4d9494af24b134ad41a22de9d838df3699c1319358350788d3
fetched_at: '2026-06-28T22:39:17.164526+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  a devolução de compra para consumo com ICMS e IPI no FISA170?
type: support-article
updated_at: '2026-05-29T13:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39958060153495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-a-devolu%C3%A7%C3%A3o-de-compra-para-consumo-com-ICMS-e-IPI-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060117271) Tempo aproximado para leitura: **00:10min**  
  
**Dúvida**  
Como configurar a devolução de compra para consumo com ICMS e IPI no fisa170?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
O exemplo abaixo representa a configuração do calculo de ICMS e IPI para mercadorias adquiridas para consumo e podem ser usadas para qualquer estado de acordo com a sua aliquota interna.

Exemplo:

MV\_ESTADO = SP

Fornecedor = SP

Cadastro de Produtos

Origem = 0

TES

CFOP = 1556

Configurador de tributos

ID tributo

ICMS  
IPI

Cadastro de Regra de NCM

NCM = 87083090

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082089751)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060119063)

**Regra de Base de calculo - IPI**

O:VAL\_MERCADORIA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060120471)

Regra de alíquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060121367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082095895)

**Regra de Escrituração**

Incidência = Outros

CST = 49

Total nota fiscal = 6

Incid. devolução = Outros

CST devolução = 50

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060123927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060124695)

**Regra de Calculo Documentos Fiscais - IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082099863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082101015)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060128791)

**Regra de Base de calculo ICMS**

( O:VAL\_MERCADORIA + VAL: calculo do IPI )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060129687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060130583)

**Regra de Alíquota**

I:ALIQ\_NCM

A mesma do IPI

**Regra de escrituração ICMS**

Incidência = Outros

CST = 90

Incid. devolução = Tributado

CST = 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060131351)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060132119)

**Regra de Calculo Documentos Fiscais - ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082106647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082107799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082108311)

**IBS/CBS - configurados de acordo com o boletim**

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

Regra de Base de calculo

* Valor Origem (F27\_VALORI): 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

Alíquota - IBSMUN

Informada manualmente = 0,10

Alíquota - CBSFED

Informada manualmente = 0,90

Valores

Mercadoria = 1000,00

Base de calculo do IPI = 1000,00\*3,25% = 32,50

Base de calculo do ICMS = 1000,00+32,50 = 1032,50\*18% = 185,85

1a) Entrada da mercadoria para consumo - CFOP = 1556

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060136343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082108823)

CJ3 - preenchida

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060136855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060137367)

CJ3\_CSTCAB - para os impostos do legado - ICMS, IPI, ISS, PIS e COFINS

CJ3\_CCT - para o IBS/CBS

2a) Pedido de Vendas - devolução - CFOP - 5556

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082110103)

Após faturar a NF - CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958060139287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39958082116375)

Boletim

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos)
