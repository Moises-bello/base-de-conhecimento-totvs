---
article_id: 360022655971
category: NFe - Nota Fiscal Eletrônica
content_hash: b799a7a967d6d8b9e6a2426b0a83fd9607d8c7b9b8ca364c4eb05dae3d063872
fetched_at: '2026-06-28T22:40:00.325865+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar o
  peso líquido e peso bruto na DANFE'
type: support-article
updated_at: '2025-12-18T17:39:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022655971--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-o-peso-l%C3%ADquido-e-peso-bruto-na-DANFE
---

**Dúvida**

Como gerar o peso liquido e peso bruto no DANFE.

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para que esas informações saiam no DANFE, deve-se na hora de criar o pedido preencher os campos Peso Líquido, Peso Bruto, Volume e espécie.  
  
No caso de Nota de Entrada, na inclusão do documento, vá na aba INFORMAÇÕES DANFE. Os campos são Peso Líquido, Peso Bruto, Espécie 1 e Volume 1, e assim sucessivamente.  
  
Para levar o Peso Líquido, Peso Bruto, Espécie e Volume no danfe é necessário que seja preenchido os campos:  
  
Peso Liquido - C5\_PESOL  
Peso Bruto - C5\_PBRUTO   
Volume 1- C5\_VOLUME1   
Espécie 1 - C5\_ESPECI1  
  
Estes campos acima da tabela SC5 gravam nas tabelas:  
  
(SF2 – nota de saída) nos campos F2\_PLIQUI, F2\_PBRUTO, F2\_VOLUME1, F2\_ESPECIE1 ou  
(SF1 – notas de entrada) nos campos F1\_PLIQUI, F1\_PBRUTO, F1\_VOLUME1, F1\_ESPECIE1
