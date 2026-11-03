---
article_id: 8248914155159
category: RH - Folha de Pagamento
content_hash: 3b897bb81cbb91f981c200454a4b75a79aeffc36136dac046ed25970bd6722fd
fetched_at: '2026-06-28T22:44:13.348339+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como considerar outras verbas além de comissão
  para o cálculo de médias na ausência de funcionário comissionado
type: support-article
updated_at: '2025-08-06T17:20:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8248914155159-RH-Linha-Protheus-GPE-Como-considerar-outras-verbas-al%C3%A9m-de-comiss%C3%A3o-para-o-c%C3%A1lculo-de-m%C3%A9dias-na-aus%C3%AAncia-de-funcion%C3%A1rio-comissionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17471821663639) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como considerar outras verbas além de comissão para o cálculo das médias na ausência de funcionário comissionado?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para calcular as médias de comissionado quando ele tem ausências parametrizadas para isso, o sistema no padrão considera os valores de comissão (ID 0165) e DSR comissão (ID 0166).

Para adicionar outras verbas ao cálculo das médias, informe no mnemônico **P\_PDMEDAFA** as verbas que também farão parte das médias, para isso, siga o passo a passo a seguir:  
  
1. Acesse a rotina pelo caminho **Atualizações >Definições de Cálculos >Mnemônicos**;  
  
2. Pesquise pelo mnemônico **P\_PDMEDAFA** e clique em Alterar:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26438955141015)  
  
3. No campo Conteúdo, informe as verbas conforme necessidade, elas devem ser informadas sem espaço, conforme exemplo abaixo, inseri as verbas 013 e 210:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26438955146391)

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Média de Periculosidade e Insalubridade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX1AGHyRc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBimh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI2MTU0MzIwOTA5MzM1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1NJUMzJUE5ZGlhLWRlLVBlcmljdWxvc2lkYWRlLWUtSW5zYWx1YnJpZGFkZQY7CFQ6DnNlYXJjaF9pZEkiKTFlNThkYzhjLTc1MzYtNDllMC1iZDE5LTllMmVlYTY4ZTA1MwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHWFkaWNpb25haXMgc29icmUgbcOpZGlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAt0C--2e5f35d7ade6d0fad6d4724c35363601d74a9056)

[RH - Linha Protheus - GPE - Como realizar admissão de comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420684082071-RH-Linha-Protheus-GPE-Como-realizar-admiss%C3%A3o-de-comissionado-puro?source=search)

[RH - Linha Protheus - GPE - Como parametrizar o cálculo de Horas Extras/RSR para Comissionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012420731-RH-Linha-Protheus-GPE-Como-parametrizar-o-c%C3%A1lculo-de-Horas-Extras-RSR-para-Comissionado?source=search)

[RH - Linha Protheus - GPE - Desconto de faltas e atrasos para comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041228333-RH-Linha-Protheus-GPE-Desconto-de-faltas-e-atrasos-para-comissionado-puro?source=search)
