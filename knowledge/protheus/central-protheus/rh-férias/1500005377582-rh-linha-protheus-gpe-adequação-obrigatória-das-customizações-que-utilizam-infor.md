---
article_id: 1500005377582
category: RH - Férias
content_hash: 2680acbd2c3941f2c20d8f75520f632cfeb4ed6a21f8bba6042a361535721fd1
fetched_at: '2026-06-28T22:43:57.924902+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Adequação obrigatória das customizações que utilizam
  informações de médias
type: support-article
updated_at: '2025-09-04T17:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005377582-RH-Linha-Protheus-GPE-Adequa%C3%A7%C3%A3o-obrigat%C3%B3ria-das-customiza%C3%A7%C3%B5es-que-utilizam-informa%C3%A7%C3%B5es-de-m%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26594392070551) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Adequação obrigatória das **customizações que utilizam informações de médias (RH).**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A partir da release 12.1.25 o alias **TRP (arquivo temporário onde são gravados valores de médias)** deixará de ser utilizado, de modo que **será preciso utilizar a variável pública cTBLXMED que contém o Alias utilizado pelas rotinas de médias.**Esta alteração tem reflexos em alguns pontos de entrada, desta forma as customizações precisam ser ajustadas. Os principais pontos de entrada são: **GPALTTRP, GPMEDTRP, GPMOVSRC, GPXCOMIS, GPAVOSMED, GPXMEDPD, GPMEDPER, GPMEDARR, GPDERSRD, GPMEDTAR.**

**Todos os pontos de entradas e/ou roteiros de cálculos que fizerem uso do alias TRP devem ser ajustados para uso da variável pública cTBLXMED (exemplificações abaixo).**Exemplificaremos a seguir o uso do ponto de entrada GPALTTRP com ajuste do alias.  
  
Abaixo demonstramos a customização no formato **antigo**, onde era referenciado o arquivo temporário de médias através do alias **TRP:**

User Function GPALTTRP()

Local aArea := GetArea()

If **TRP**->RP\_PD $ "210/220/300"   
nSalMedHr := (((SRA->RA\_SALARIO \* 0.80) / 14) / 7.33)  
ElseIf **TRP**->RP\_PD == "207"  
nSalMedHr := (((SRA->RA\_SALARIO \* 0.20) / 14) / 7.33)  
EndIf

RestArea(aArea)

Return()  
  
Agora, a **mesma customização** com a substituição do alias **TRP**pelo novo alias **cTBLXMED:**

User Function GPALTTRP()

Local aArea := GetArea()

If **(cTBLXMED)**->RP\_PD $ "210/220/300"   
nSalMedHr := (((SRA->RA\_SALARIO \* 0.80) / 14) / 7.33)  
ElseIf **(cTBLXMED)**->RP\_PD == "207"  
nSalMedHr := (((SRA->RA\_SALARIO \* 0.20) / 14) / 7.33)  
EndIf

RestArea(aArea)

Return()

As customizações em fórmulas, roteiros de cálculo ou Rdmakes que executam funções e utilizam informações de médias **devem ser ajustadas com o mesmo procedimento**, substituindo o alias **TRP** pelo novo alias **(cTBLXMED)**conforme exemplo citado.  
  
As adaptações nas customizações serão obrigatórias para clientes que estiverem atualizados com o release 12.1.25 em diante, no entanto, as mesmas já podem ser executadas em releases anteriores (12.1.17 / 12.1.23), planejamento esse que aconselhamos nossos clientes a seguirem desde já desde de que cumpram os pré-requisitos abaixo:

|  |  |
| --- | --- |
| Programa | Versão a partir de: |
| GFPXCALC.PRW | 08/03/2019 |
| GPEM030.PRX | 08/03/2019 |
| GPEM040.PRX | 08/03/2019 |
| GPEM060.PRX | 08/03/2019 |
| GPEM070.PRX | 08/03/2019 |
| GPEM630.PRX | 08/03/2019 |
| GPER080.PRX | 08/03/2019 |
| GPEXC131.PRX | 08/03/2019 |
| GPEXCADI.PRX | 08/03/2019 |
| GPEXCAL1.PRX | 08/03/2019 |
| GPEXCAL3.PRX | 08/03/2019 |
| GPEXFUN1.PRX | 08/03/2019 |
| GPEXLOC.PRX | 08/03/2019 |
| GPEXMED.PRX | 08/03/2019 |
| GPEXRESB.PRW | 08/03/2019 |

Obedecendo ao ciclo de vida dos releases Protheus, o último release no qual ainda será possível utilizar as customizações sem a revitalização será o 12.1.23, o qual tem ciclo de vida previsto para encerramento em Agosto/2020, ou seja, essa é a data máxima para que todas as customizações tenham sido revitalizadas para os clientes que estiverem utilizando o release 12.1.23.  
  
**Saiba Mais**  
[Adequação obrigatória das customizações que utilizam informações de médias](https://tdn.totvs.com/pages/releaseview.action?pageId=464961568)  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Pontos de entrada disponíveis na rotina de Médias - GPEXMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450454935-RH-Linha-Protheus-GPE-Pontos-de-entrada-dispon%C3%ADveis-na-rotina-de-M%C3%A9dias-GPEXMED)
