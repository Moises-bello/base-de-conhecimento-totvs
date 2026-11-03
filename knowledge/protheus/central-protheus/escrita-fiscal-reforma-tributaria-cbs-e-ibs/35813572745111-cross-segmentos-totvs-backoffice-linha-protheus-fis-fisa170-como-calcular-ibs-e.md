---
article_id: 35813572745111
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: f930eb7bca163c3d9b3a48fce571491ec4cf1d84ce23574691fa4b05660f997d
fetched_at: '2026-06-28T22:39:15.844208+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular
  IBS e CBS com redução de alíquota?
type: support-article
updated_at: '2025-10-22T19:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35813572745111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-IBS-e-CBS-com-redu%C3%A7%C3%A3o-de-al%C3%ADquota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35813572721303) Tempo aproximado para leitura: **00:020:00 min**  
  
**Dúvida**  
Como calcular IBS e CBS com redução de alíquota?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Para o cálculo do **IBS** e **CBS** no **Configurador de Tributos**, existem **dois cenários possíveis** para configuração:

1. **Cenário 100% no Configurador de Tributos**
2. **Cenário Híbrido (Legado + Configurador de Tributos)**

A documentação com as instruções de configuração de cada cenário pode ser consultada no artigo:  
👉 [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o cálculo do IBS e CBS?](#)

Após a devida configuração de um dos cenários acima, deve-se criar a **regra de alíquota** conforme o exemplo abaixo:

**Regra de Alíquota**

* IBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35813585444759)

* CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35813585445911)

Dessa forma, será considerada a redução percentual da alíquota na operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35813585449111)

OBS.: Para este exemplo, o sistema foi configurado para calcular a base do IBS e CBS com **redução dos valores referentes ao ICMS, PIS e COFINS**, conforme abaixo:

| Descrição | Valor (R$) |
| --- | --- |
| Valor da operação | 1.000,00 |
| (-) ICMS | 120,00 |
| (-) PIS | 16,50 |
| (-) COFINS | 76,00 |
| **Base de cálculo IBS/CBS** | **787,50** |

> 💡 Este é apenas um exemplo. Cada empresa deve configurar as deduções conforme sua necessidade operacional.

**Exemplo de Redução de Alíquota**

Alíquota padrão de IBS é 0,10% com a redução de 60% foi contabilizado 0,04%.

Alíquota padrão de IBS é 0,90% com a redução de 60% foi contabilizado 0,36%.

Desta forma as informações do IBS e CBS são gravadas corretamente nas tabelas **CJ3** e **F2D**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35813572726423)

Importante: Caso ocorre rejeição depois de gravas as tabelas CJ3 ou F2D deverá acionar o time do XML

Documentações relacionadas:

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

###
