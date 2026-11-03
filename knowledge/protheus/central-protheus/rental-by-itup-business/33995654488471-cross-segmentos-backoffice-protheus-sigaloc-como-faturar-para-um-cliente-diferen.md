---
article_id: 33995654488471
category: Rental by ItUp Business
content_hash: 58db962722c58f59f7d9986f6e61d4558487652b393ef49950c79c26376f86e4
fetched_at: '2026-06-28T22:36:20.549528+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como faturar para um cliente
  diferente do cliente de remessa
type: support-article
updated_at: '2025-08-06T19:38:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33995654488471-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-faturar-para-um-cliente-diferente-do-cliente-de-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33995677502359) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar remessa para um CNPJ (obra) e faturar para outro CNPJ (contratante) dentro do módulo SIGALOC?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Faça a inclusão do projeto e, nos campos **"CLIENTE" (FP0\_CLI)** e **"LOJA" (FP0\_LOJA)**, informe o cliente e a loja para os quais será enviada a remessa do equipamento;

2. Na aba **LOCALIDADE**, nos campos **"CLIENTE" (FP1\_CLIORI)** e **"LOJA" (FP1\_LOJORI)**, informe o cliente e a loja para os quais será enviada a remessa do equipamento;

3. Na aba **LOCAÇÃO**, onde são informados o produto, equipamento, data, etc., preencha os campos **"Cli. FAT (FPA\_CLIFAT)"** e **"LOJ. FAT." (FPA\_LOJFAT)** com o cliente e a loja para os quais o faturamento deve ser realizado.
