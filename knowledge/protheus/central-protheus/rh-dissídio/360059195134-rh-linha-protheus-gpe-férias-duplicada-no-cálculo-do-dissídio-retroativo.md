---
article_id: 360059195134
category: RH - Dissídio
content_hash: f9ff29b6c5b770cd741f785e530ee7c398c7aedab50c296680431cc97b6a2cf8
fetched_at: '2026-06-28T22:43:43.361273+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Férias duplicada no cálculo do dissídio retroativo
type: support-article
updated_at: '2025-08-15T18:22:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059195134-RH-Linha-Protheus-GPE-F%C3%A9rias-duplicada-no-c%C3%A1lculo-do-diss%C3%ADdio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34214364890391)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Valor de férias no dissídio retroativo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - A partir da versão 12.  
  
**Causa**Verbas de mês seguinte configurada para dissídio e as duas sequências da formula S\_CADIFFER habilitada nos roteiros de cálculo.  
  
**Solução**1. Necessário realizar a impressão do relatório de dissídio retroativo para verificar se alguma verba de férias e/ou adicional de mês seguinte está configurada para dissídio. Nenhuma verba de mês seguinte deve conter essa configuração, por isso o ajuste deve ser realizado na configuração de verbas.

2. Localizar dentro dos roteiros de cálculo(FOL) a primeira sequência da formula S\_CADIFFER (000720) e confirmar se a mesma encontra-se desabilitada.

Acesse:  
Atualizações -> Definições de cálculo -> Roteiros de Cálculo ->FOL -> Sequência 000720 -> Habilitado = Não :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14792033364631)

**Saiba Mais:**  
[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
