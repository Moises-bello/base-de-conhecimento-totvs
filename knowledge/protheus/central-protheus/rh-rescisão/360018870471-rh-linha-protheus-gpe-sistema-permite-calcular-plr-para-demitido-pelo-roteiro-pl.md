---
article_id: 360018870471
category: RH - Rescisão
content_hash: 2bfdcaf6fa8af505fc0f9bba31b22b972b873bfa0a1f770c05de11369fba2536
fetched_at: '2026-06-28T22:43:54.473513+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema permite calcular PLR para Demitido pelo
  roteiro PLR, porém, no fechamento do roteiro as verbas não foram para a SRD
type: support-article
updated_at: '2025-06-25T12:20:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018870471-RH-Linha-Protheus-GPE-Sistema-permite-calcular-PLR-para-Demitido-pelo-roteiro-PLR-por%C3%A9m-no-fechamento-do-roteiro-as-verbas-n%C3%A3o-foram-para-a-SRD
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33041048272535)***Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Gestão de Pessoal, sistema permite calcular PLR para demitido pelo roteiro PLR, porém, no fechamento do roteiro as verbas não carregaram para tabela SRD.  
  
**Ambiente**Microsiga Protheus - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Realizado ajuste na fórmula S\_VLDADMPL para validar se o funcionário está demitido no período de cálculo do roteiro PLR, se estiver o cálculo não será realizado.

Atualmente o cálculo de PLR para funcionário demitidos deve ocorrer exclusivamente pelo roteiro RES. Será planejado melhoria no produto para permitir o cálculo de demitidos pelo roteiro PLR.

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o *backup* prévio;  
2. Aplique pacote de atualização   
3. Refaça o teste.  
  
**Saiba Mais  
[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)**
