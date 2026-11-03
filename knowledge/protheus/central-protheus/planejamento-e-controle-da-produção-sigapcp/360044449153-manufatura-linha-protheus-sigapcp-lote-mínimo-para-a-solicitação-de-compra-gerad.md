---
article_id: 360044449153
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 45dadb25d69b44742a042cbd866ba12fab2fe3f6da04e9a5acc75af337606aae
fetched_at: '2026-06-28T22:42:43.539567+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Lote mínimo para a solicitação de compra
  gerada pelo MATA650 ou pelo MRP
type: support-article
updated_at: '2021-06-29T14:46:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044449153-Manufatura-Linha-Protheus-SIGAPCP-Lote-m%C3%ADnimo-para-a-solicita%C3%A7%C3%A3o-de-compra-gerada-pelo-MATA650-ou-pelo-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Por que quando a **SC - Solicitação de Compra** está sendo gerada automaticamente, pelo **MRP - Material Requiriments Planning** ou pelo **MATA650 - Ordens de Produção**, o Sistema não está considerando o **lote mínimo** cadastrado no produto?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre porque o **Lote Mínimo - B1\_LM**, cadastrado no **MATA010 - Cadastro de Produto**, é utilizado para produtos **fabricados**.  
Para produtos que são **comprados**, o Sistema seleciona a informação do campos **Quantidade de Embalagem - B1\_QE**.
