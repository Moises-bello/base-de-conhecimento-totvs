---
article_id: 360040965714
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d91d521185d66daa978490593b4997262742e4c97d4a02dbc5d1d461ad6aa2d8
fetched_at: '2026-06-28T22:38:42.349527+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Dividir/acumular
  os valores de FRETE/DESPESAS/SEGURO entre as parcelas do pedido de vendas
type: support-article
updated_at: '2022-08-26T12:58:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040965714-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Dividir-acumular-os-valores-de-FRETE-DESPESAS-SEGURO-entre-as-parcelas-do-pedido-de-vendas
---

**Dúvida**

Em pedidos de venda, quando informado valor de frete/despesas/seguro, é possível diluir esse valor entre as parcelas/duplicatas ou acumular o valor em uma parcela específica?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**Por padrão os valores de **frete/despesas/seguro** são **rateados** entre os itens e entre as parcelas seguindo a regra de rateio descrita na **documentação**: <https://tdn.totvs.com/pages/viewpage.action?pageId=239024024>Não há configuração padrão para acumular o valor do frete em uma parcela específica.

Sugerimos tratar por uma das formas abaixo:

1. Emissão de uma **fatura separada** referente ao valor de frete (pode-se cadastrar um produto com a descrição "frete" e utilizar um **TES** que **não atualiza estoque**);   
  
2. A utilização da **condição de pagamento** do **tipo 09**, onde pode **determinar manualmente** o valor das parcelas ([MP - FAT - Condição de Pagamento Tipo 9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176512-MP-FAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-9?source=search));  
  
3. Tratar de forma **customizada**, utilizando um dos **pontos de entrada** abaixo:  
**M460RTPD** - <http://tdn.totvs.com/display/public/PROT/M460RTPD>

**M460FIM** - Gravação da NF saída - <http://tdn.totvs.com/pages/releaseview.action?pageId=6784180>
