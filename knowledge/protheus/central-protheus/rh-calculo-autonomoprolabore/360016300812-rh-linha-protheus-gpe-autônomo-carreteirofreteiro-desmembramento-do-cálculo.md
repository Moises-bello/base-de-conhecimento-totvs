---
article_id: 360016300812
category: RH - Calculo Autonomo/Prolabore
content_hash: 92d8b340d014dc48fdf37f1f288310de48f9ee4055c6f1b263de030e3595e2b1
fetched_at: '2026-06-28T22:43:15.097867+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Autônomo Carreteiro/Freteiro - Desmembramento do
  Cálculo
type: support-article
updated_at: '2025-08-08T11:35:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016300812-RH-Linha-Protheus-GPE-Aut%C3%B4nomo-Carreteiro-Freteiro-Desmembramento-do-C%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24831352966423) Tempo aproximado para leitura: **00:02: min**

**Ocorrência**No módulo **Gestão de Pessoal**, para **autônomo carreteiro/freteiro**, ocorre a redução tanto da base de INSS quanto da base de IRRF. Apesar do cálculo da folha estar correto, a maneira que as rubricas são geradas no evento S-1200 não está de acordo com o que o eSocial determina.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Na página de perguntas e respostas do eSocial, o governo respondeu que para autônomo carreteiro/freteiro deverá haver um desmembramento de rubricas:  
  
![tdn.JPG](http://tdn.totvs.com/download/attachments/394222582/tdn.JPG?version=2&modificationDate=1535548149000&api=v2)  
Observe que o valor do frete foi de R$ 10.000,00, mas houve o desmembramento desse valor nas rubricas X, XX e XXX. A primeira rubrica apenas tem incidência pra INSS, a segunda rubrica apenas tem incidência pra IRRF e a terceira rubrica não possui incidência.  
  
**Solução**

Para seguir a determinação do governo, foi efetuado a criação de três Ids de cálculo:

**1563 -****Valor do Frete - Incidência INSS,** que irá conter a parte do frete que possui incidência para INSS;

**1564 -****Valor do Frete - Incidência IRRF**, que irá conter a parte do frete que possui incidência para IRRF;

**1565 -****Valor do Frete - Sem Incidência**, que irá conter a parte do frete que não possui incidência.

As verbas deverão ser cadastradas com a configuração abaixo:

| **ID** | **Descrição** | **RV\_TIPOCOD** | **RV\_INSS** | **RV\_IR** | **RV\_FGTS** | **IncCP** | **IncIRRF** | **IncFGTS** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1563 | Frete - Incidência INSS | 1 (Provento) | S | N | N | 11 | 00 | 00 |
| 1564 | Frete - Incidência IRRF | 1 (Provento) | N | S | N | 00 | 11 | 00 |
| 1565 | Frete - Sem Incidência | 1 (Provento) | N | N | N | 00 | 00 | 00 |

Por exemplo, segue abaixo como ficaria o cálculo de folha do autônomo:

O valor do frete de R$ 10.000,00 foi gerado na verba 218:

| **ID** | **Verba** | **Valor** | **RV\_INSS** | **RV\_IR** |
| --- | --- | --- | --- | --- |
| 0218 | 218 | R$ 10.000,00 | S | S |

Ao efetuar o cálculo da folha, o valor da verba 218 será desmembrado nas verbas cadastradas para os três novos Ids e a verba 218 não será gerada no cálculo:

| **Id de Cálculo** | **Verba** | **Descrição** | **Valor** |
| --- | --- | --- | --- |
| 1563 | 263 | Frete - Incidência INSS | R$ 2.000,00 |
| 1564 | 264 | Frete - Incidência IRRF | R$ 1.000,00 |
| 1565 | 265 | Frete - Sem Incidência | R$ 7.000,00 |
| 0064 | 417 | Desconto INSS | R$ 220,00 |
| 0437 | 464 | Desconto SEST | R$ 30,00 |
| 1456 | 465 | Desconto SENAT | R$ 20,00 |

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097450173)  
 **Saiba Mais**Para mais informações sobre a separação do desconto do SEST e SENAT, consultar a documentação disponível em

<http://tdn.totvs.com/pages/releaseview.action?pageId=364924146>

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
