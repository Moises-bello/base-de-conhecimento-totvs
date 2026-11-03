---
article_id: 16953507081879
category: Materiais - Compras (SIGACOM)
content_hash: 906d212251eedd5ba5af04daed3519c80aa70afddf4611fb203eef2be4b4f1d4
fetched_at: '2026-06-28T22:41:21.997516+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - O sistema não está
  puxando o peso do cadastro do produto no documento de entrada
type: support-article
updated_at: '2024-12-02T15:07:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16953507081879-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-O-sistema-n%C3%A3o-est%C3%A1-puxando-o-peso-do-cadastro-do-produto-no-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16953521896087) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao inserir no documento de entrada um produto que possui peso líquido e bruto em seu cadastro, o sistema não está puxando esses pesos na aba Informações DANFE.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Compras- a partir da 12.1.33  
  
**Causa**

Por padrão no documento de entrada a rotina não possui a funcionalidade de carregar a informação do peso que consta no cadastro do produto.

No processo de entrada de uma compra o peso de um produto pode variar de acordo com o produto, ou mesmo de acordo com o fornecedor, por este motivo a rotina não faz esse carregamento automático da informação do peso que consta no cadastro do produto.

![](https://totvssuporte.zendesk.com/attachments/token/ZuW0rfOYL13P1mUsZnwOQKiOk/?name=inline2074185833.png)​  
  
Esses campos são abertos como informação adicional da DANFE onde poderão ser digitados manualmente.

**Observação:**

O campo de peso não é preenchido na devolução de vendas.  
No processo de entrada de uma compra, o peso de um produto pode variar de acordo com o produto, ou mesmo de acordo com o fornecedor, por este motivo a rotina não faz esse carregamento automático.

Temos os  pontos de entrada estão disponíveis:  
MT103DNF : [Validação dos campos existentes no Folder "Informações Danfe" e "Nota Fiscal Eletrônica"](https://tdn.totvs.com/pages/releaseview.action?pageId=6085666)  
MT103DEV - [Alterar filtro para Notas Fiscais de saída](https://tdn.totvs.com/pages/releaseview.action?pageId=393366406)

A103VLQT - [Interrompe Validação de tabelas de entrada e saída](https://tdn.totvs.com/pages/releaseview.action?pageId=6085260)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
