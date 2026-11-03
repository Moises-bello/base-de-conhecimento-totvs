---
article_id: 360018754571
category: RH - Rescisão
content_hash: 8c2198f40c00c1ef29caacabc2c489916616e5d3abc6f695b3ab64c332d231a1
fetched_at: '2026-06-28T22:43:52.169232+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Férias indenizadas, Proporcionais ou sobre aviso
  não são calculadas na rescisão mesmo quando o funcionário tem direito
type: support-article
updated_at: '2025-09-08T17:06:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018754571-RH-Linha-Protheus-GPE-F%C3%A9rias-indenizadas-Proporcionais-ou-sobre-aviso-n%C3%A3o-s%C3%A3o-calculadas-na-rescis%C3%A3o-mesmo-quando-o-funcion%C3%A1rio-tem-direito
---

**Ocorrência**Ao calcular Rescisão, as **Férias Vencidas,** **Férias Proporcionais ou Férias sobre Aviso** não estão sendo calculadas, mesmo o funcionário tendo direito.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Causa**Os gatilhos da rotina que **iniciam**o cálculo das férias é o **campo de DATA DO AVISO** em combinação com os campos seguintes no preenchimento como **DATA DE GERAÇÃO** e **HOMOLOGAÇÃO**.

Todos os casos de bases que apresentaram este problema, os campos estavam **invertidos** e a **DATA DO AVISO estava após os campos de DATA DE GERAÇÃO e HOMOLOGAÇÃO** (ficando como ultima posição e não carregando nenhum dos outros campos após ela).

**Solução**Forçar o preenchimento de todos os campos **após a DATA DO AVISO.**Verifique via configurador se a ordem da SRG está correta.![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014800671)

Abaixo ordem correta dos campos da tabela SRG via Configurador (Cabeçalho da Rescisão):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15970209150871)  
  
**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
