---
article_id: 34775583988887
category: Escrita Fiscal - Configurador de Tributos
content_hash: 030d440b2cc7ec88e8c638920152dec47dc1ac0f4abd3c4dd0d26f82f6f76628
fetched_at: '2026-06-28T22:39:17.779852+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como fazer
  uma Venda com  o mesmo CFOP para fins diferentes na Configurador de Tributos?
type: support-article
updated_at: '2025-11-14T21:27:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34775583988887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-fazer-uma-Venda-com-o-mesmo-CFOP-para-fins-diferentes-na-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583947031) Tempo aproximado para leitura: 10:00**min**  
  
**Dúvida**  
Como fazer uma Venda com  o mesmo CFOP para fins diferentes no fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Venda com calculo de IPI, CFOP 5101 sendo para Revenda e Consumo

Valor da mercadoria = 1000,00

Aliquota do IPI = 3,25%

Aliquota do ICMS = 18%

Aliquota pis =1,65%

Aliquota Cof = 7,6%

1a) Venda de MV\_ESTADO = SP para Cliente UF = SP - para revenda

Base de calculo do ICMS = 1000,00\*18% = 180,00

Base de calculo do IPI = 1000,00\*3,25% = 32,50

Base de calculo PIS/COFINS = 1000,00-180,00= 820,00

PIS = 820,00\*1,65% = 13,53

COF = 820,00\*7,6% = 62,32

2a) Venda de MV\_ESTADO = SP para Cliente UF = SP - para consumo

Base de calculo do ICMS = 1032,50\*18% = 185,85

Base de calculo do IPI = 1000,00\*3,25% = 32,50

Base de calculo PIS/COFINS = 1000,00-185,85= 814,15

PIS = 814,15\*1,65% = 13,43

COF = 814,15\*7,6% = 61,88

Tabela DJ - no SIGACFG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583947415)

TES inteligente

Tipo = 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583960471)

Tipo = 03

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583961239)

TES = 560

Gera duplicata = sim

CFOP = 5101

Configurador

Cadastro de Regra de NCM = 3305.90.00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583962007)

IPI = SP para Todos = origem = 1 - aliquota = 3,25%

COF = SP para Todos = origem = 1 - aliquota = 7,6%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583975191)

Perfil Cadastro de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598278423)

Perfil Operações para Comercialização

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583975831)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598279191)

Perfil Operações para Consumo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583976215)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598279831)

Perfil Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598280215)

Perfil Origem x destino = todas as UFS = para IPI/PIS/COFINS

SP para SP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598281111)

Perfil Origem x destino = operações internas = para ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583977495)

Regra de Base de Calculo ICMS - para Revenda

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583977751)

Regra da Base de Calculo IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598282263)

Regra de Base de Calculo PIS/COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598285975)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598286487)

Regra de Base de Calculo ICMS + IPI na base

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598286871)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598287639)

Regra de Aliquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598288279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598290583)

Regra de Escrituração

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583981975)

Regra de Escrituração

IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583982743)

Regra de Escrituração

PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775598292119)

Regra de Escrituração

COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34775583983127)

Regra de Calculo Documentos Fiscais - ICMS para Revenda = 600001

Regra de Calculo Documentos Fiscais - IPI = 600002

Regra de Calculo Documentos Fiscais - PIS = 600005

Regra de Calculo Documentos Fiscais - COFINS = 600006

Regra de Calculo Documentos Fiscais - ICMS para Consumo = 600004

Videos em anexo das configurações e lançamentos das notas fiscais
