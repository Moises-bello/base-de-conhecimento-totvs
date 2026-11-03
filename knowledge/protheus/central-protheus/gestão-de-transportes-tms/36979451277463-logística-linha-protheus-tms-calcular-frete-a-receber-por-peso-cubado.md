---
article_id: 36979451277463
category: Gestão de Transportes (TMS)
content_hash: 96f4304037323d6121c9ac63ff71afd3a57743b2a1ff171990d6fc464c406962
fetched_at: '2026-06-28T22:45:27.360010+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Calcular frete a receber por Peso Cubado
type: support-article
updated_at: '2025-12-12T20:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36979451277463-Log%C3%ADstica-Linha-Protheus-TMS-Calcular-frete-a-receber-por-Peso-Cubado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36979451230999) Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Como calcular frete a receber por peso cubado no **Protheus TMS**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para calcular um componente de peso cubado no frete a receber no TMS, é necessário cadastrar rotina **TMSA030 - Componentes de Frete** um componente na que calcula sobre Peso Mercadoria e o campo **Calc.do Peso - DT3\_CALPES = 2 - Peso Cubado**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979467136279)

Configure esse componente na configuração da tabela de frete a receber que irá utilizar para calcular o documento na rotina **TMSA130 - Config. Tab. Frete**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979467142039)

Configure as faixas e valores do componente na tabela de frete conforme sua necessidade na rotina **TMSA010 - Tabela de Frete**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979467144215)

Defina a tabela de frete no contrato do cliente que irá utilizar essa tabela de frete na rotina **TECA250 - Contrato de Cliente**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979467145495)

Com isso, ao calcular o frete, **o componente será calculado com base no peso cubado, desde que o peso cubado seja igual ou maior que o peso real.**  
  
Por exemplo, o componente foi configurado para calcular 1 real por quilo.  
  
Quando o Peso Cubado é maior que o Peso Real, calcula sobre o Peso Cubado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979451237271)

Quando o Peso Real é maior que o Peso Cubado, calcula sobre o Peso Real:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36979451238423)

Caso deseje customizar o cálculo do peso cubado, pode verificar os pontos de entrada listados em **Saiba mais**.

**Saiba mais**  
[Logística - Linha Protheus - TMS - Ponto de entrada TM200CUB Altera Valor do Peso Cubado](https://totvssuporte.zendesk.com/agent/tickets/25708745#:~:text=Log%C3%ADstica%20%2D%20Linha%20Protheus%20%2D%20TMS%20%2D%20Ponto%20de%20entrada%20TM200CUB%20Altera%20Valor%20do%20Peso%20Cubado)  
[Logística - Linha Protheus - TMS - Ponto de entrada TM040FCB Altera Fator de Cubagem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452211-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040FCB-Altera-Fator-de-Cubagem)  
[Logística - Linha Protheus - TMS - Ponto de Entrada TMCALFRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035401873-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-Entrada-TMCALFRE)
