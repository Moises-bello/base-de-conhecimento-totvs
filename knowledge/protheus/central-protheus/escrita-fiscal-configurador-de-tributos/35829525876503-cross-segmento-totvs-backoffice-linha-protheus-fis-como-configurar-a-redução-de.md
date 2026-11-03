---
article_id: 35829525876503
category: Escrita Fiscal - Configurador de Tributos
content_hash: 92af9ff2ddf13a49ccee45c938004a057a613a34388db4342aea8fcbde6fb967
fetched_at: '2026-06-28T22:39:17.169784+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  a redução de base do ICMS no fisa170?
type: support-article
updated_at: '2025-10-23T13:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35829525876503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-a-redu%C3%A7%C3%A3o-de-base-do-ICMS-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534634007) Tempo aproximado para leitura: 00:10 **min**  
  
**Dúvida**  
 Como configurar a redução de base do ICMS no fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A configuração abaixo é um exemplo e pode ser aplicada para qualquer estado.

Redução de base = 60%

Aliquota icms = 17%

Aliquota Pis = 1,65%

Aliquota Cofins = 7,6%

**Calculo**

Valor da mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\*60% = 400,00\*17% = 68,00

Base de calculo do PIS/Cofins = 1000,00-68,00= 932,00

932,00\*1,65% = 15,38

932,00\*7,6% = 70,83

MV\_ESTADO = SC

Cliente = SC

Cadastro Regra de NCM

19053100

ICMS - SC para SC - origem \* - aliquota 17%

PIS -    SC para SC - origem \* - aliquota 1,65%

COF -  SC para SC - origem \* - aliquota 7,6%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525835543)

Regra de Base de Calculo do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525838615)

Regra de Aliquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534636055)

Regra de Escrituração - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534639383)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525841943)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534641943)

Regra de Base de Calculo para PIS /COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534642199)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525844119)

Regra de Aliquota a mesma

Regra de Escrituração do PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525845143)

Regra de Calculo Documentos Fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534643863)

Perfis os mesmos

Regra de Escrituração do Cofins

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534644375)

Regra de Calculo Documentos Fiscais - COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525848087)

Perfis os mesmos

Usando os Ids Totvs Padrão o sistema vai gravar o ICMS, PIS e COFINS nos mesmos campos do TES nas tabelas SD2/SF2/SF3/SFT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534645399)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829525852439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35829534646807)
