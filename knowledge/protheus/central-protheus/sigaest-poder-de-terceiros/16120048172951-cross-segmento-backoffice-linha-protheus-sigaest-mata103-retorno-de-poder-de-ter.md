---
article_id: 16120048172951
category: SIGAEST - PODER DE TERCEIROS
content_hash: 04f8d2b342dc07ea14b1423384ffe5f055e18d4e21643bf3833eff0387f4d797
fetched_at: '2026-06-28T22:39:03.207766+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - Retorno
  de Poder de Terceiros com valor de origem divergente
type: support-article
updated_at: '2023-08-14T14:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16120048172951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Retorno-de-Poder-de-Terceiros-com-valor-de-origem-divergente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16120062113303) Tempo aproximado para leitura: **00:03:12 min****Ocorrência**Retorno de Poder de Terceiros (via MATA103) puxando valor divergente da origem.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

No cenário em que os campos de quantidade e valor estão com as casas decimais aumentadas, no processo de inclusão de **Pedido de Venda para Devolução de Poder de Terceiros**, a tela para seleção de **Documentos de Origem**está carregando valores indevidos nos campos **Preço Unitário**e **Valor Liquido** e está impedindo a confirmação de inclusão do pedido de venda.

**Solução**

Foi efetuado ajuste no processo de **Pedido de Venda para Devolução de Poder de Terceiros**para que cada linha apresentada na tela **Documentos de Origem** sejam carregados os valores correspondentes  aos documentos de origem.

Para este problema ser resolvido, é necessário que o fonte COMXFUN seja atualizado no ambiente. Ele foi expedido com data 21/06 para correção. Porém, o mesmo já está mais atualizado na Expedição Contínua do Módulo de Compras. Abaixo link para atualização da Expedição conforme releases vigentes:

Expedição Continua Compras

2210:

<https://suporte.totvs.com/portal/p/10098/download#detail/1080335>

12.1.33:

<https://suporte.totvs.com/portal/p/10098/download#detail/1039089>

OBS: Sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

Após isso, basta validar novamente e o problema será solucionado.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
