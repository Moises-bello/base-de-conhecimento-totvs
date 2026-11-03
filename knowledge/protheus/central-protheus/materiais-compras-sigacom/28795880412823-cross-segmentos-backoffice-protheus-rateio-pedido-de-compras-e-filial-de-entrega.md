---
article_id: 28795880412823
category: Materiais - Compras (SIGACOM)
content_hash: 39e392cbee9d74a1d82311625dc67a40a1abf2a132e01b7ea31d9aa6440644f2
fetched_at: '2026-06-28T22:41:11.880733+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Rateio Pedido de Compras e Filial de
  Entrega diferente da origem
type: support-article
updated_at: '2024-12-26T20:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28795880412823-Cross-Segmentos-Backoffice-Protheus-Rateio-Pedido-de-Compras-e-Filial-de-Entrega-diferente-da-origem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28795864568727) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao gerar um pedido de compras (MATA121) onde a filial de entrega é diferente da filial de origem e incluir um rateio deste pedido, o rateio não é trazido no preenchimento automático do documento de entrada através da rotina Ações Relacionadas>Pedido.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão COMPRAS - Versão 12

**Solução**

Ao incluir um pedido de compras por uma determinada filial os registros de banco de dados são associados a aquela filial, sendo que as tabelas de Pedido de Compras(SC7), condições de pagamento(SE4), TES(SF4) e Rateios (SCH), por padrão são todas Exclusivas.

Portanto ao incluir o documento de entrada, mesmo que usando um pedido de compras gerado pela filial 1 será necessário ratear novamente e preencher condição de pagamento e TES. Por serem exclusivos os cadastros podem estar divergentes e não estarem de acordo com a realidade estipulada pelo cliente.

***Obs:***

Esse tratamento é regra do sistema e não pode ser alterado devido a regra de negócios anteriormente estipulada.

***Saiba Mais:***

[Pedido de compras(MATA121) com rateio e filial de entrega diferente da filial de origem](https://tdn.totvs.com/display/PROT/PCOM04015+-+Pedido+de+compras%28MATA121%29+com+rateio+e+filial+de+entrega+diferente+da+filial+de+origem)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
