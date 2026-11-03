---
article_id: 360051310413
category: RH - Folha de Pagamento
content_hash: 5a1f319c259273deec250e71155d59466bf5411a89146a6ac666a1b5f8505e57
fetched_at: '2026-06-28T22:44:14.636430+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o mnemônico P_DSRCCMAT
type: support-article
updated_at: '2025-10-06T13:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051310413-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-DSRCCMAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26998287459351) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como parametrizar o mnemônico P\_DSRCCMAT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Realizado ajuste no cálculo de DSR sobre Hora Extra para quando existem verbas de base de Horas Extras lançadas de forma rateada. Criado o mnemônico **P\_DSRCCMAT** cuja configuração habilita geração do DSR de acordo com o rateio das verbas de base de Hora Extra. Para configurar o mnemônico acesse **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998287462807)  
  
Mnemônico Configurado:**

**.T.** - Default de sistema, onde é gerada a verba de DSR (com valores aglutinados quando existe rateio) para o centro de custo do funcionário) - Padrão do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998303286551)

**.F.** - Para geração da verba de DSR conforma centro de custo da verba de base de Hora Extra.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998303287831)

**Saiba mais:**

[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011913513-RH-Defini%C3%A7%C3%B5es-de-C%C3%A1lculo)
