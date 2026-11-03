---
article_id: 360028868591
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8af2d20ec4010c41ad9bcbbdfe5311dac9be17e5adc117b6bfaa220a6217eadd
fetched_at: '2026-06-28T22:42:09.222331+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Advertência
  na transmissão de GNRE Maranhão - Erro apresentado: valor calculado difere do valor
  devido'
type: support-article
updated_at: '2022-08-17T19:43:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028868591-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Advert%C3%AAncia-na-transmiss%C3%A3o-de-GNRE-Maranh%C3%A3o-Erro-apresentado-valor-calculado-difere-do-valor-devido
---

**Dúvida**Como corrigir advertência na transmissão de GNRE para o Maranhão,  Erro apresentado valor calculado difere do Valor devido?  
   
 **Ambiente**Protheus - A partir Versão 12.1.17  
  
**Solução**Identificado que a advertência no valor é apresentada pelo fato que o Difal - Venda para não contribuinte ter sido calculado com alíquota interna de 17%, correto é calcular com alíquota interna de 18%

Para correção, alterar Parâmetro: MV\_ESTICM= MA18
