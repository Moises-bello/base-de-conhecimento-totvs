---
article_id: 18343656358167
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: a4bb4dabfd1d1b5f32a587f28e016de8b6416c16e83c8ac4f0d23db0eb401230
fetched_at: '2026-06-28T22:39:22.115967+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - MP FIS Como gerar a sub-apuração
  ?
type: support-article
updated_at: '2023-10-17T20:10:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18343656358167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-MP-FIS-Como-gerar-a-sub-apura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18343664274711) Tempo aproximado para leitura: **05:00 min** **Dúvida** Como gerar a sub-apuração ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Será configurado o exemplo do boletim de sub-apuração  
estado = SC

Configurações:

1a) Parametros

MV\_estado = SC

MV\_APUSEP = 1/2/3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18341368180503)

Configuração de acordo com o Sped Fiscal

<https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal>

2a) Codigos de lançamentos :

SC24000001/ SC10000012 / SC54000001

Baixar a tabela 53 do site <http://www.sped.fazenda.gov.br/>

Conforme passo a passo

<https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533801-Escritura%C3%A7%C3%A3o-e-Relat%C3%B3rios-Fiscal-SIGAFIS->

3a) Configurar na rotina mata985 o tipo de apuração, cada codigo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18341903858711)

SC54000001 - cons. apurac = 3 -somente ap centralizadora

SC10000012 - cons. apurac = 2 - todas

4a) Amarrar na TES os codigos de lançamento junto com os reflexos

TES de exemplo calculo do credito presumido

**Tp Cred Pres.(F4\_TPCPRES**) = B = cred BC ICMS

**Crd.Pres (F4\_CRDPRES) =**11%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18342338974743)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18342097657623)

Reflexo 000010 - padrão criado pelo U\_IMPSPED

Reflexo 000070 - padrão criado pelo U\_IMPSPED

5a) Lançamento de duas notas fiscais de saidas, sendo:

1NF - valor de 1000,00 com icms de 18% e credito presumido de 11% , conforme amarrado no TES

2NF - valor de 2000,00 com icms de 18% sem credito presumido

6a) Lançamento das notas fiscais de saidas

1NF - cliente = SC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18342639875863)

2NF - cliente = SC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18342775186455)

Apuração do ICMS

1a) Sub - Apuração livro 1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18342850455831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18343284083351)

A sub-apuração gera GNRE

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18343324762135)

2a) Apuração Centralizadora

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18343342340759)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18343372554647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18343381380247)

Dessa forma foi deduzido o valor do icms de vendas apurado na sub-apuração.

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=484694802
