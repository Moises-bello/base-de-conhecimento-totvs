---
article_id: 35984922421399
category: eConsignado (Crédito do Trabalhador)
content_hash: e69b7eee77bb5b9b65689902b6b808838aa47dfe029148a492d5018c1adcbe90
fetched_at: '2026-06-28T22:43:07.075375+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: Linha Protheus - GPE - Desconto do eConsignado acima do limite de 35% na folha
  de pagamento
type: support-article
updated_at: '2025-10-30T13:01:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35984922421399-Linha-Protheus-GPE-Desconto-do-eConsignado-acima-do-limite-de-35-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35984862049687) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Desconto do eConsignado acima do limite de 35% na folha de pagamento  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Causa**  
Este problema acontece quando o mnemônico **P\_LIMECONS** está com conteúdo = **.F.** ou o mnemônico **P\_PERECONS** está com percentual **diferente de 35**.  
  
**Solução**  
Para que o Sistema considere **35% da Margem** do consignado, é necessário que o mnemônico **P\_LIMECONS** esteja = **.T.**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35984922393751)

E o mnemônico **P\_PERECONS** esteja = **35**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35984862051095)

Desta forma, o Sistema utilizará a seguinte **fórmula para cálculo**:  
Verbas de **provento da folha** com **sim para INSS** + verbas informadas no **P\_ADICONS** - **INSS** - **IR** - - verbas de **desconto da folha** com **sim para INSS** - verbas informadas no **P\_DEDCONS** nessa margem \* percentual informado no **P\_PERECONS** se o P\_LIMECONS = .T.  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Como consultar memória de calculo do Credito do trabalhador Econsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34163947469335-RH-Linha-Protheus-GPE-Como-consultar-mem%C3%B3ria-de-calculo-do-Credito-do-trabalhador-Econsignado)

[RH - Linha Protheus - GPE - Quais são os id's de cálculo relacionados ao Crédito do Trabalhador - eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35930969578519-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-id-s-de-c%C3%A1lculo-relacionados-ao-Cr%C3%A9dito-do-Trabalhador-eConsignado)

[RH - Linha Protheus - GPE - Mnemônicos eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33093447579799-RH-Linha-Protheus-GPE-Mnem%C3%B4nicos-eConsignado)

[Manual Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
