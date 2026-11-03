---
article_id: 4413001001623
category: Férias
content_hash: 1d2b8a01ef69b3cb87e58653b830272d2560ee9e6ef58114d8438e46b048035e
fetched_at: '2026-06-28T22:46:56.357205+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Contrato Suspenso estende período aquisitivo '
type: support-article
updated_at: '2024-10-23T22:13:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413001001623-RH-RM-FOP-Contrato-Suspenso-estende-per%C3%ADodo-aquisitivo
---

**Afastamento por Contrato Suspenso mantém período aquisitivo de férias**

Quando o funcionário for afastado por contrato suspenso, o sistema fará o acerto do período aquisitivo de férias de acordo com este parâmetro e o motivo selecionado para que não haja perda do período aquisitivo gerado por esse afastamento. O acerto do período aquisitivo deve ser executado no retorno do afastamento.

**Afastamento por Contrato Suspenso mantém avos de 13º salário**

Quando o funcionário for afastado por contrato suspenso, o sistema fará o cálculo dos avos de 13º salário de acordo com este parâmetro e o motivo selecionado para que não haja perda dos avos gerado por esse afastamento.

**Motivo do afastamento por Contrato Suspenso sem perda de avos**

Quando for marcado um dos parâmetros acima será necessário informar neste campo o motivo de afastamento que será considerado para não computar a perda de avos referentes ao afastamento por Contrato Suspenso. Para que esta parametrização seja considerada é necessário que este motivo seja igual ao motivo cadastrado no afastamento do funcionário.  
  
**Observação**  
Caso estes parâmetros não estejam selecionados todos os afastamentos serão considerados para a perda de avos nos processos de acerto de período aquisitivo, rescisão, histórico de provisões e lançamento de 13º salário. Para o cálculo da rescisão com a perda dos avos do período aquisitivo deve ser executado o acerto do período aquisitivo.  
  
**Exemplo:**   
Mês competência 05/2020 – Parâmetros marcados e motivo preenchido com 1 – Sem perda de avos

Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 1 – Sem perda de avos

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 2 – Com perda de avos  
  
Executando o acerto de período aquisitivo:  
  
[RH - RM - FOP - Férias: Acerta Período Aquisitivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015475891-RH-RM-FOP-F%C3%A9rias-Acerta-Per%C3%ADodo-Aquisitivo)  
  
Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Período não foi estendido porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – Período aquisitivo de 02/01/2020 a 02/03/2021 – Período foi estendido porque o motivo de afastamento não era o mesmo do parametrizador.  
  
Calculando 13º salário em dezembro/2020:

Funcionário 1 – 12 avos – Avos completos porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – 10 avos – Perda de 2 avos porque o motivo de afastamento não era o mesmo do parametrizador.  
  
**Observação**  
Para a rescisão contratual e histórico de provisões deverá ser executado o acerto de período aquisitivo primeiro pois assim o período aquisitivo estará correto no momento do cálculo. E o cálculo do 13º salário rescisão e histórico de provisões do 13º salário seguirá do mesmo jeito do 13º salário normal.
