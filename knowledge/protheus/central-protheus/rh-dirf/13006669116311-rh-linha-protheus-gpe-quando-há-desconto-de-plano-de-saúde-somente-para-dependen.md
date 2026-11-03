---
article_id: 13006669116311
category: RH – DIRF
content_hash: 837596331404382945f944904cfa70c409c9036150b970228c2829711d473456
fetched_at: '2026-06-28T22:44:07.187602+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Quando há desconto de plano de saúde somente para
  dependentes e o desconto é lançado direto na folha, os dados não são gerados no
  arquivo magnético
type: support-article
updated_at: '2025-08-15T12:55:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13006669116311-RH-Linha-Protheus-GPE-Quando-h%C3%A1-desconto-de-plano-de-sa%C3%BAde-somente-para-dependentes-e-o-desconto-%C3%A9-lan%C3%A7ado-direto-na-folha-os-dados-n%C3%A3o-s%C3%A3o-gerados-no-arquivo-magn%C3%A9tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34205068108695) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Quando há desconto de plano de saúde somente para dependentes e o desconto é lançado direto na folha, os dados não são gerados no arquivo magnético.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**A importação apenas dos dependentes de plano de saúde causa erro no validador da DIRF.  
  
**Solução**Quando o desconto de plano de saúde de dependente é lançado direto na folha e não há desconto de titular, se gerado no arquivo magnético apenas os dados dos dependentes, ao importar no PGD é gerado erro abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13006434080791)  
  
Por conta disso, os dados não são enviados no arquivo magnético.

Quando usada as rotinas padrões de cálculo de plano de saúde, mesmo que o titular não tenha desconto do plano, ele é gerado em Informações complementares da rotina Manutenção Arquivo com o valor zerado conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13006501246615)  
  
Então é gerado no arquivo magnético o titular, com o valor zerado, e assim é importado sem erro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13006555696791)  
  
Neste caso, é possível incluir a informação zerada em informações complementares, pelo caminho **>Miscelânea >Dirf >Manutenção arquivo** conforme exemplo acima, ou incluir diretamente no PGD.  
  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
