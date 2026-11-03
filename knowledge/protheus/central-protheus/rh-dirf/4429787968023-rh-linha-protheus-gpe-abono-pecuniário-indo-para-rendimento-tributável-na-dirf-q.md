---
article_id: 4429787968023
category: RH – DIRF
content_hash: 8a3314508fe8a015e2187d5e4015f14ba7f0f6f3652b2a5cbad0c790de2ac778
fetched_at: '2026-06-28T22:44:06.738300+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Abono pecuniário indo para rendimento tributável
  na DIRF quando tem abono mês seguinte
type: support-article
updated_at: '2025-08-18T14:58:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4429787968023-RH-Linha-Protheus-GPE-Abono-pecuni%C3%A1rio-indo-para-rendimento-tribut%C3%A1vel-na-DIRF-quando-tem-abono-m%C3%AAs-seguinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34262876496663) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Valor do abono pecuniário sendo carregado para a coluna de rendimento tributável.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**  
Isso ocorre pois a verba de Abono Pago mês anterior esta sem incidência para a DIRF.  
  
**Solução**Na rotina Verbas, pelo caminho >Atualizações >Definições de Cálculo >Verbas, entre na verba de ID 1449, e na aba Anuais, no campo DIRF, deixe a incidência com 0 (zero), que é a incidência da DIRF para abono pecuniário:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429767529751)

Após ajuste, execute novamente a rotina Gerar Arquivo.

**IMPORTANTE**  
Além do ID 1449, os IDs abaixo também devem ter incidência 0 para a DIRF:

|  |  |
| --- | --- |
| 0074 | Abono Pecun. Férias |
| 0079 | Adic. 1/3 Sobre Abono Pecun. **(Somente se não tiver incidência para IR)** |
| 0094 | Dif Abono Pecun Férias |
| 0095 | Dif 1/3 sobre Abono Férias **(Somente se não tiver incidência para IR)** |
| 0205 | Abono Mês Seguinte |
| 0206 | 1/3 Abono Mês. Seg. **(Somente se não tiver incidência de IR)** |
| 0207 | Dif. Abono Mês. Seg. |
| 0208 | Dif. 1/3 Abono Mês. Seg. **(Somente se não tiver incidência de IR)** |
| 0622 | Média Horas sobre Abono |
| 0623 | Média Valor sobre Abono |
| 0632 | Adicionais sobre Abono Pecuniário |
| 0633 | Média Horas sobre Abono Mês seguinte |
| 0634 | Média valor sobre Abono Mês seguinte |
| 0635 | Adicionais sobre Abono Mês Seguinte |
| 1312 | ATS Abono Mês |
| 1313 | ATS Abono Mês Seg. |
| 1314 | ATS Abono Mês s/ Verbas |
| 1315 | ATS Abono Mês Seg. s/ Verbas |
| 1316 | Periculosidade Abono Mês |
| 1317 | Periculosidade Abono Mês Seg. |
| 1318 | Periculosidade Abono Mês s/ Verbas |
| 1319 | Periculosidade Abono Mês Seg. s/ Verbas |
| 1320 | Insalubridade Abono Mês |
| 1321 | Insalubridade Abono Mês Seg. |
| 1322 | Insalubridade Abono Mês s/ Verbas |
| 1323 | Insalubridade Abono Mês Seg. s/ Verbas |
| 1324 | Adic. Cargo Confiança Abono Mês |
| 1325 | Adic. Cargo Confiança Abono Mês Seg. |
| 1326 | Adic. Transferência Abono Mês |
| 1327 | Adic. Transferência Abono Mês Seg. |
| 1330 | DSR sobre Médias Abono |
| 1331 | DSR sobre Médias Abono Mês Seguinte |
| 1407 | Pagto Peric. Sobre Médias Abono |
| 1408 | Pagto Insalub. Sobre Médias Abono |
| 1409 | Pagto Peric. Sobre Médias Abono Mês Seguinte |
| 1410 | Pagto Insalub. Sobre Médias Abono Mês Seguinte |
| 1416 | Dif Média Horas sobre Abono |
| 1417 | Dif Média Valor sobre Abono |
| 1418 | Dif Média Horas sobre Abono Mês Seg. |
| 1419 | Dif Média valor sobre Abono Mês Seg. |
| 1449 | Abonos Pagos Mês Anterior |
| 1450 | Dif. Adic. sobre Abono Mês |
| 1451 | Dif. Adic. sobre Abono Mês Seg. |
| 1859 | Desconto abono antecipado (MP 1.046/2021) |
|  |  |

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)
