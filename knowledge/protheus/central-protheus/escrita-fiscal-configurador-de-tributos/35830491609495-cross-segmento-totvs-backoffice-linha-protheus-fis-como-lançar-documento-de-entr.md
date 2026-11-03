---
article_id: 35830491609495
category: Escrita Fiscal - Configurador de Tributos
content_hash: 0a519c2694df9706f6a8d6030eb76d3dd3d1b8e4698bdcd6df3c5f9efa212e28
fetched_at: '2026-06-28T22:39:17.267115+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como lançar documento
  de entradas com redução de base para consumo no fisa170?
type: support-article
updated_at: '2025-11-04T21:10:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35830491609495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-lan%C3%A7ar-documento-de-entradas-com-redu%C3%A7%C3%A3o-de-base-para-consumo-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491576087) Tempo aproximado para leitura: 00:10 **min**  
  
**Dúvida**  
Como lançar documento de entradas com redução de base para consumo no fisa170?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
Segue abaixo um exemplo de configuração que pode ser usado para qualquer estado.

MV\_estado = SC

Fornecedor = SC

Redução de base = 60%

Alíquota icms = 17%

**Calculo**

Valor da mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\*60% = 400,00\*17% = 68,00

Como a mercadoria é para consumo o valor do ICMS será apenas calculado e não vai gerar credito

TES

CFOP = 1556

F4\_consumo = sim ou outros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830461954967)

Perfil de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491578007)

B1\_origem = 0

Perfil de Operações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491578775)

Perfil Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830461959959)

Fornecedor = SC

Perfil Origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491580951)

MV\_ESTADO = SC

Regra de Base de Calculo do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491581463)

Regra de Alíquota

Informada manualmente

alíquota = 17%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830461962519)

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491582487)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491582999)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830461964311)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491584791)

Lançamento da nota fiscal de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830491585687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830461968279)

Campos que permanecem no TES

<https://tdn.totvs.com/pages/releaseview.action?pageId=928965724>

Boletim configurador

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos>
