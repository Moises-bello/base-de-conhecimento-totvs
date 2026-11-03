---
article_id: 360017518652
category: Originação de Grãos (OG)
content_hash: a259deb2209113e197348a7b3b1e18fbb1aedea2aa23ca5d89c1774cb5211fc7
fetched_at: '2026-06-28T22:45:38.880942+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Conversão de unidades de medidas no agronegócio
type: support-article
updated_at: '2025-06-24T19:19:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017518652-Agro-Linha-Protheus-AGR-Convers%C3%A3o-de-unidades-de-medidas-no-agroneg%C3%B3cio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20298458809239)**Tempo aproximado para leitura: **00:01:10min  
Dúvida**Como usar e configurar o Sistema de medidas no **Agronegócio**?   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Há apenas um cadastro de conversão, o **AGRA060 - Tabela de Conversão de Unidade de Medida**, que não diferencia **conversão de quantidade** ou **preço**, por isso necessita respeitar uma regra.  
A regra é cadastrar no **AGRA060** sempre considerando a conversão de **quantidade para quantidade**.  
No desenvolvimento de funções para **converter quantidades** é necessário usar o fator **DE -> PARA** que está cadastrado no **AGRA060**. No desenvolvimento de funções para **converter preços unitários** é necessário usar o fator **PARA -> DE** que está cadastrado no **AGRA060**.  
  
Exemplo de cadastro correto:

| AGRA060 | U.M. DE | U.M. PARA | FATOR | OPERADOR |
| --- | --- | --- | --- | --- |
|  | KG | TL | 1.000,0000000 | Dividir |
|  | TL | KG | 1.000,0000000 | Multiplicar |
|  | S60 | KG | 60,0000000 | Multiplicar |
|  | KG | S60 | 60,0000000 | Dividir |
|  | TL | S60 | 0,0600000 | Dividir |
|  | S6 | TL | 0,0600000 | Multiplicar |
|  | BU | KG | 27,2155750 | Multiplicar |
|  | KG | BU | 27,2155750 | Dividir |
|  | BU | S60 | 2,2046000 | Dividir |
|  | S60 | BU | 2,2046000 | Multiplicar |

![Agron.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7752002232599)
