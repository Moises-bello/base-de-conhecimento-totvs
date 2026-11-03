---
article_id: 32670450646807
category: Originação de Grãos (OG)
content_hash: 7fdf8a9a238c095d091c85872c0eae2ea2ddf85956d61c232a9e1ec3228546fe
fetched_at: '2026-06-28T22:45:40.933615+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Integrações entre Protheus x PIMS não foi efetuada.
  String or binary data would be truncated
type: support-article
updated_at: '2025-06-16T11:45:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32670450646807-Agro-Linha-Protheus-AGR-Integra%C3%A7%C3%B5es-entre-Protheus-x-PIMS-n%C3%A3o-foi-efetuada-String-or-binary-data-would-be-truncated
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32670450641047) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Na tela de **Romaneios com Pesagem**, ao tentar realizar uma integração da pesagem com o **TOTVS AGRO Multicultivo (PIMS)**, é apresentada a mensagem **Integrações entre Protheus x PIMS não foi efetuada. String or binary data would be truncated**?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32670439459095)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O Protheus quando integra a pesagem utiliza a integração de [Pesagem de Matéria Prima (WeighingRawMaterials)](https://tdn.totvs.com/pages/viewpage.action?pageId=376078758) onde o TOTVS Agro Multicultivo recebe as informações de pesagem e devolve ao Protheus com uma integração de  [Movimentação de Estoque (StockTurnover)](https://tdn.totvs.com/pages/viewpage.action?pageId=351020209) onde ele valida o centro de custo, conta, estabelecimentos e outras questões.  
Provavelmente nessa integração de movimentação de estoque esta ocorrendo algo que esta impossibilitando a integração.  
Dessa forma acesse o PIMS Connector e procure a mensagem de StockTurnover mais próxima da mensagem de WeighingRawMaterials no horário que realizou a tentativa de integração.  
Nessa mensagem esta disponível o que pode esta impedindo a integração.
