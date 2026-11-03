---
article_id: 360020493192
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7642417e45b6eaf762f7a83ef4c88db7c3a7ecd60b7867c64fea93ef49e4574b
fetched_at: '2026-06-28T22:38:41.294254+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-DBH020- SetOrder - Index not found on D630DESCON em ambiente que não
  utiliza integração com módulo de Distribuição
type: support-article
updated_at: '2021-04-28T15:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020493192-MP-FAT-DBH020-SetOrder-Index-not-found-on-D630DESCON-em-ambiente-que-n%C3%A3o-utiliza-integra%C3%A7%C3%A3o-com-m%C3%B3dulo-de-Distribui%C3%A7%C3%A3o
---

**Ocorrência**

DBH020- SetOrder - Index not found on D630DESCON em ambiente que não utiliza integração com módulo de Distribuição.

**Ambiente**

Microsiga Protheus - a partir da versão 11.  
  
**Causa**

Ao gerar um pedido de venda (mata410) está gerando o erro:**DBH020: SetOrder - Index not found. on D630DESCON(DISXFUNA.PRW) ,** esse erro somente ocorre devido ao parâmetro **MV\_FATDIST**  estar habilitado.Quando o ambiente não possui a integração com o módulo de Distribuição, o conteúdo do parâmetro deve ser N.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Em configurador, ambiente, cadastros, parâmetros, localize o parâmetro **MV\_FATDIST** ;  
2. Deixe o parâmetro com o conteúdo como N e salve a configuração;  
3. Reinicie o smartclient e refaça o processo.
