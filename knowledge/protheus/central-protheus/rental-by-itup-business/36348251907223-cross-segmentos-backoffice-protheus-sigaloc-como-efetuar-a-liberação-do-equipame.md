---
article_id: 36348251907223
category: Rental by ItUp Business
content_hash: 04138e09baff2189f5601837fbd5bd870488baef5043614b81d3558167364414
fetched_at: '2026-06-28T22:36:20.532215+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como efetuar a liberação
  do equipamento (BEM) para nova alocação
type: support-article
updated_at: '2025-11-14T21:19:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36348251907223-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-efetuar-a-libera%C3%A7%C3%A3o-do-equipamento-BEM-para-nova-aloca%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36348251865879) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como é feita a liberação do equipamento alocado para que possa ser utilizado em um novo contrato de locação?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - A partir da release P12.1.2410.  
  
**Solução**  
Para realizar a liberação do equipamento, siga os passos abaixo:

1. Acesse a rotina **Gerenciamento de Bens (LOCA224)** e localize o bem que deseja liberar.
2. Verifique se ele está com a legenda "**PRETA"** ou "**VERMELHA"**. Essas cores indicam que o retorno do equipamento já foi registrado. Caso não esteja com essas legendas, valide o processo de retorno na rotina **LOCA001**.
3. Estando com a legenda "**PRETA"** ou "**VERMELHA"**, selecione o equipamento e acesse **Outras Ações > Dev. Equipamento > Libera Equipamento**.
4. Após essa ação, a legenda do equipamento será alterada para "**VERDE"**, indicando que está disponível. Agora, basta acessar a rotina **Orçamento (LOCA001)** e, no campo **Equipamento (****FPA\_GRUA)**, o bem estará disponível para vinculação a um novo contrato.
