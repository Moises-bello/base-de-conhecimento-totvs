---
article_id: 360018945212
category: RH - Folha de Pagamento
content_hash: 7132711b2bd7561e0e51f349b8d2efca63cc52e22b5352e16240fe217720ccf5
fetched_at: '2026-06-28T22:44:12.204760+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular a diferença de férias
type: support-article
updated_at: '2026-06-25T13:43:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018945212-RH-Linha-Protheus-GPE-Como-calcular-a-diferen%C3%A7a-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18890840469655)**Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**  
Como calcular a diferença de férias na folha de pagamento  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Na versão 12 para calcular a diferença de férias é necessário que existam verbas vinculadas aos id's abaixo no campo **V. Dif. Fer.** na aba **Outras Informações,** aos respectivos id's de diferença conforme abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| Id para cálculo | Descrição | Vincular no campo **V. Dif. Fer. a** verba com Id | Descrição2 |
| 0065 | INSS Férias | - | - |
| 0072 | Férias | 0088 | Dif de Férias |
| 0073 | Férias Mês Seg. | 0089 | Dif. Férias Mês Seg. |
| 0074 | Abono | 0094 | Dif. Abono |
| 0075 | Média Férias Valor | 0838 | Dif. Médias Férias Valor |
| 0076 | Med. Férias Valor Mês Seg. | 0839 | Dif. Med. Férias Mês Seg. |
| 0077 | 1/3 de férias | 0090 | Dif 1/3 de Férias |
| 0078 | 1/3 Férias Mês Seg. | 0091 | Dif. 1/3 Férias Mês Seguinte |
| 0079 | 1/3 Abono Férias | 0095 | Dif. 1/3 sobre Abono Férias |
| 0082 | Média Férias Horas | 0096 | Dif. Médias Férias Horas |
| 0083 | Med. Férias Horas Mês Seg. | 0097 | Dif. Med. Férias Horas Mês Seg. |
| 0084 | Out. Adicionais Férias | 0098 | Dif. Out. Adicionais Férias |
| 0085 | Out. Adic. Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 0205 | Abono Mês Seg | 0207 | Dif. Abono Mês Seg. |
| 0206 | 1/3 Abono Mês Seg. | 0208 | Dif. 1/3 Abono Mês Seg. |
| 0232 | INSS Férias Mês Seg. | - | - |
| 0622 | Medias Horas Sobre Abono | 1416 | Dif. Média Horas Sobre Abono |
| 0623 | Médias Valor Sobre Abono | 1417 | Dif. Média valor Sobre Abono |
| 0632 | Adicionais Sobre Abono Pecuniário | 1450 | Dif. Adic. Sobre Abono Mês |
| 0633 | Média Horas sobre Abono Mês Seg. | 1418 | Dif. Média Horas Sobre Abono Mês Seg. |
| 0634 | Médias Valor Sobre Abono Mês Seg. | 1419 | Dif. Média Valor Sobre Abono Mês Seg. |
| 0635 | Adicionais Sobre Abono Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1296 | ATS Férias | 0098 | Dif. Out. Adicionais Férias |
| 1297 | ATS Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1298 | ATS sob. Verbas Férias | 0098 | Dif. Out. Adicionais Férias |
| 1299 | ATS sob. Verbas Abono Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1300 | Peric. Férias | 0098 | Dif. Out. Adicionais Férias |
| 1301 | Peric. Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1302 | Peric. Sob. Verbas Férias | 0098 | Dif. Out. Adicionais Férias |
| 1303 | Peric. Sob. Verbas Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1304 | Insalu. Férias | 0098 | Dif. Out. Adicionais Férias |
| 1305 | Insalu. Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1306 | Insalu. sob. Verbas Férias | 0098 | Dif. Out. Adicionais Férias |
| 1307 | Insalu. Sob. Verbas Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1308 | Adic. Confiança Férias | 0098 | Dif. Out. Adicionais Férias |
| 1309 | Adic. Confiança Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1310 | Adic. Transf. Férias | 0098 | Dif. Out. Adicionais Férias |
| 1311 | Adic. Transf. Férias Mês Seg. | 0099 | Dif. Outros Adic. Férias Mês Seg. |
| 1312 | ATS Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1313 | ATS Abono Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1314 | ATS sob. Verbas Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1315 | ATS Sob. Verbas Abono Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1316 | Peric. Abono Férias | 1450 | Dif. Adic. Sobre Abono Mês |
| 1317 | Peric. Abono Férias Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1318 | Peric. Sob. Verbas Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1319 | Peric. Sob. Verbas Abono Férias Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1320 | Insalu. Abono Férias | 1450 | Dif. Adic. Sobre Abono Mês |
| 1321 | Insalu. Abono Férias Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1322 | Insalu. Sob. Verbas Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1323 | Insalu. Sob. Abono Férias Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1324 | Adic. Confiança Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1325 | Adic. Confiança Anono Mês Seg | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1326 | Adic. Transf sob. Verbas Abono | 1450 | Dif. Adic. Sobre Abono Mês |
| 1327 | Adic. Transf. Sob. Verbas Abono Mês Seg. | 1451 | Dif. Adic. Sobre Abono Mês Seg. |
| 1407 | Média Abono Sobre Periculosidade | 1417 | Dif. Média Valor Sobre Abono |
| 1408 | Média Abono Sobre Insalubridade | 1417 | Dif. Média Valor Sobre Abono |
| 1409 | Média Abono Sobre Periculosidade Mês Seg. | 1419 | Dif. Média Valor Sobre Abono Mês Seg. |
| 1410 | Média Abono Sobre Insalubridade Mês Seg. | 1419 | Dif. Média Valor Sobre Abono Mês Seg. |

Exemplo:  
Verba com id **0072** - **Férias**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579038882199)  
  
Está com a verba de id **0088 - Diferença de Férias** vinculada à ela no campo **V. Dif. Fer.** na aba **Outras Informações.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579038884631)**  
  
  
Caso haja **reajuste salarial,** o sistema **sempre** irá apurar as diferenças de férias e das médias, tanto de horas quanto de valor. O sistema gera a diferença de média de valor nas verbas dos Ids abaixo:

**0838** - Diferença de Média de Valor no Mês  
**0839** - Diferença de Média de Valor Mês Seguinte  
**0840** - Diferença 1/3 sobre Média de Valor no Mês  
**0841** - Diferença 1/3 sobre Média de Valor Mês Seguinte  
  
Os Ids **0840** e **0841** somente serão utilizados quando **não** houver reajuste salarial. Caso haja reajuste salarial, a **diferença** de 1/3 sobre a média de valor será gerado **junto** as verbas de diferença de 1/3 de férias (Ids **0090** e **0091),** assim como ocorre com a diferença de 1/3 sobre a média de horas.

O sistema ainda permite apurar a diferença da média de valor ou de horas, mesmo se não houver reajuste salarial, para os funcionário que recebem salário, e também para os que só recebem médias, como os comissionistas puros. Para isso, deve-se configurar o mnemônico **P\_LDIFMED** com **.T.** (verdadeiro).

**Observação**

O mnemônico **P\_LDIFMED**configurado com**.T.**(verdadeiro) irá efetuar a carga das verbas incluídas no movimento para efetuar o recálculo de médias.

**Importante**

O mnemônico **P\_LDIFMED**configurado com**.F.**(falso) não fará com que o sistema não apure as diferença de médias em casos em que houver reajuste salarial, nesses casos, sempre haverá a apuração e geração das diferenças nos Ids abaixo:

* **0088** – Diferença de Férias
* **0089** – Diferença de Férias Mês Seguinte
* **0090** – Diferença de 1/3 Férias
* **0091** – Diferença de 1/3 Férias Mês Seguinte
* **0092** – Diferença de DSR sobre Férias
* **0093** – Diferença de DSR sobre Férias Mês Seguinte
* **0094** – Diferença Abono Pecuniário Férias
* **0095** – Diferença 1/3 Sobre Abono Férias
* **0096** – Diferença de Média de Horas Extras no mês
* **0097**– Diferença de Média de Horas Extras mês seguinte
* **0098** – Diferença Outros Adicionais
* **0099** – Diferença Outros Adicionais Mês Seguinte
* **1416** – Diferença de Média Horas sobre Abono
* **1417** – Diferença de Média Valor sobre Abono
* **1418** – Diferença de Média Horas sobre Abono Mês Seguinte
* **1419** – Diferença de Média Valor sobre Abono Mês Seguinte
* **1450** – Diferença Adicionais sobre Abono Mês
* **1451** – Diferença Adicionais sobre Abono Mês Seguinte
* **0207** – Diferença Abono Férias Mês Seguinte
* **0208** – Diferença 1/3 Sobre Abono Férias Mês Seguinte

**Observação**: Todas as verbas de férias e as verbas de Diferença de férias, devem estar com o campo **Ref. a Férias** (RV\_REFFER) preenchido com **Sim.** Do contrário, não será calculada a diferença de férias.

**Exemplo**

Cálculo de férias partidas e geração da diferença de férias na folha com o mnemônico P\_LDIFMED configurado com .F. (falso):

Ids envolvidos: 0088 – Diferença de Férias e 0089 – Diferença de Férias Mês Seguinte

Verba de diferença de férias mês seguinte (Id 0089) precisa ter o código da verba de diferença de férias (Id 0088) vinculado no campo RV\_CODMSEG:

![image-2024-6-28_13-29-23.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_13-29-23.png?version=1&modificationDate=1719592163230&api=v2)  
  
Férias de 13/05/2024 a 11/06/2024:

![image-2024-6-28_12-11-38.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_12-11-38.png?version=1&modificationDate=1719587498730&api=v2)

Após integração do roteiro FER, fazer alteração salarial:

![image-2024-6-28_12-12-20.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_12-12-20.png?version=1&modificationDate=1719587540997&api=v2)

Calcular a folha do mês 05/2024. Veja que gerou as verbas 145 (id 0088) e 146 (id 0089).

![image-2024-6-28_12-12-48.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_12-12-48.png?version=1&modificationDate=1719587568657&api=v2)  
  
Após fechamento do período 05/2024, veja que a verba 146 (id 0089) foi transformada em 145 (id 0088). Sem o id 0089 no período anterior, não geraria o 088 no mês atual.

![image-2024-6-28_12-13-17.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_12-13-17.png?version=1&modificationDate=1719587597877&api=v2)

![image-2024-6-28_12-14-45.png](https://tdn.totvs.com/download/attachments/384589397/image-2024-6-28_12-14-45.png?version=1&modificationDate=1719587685553&api=v2)  
  
**Todas** as verbas de **férias** devem estar com o campo **Ref. a Férias** (RV\_REFFER) preenchido com **Sim.** Do contrário, não será calculado diferença de férias.

**Saiba mais:**

[RH - Linha Protheus - GPE - Qual a teoria do pagamento da Diferença de férias na folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060307373-RH-Linha-Protheus-GPE-Qual-a-teoria-do-pagamento-da-Diferen%C3%A7a-de-f%C3%A9rias-na-folha?source=search)

[RH - Linha Protheus - GPE - Como parametrizar o mnemônico P\_LDIFINC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051265733-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-LDIFINC?source=search)

[RH - Linha Protheus - GPE - Recalculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420404618903-RH-Linha-Protheus-GPE-Recalculo-de-F%C3%A9rias-?source=search)

[RH - Linha Protheus - GPE - Como funciona o mnemônico P\_LMEDFERD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054270134-RH-Linha-Protheus-GPE-Como-funciona-o-mnem%C3%B4nico-P-LMEDFERD?source=search).

[RH - Protheus - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[P\_LDIFMED - Apuração da diferença das médias de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=384589397)
