---
article_id: 36501682971415
category: Escrita Fiscal - Configurador de Tributos
content_hash: b0bb1bb5e0615227f82f7eb6e3806ca712e458916579194f0b6548e029d095f1
fetched_at: '2026-06-28T22:39:17.110341+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Abatimento na base
  do ISS utilizando o Configurador de Tributos
type: support-article
updated_at: '2025-11-21T18:38:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36501682971415-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Abatimento-na-base-do-ISS-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36501682949143) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar a Regra de Base de Calculo para que o valor informado no campos Abatim. ISS (C6\_ABATISS) ou Abat. Mat. (C6\_ABATMAT) deduza da base do ISS.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2310  
  
**Solução**  
Para que ocorra o abatimento dos valores informado dos nos campo Abatim. ISS ou Abat. Mat. na base do ISS, deve ajustar a Regra de Base de Calculo conforme abaixo:

* Para que deduza o valor informado no campo Abat. ISS (C6\_ABATISS) ou Abat. ISS (D1\_ABATISS):

1. Ajuste o campo Valor Origem = 11 - Fórmula Manual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36501682949783)

2. Acesse a aba Detalhamento da Fórmula de Cálculo:

 - Campo Tipo da Regra s ser consultada = 01 - Valores de Origem e adicione O:VAL\_MERCADORIA - O:DEDUCAO\_SUBEMPREFEITADA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36501698385175)

* Para que deduza o valor informado no campo Abat. ISS (C6\_ABATMAT) ou Abat. ISS (D1\_ABATMAT):

1. Ajuste o campo Valor Origem = 11 - Fórmula Manual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36501682949783)

2. Acesse a aba Detalhamento da Fórmula de Cálculo:

 - Campo Tipo da Regra s ser consultada = 01 - Valores de Origem e adicione O:VAL\_MERCADORIA - O:DEDUCAO\_MATERIAIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36501682951959)

OBS: A configuração é utilizada para notas de Entrada e Saída.

Documentações relacionadas:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular o ISS utilizando o Configurador de Tributos para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33675439757335-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ISS-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Código de Serviço ISS por Perfil de Operação](https://tdn.totvs.com/pages/releaseview.action?pageId=883676152)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
