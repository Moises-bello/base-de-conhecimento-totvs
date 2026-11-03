---
article_id: 360016550212
category: RH - Folha de Pagamento
content_hash: 085c61f1c6a9a54fd764d9e1c95b94c2086f70c45b57acb8ce426fc607969301
fetched_at: '2026-06-28T22:44:12.218009+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular adicionais sobre médias
type: support-article
updated_at: '2024-09-17T19:24:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016550212-RH-Linha-Protheus-GPE-Como-calcular-adicionais-sobre-m%C3%A9dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26438960356119)** Tempo aproximado para leitura: **01:00:00 min**

**Dúvida:**Como calcular adicionais sobre médias (periculosidade e insalubridade)?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.25.  
  
**Solução**Quando o sindicato está está configurado para calcular os adicionais de Periculosidade e Insalubridade sobre Salário + Verbas, pode ser que uma determinada verba possua incidência para os adicionais e ao mesmo tempo esteja configurada para compor médias de Férias e 13º Salário.

Considerando essa situação, há possibilidade da empresa executar ou não o cálculo dos adicionais sobre as médias nas Férias, no 13º Salário, rescisão e também na provisão, pois a mesma verba utilizada para a média já foi utilizada para compor o valor do adicional.

Dessa forma, foi disponibilizado mnemônico **P\_ADISMED** para que seja possível definir se os adicionais de Periculosidade e Insalubridade deverão ser calculados também sobre as médias. 

| Mnemônico | Descrição | Valor Padrão |
| --- | --- | --- |
| **P\_ADISMED** | CALCULA ADICIONAIS SOBRE MEDIAS (.T. OU .F.) | .T. |

**IMPORTANTE:** Esse mnemônico somente é avaliado pelo sistema quando o cálculo dos Adicionais de Periculosidade e Insalubridade é sobre Salário + Verba.  
  
**Procedimento para Utilização**

1. No módulo Gestão de Pessoal (SIGAGPE), acesse **>Atualizações >Definições de Cálculos >Mnemônicos** **(GPEA300)**;

2. Pesquise pelo mnemônico **P\_ADISMED** e clique em **Alterar**;

3. Altere o conteúdo para **.T.** e clique em **Confirmar**:  
 **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8994046582167)**

4. As verbas que fazem base para as médias, além de estar com S para médias (aba Médias), devem estar com Sim para periculosidade e/ou insalubridade na aba **Incidências**, conforme exemplo abaixo.  
Caminho rotina Verbas **>Atualizações >Definições de cálculo >Verbas**

Verba de HE com sim para médias:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8994184088727)  
  
E com SIM para periculosidade e insalubridade:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8994185744151)

**Saiba Mais**

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)

[RH - Linha Protheus - GPE - Média de Periculosidade e Insalubridade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX1AGHyRc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBimh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI2MTU0MzIwOTA5MzM1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1NJUMzJUE5ZGlhLWRlLVBlcmljdWxvc2lkYWRlLWUtSW5zYWx1YnJpZGFkZQY7CFQ6DnNlYXJjaF9pZEkiKTFlNThkYzhjLTc1MzYtNDllMC1iZDE5LTllMmVlYTY4ZTA1MwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHWFkaWNpb25haXMgc29icmUgbcOpZGlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAt0C--2e5f35d7ade6d0fad6d4724c35363601d74a9056)

[RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgJm8zUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjQ2NDM5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQWx0ZXJhJUMzJUE3JUMzJUEzby1uby1jYWRhc3Ryby1kby1TaW5kaWNhdG8GOwhUOg5zZWFyY2hfaWRJIik4YjIzNzdmNy04MmRlLTQ3NmQtYjc4Ny04OWEwNWViN2I3YmIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdjYWRhc3RybyBzaW5kaWNhdG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2596a373717285e5623b5c9885811ca0e86a6935)
