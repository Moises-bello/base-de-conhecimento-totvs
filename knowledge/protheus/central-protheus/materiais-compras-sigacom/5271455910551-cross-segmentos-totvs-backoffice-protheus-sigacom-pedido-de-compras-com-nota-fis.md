---
article_id: 5271455910551
category: Materiais - Compras (SIGACOM)
content_hash: 696ddc9c971fef55766778dcd9ac2324135919666ed433f3dd82babcb52f13c3
fetched_at: '2026-06-28T22:41:22.082810+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pedido de Compras
  com Nota fiscal de Entrada gera o Help : Total'
type: support-article
updated_at: '2022-04-06T15:29:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5271455910551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pedido-de-Compras-com-Nota-fiscal-de-Entrada-gera-o-Help-Total
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao incluir Pedido de Compras com Nota fiscal e alterar o valor do pedido gera o Help : Total

![total.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5270405693847/total.png)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Sigacom - Todas as Versões  
  
**Solução**

Se alterar o valor do pedido de compras, não será recalcuado o valor total da nota fiscal,  um dos principais motivos é a questão de arredondamento, o MATA103 permite ate 0,49 de diferença  
porque o valor impresso não pode ser modificado, dessa forma o usuário informa o valor manualmente.

É possível criar gatilho para o campo D1\_TOTAL para ser carregado automaticamente quando informado a quantidade e o valor no Documento de Entrada, não é indicado alterar as tabelas do ambiente padrão, contudo caso necessário criar gatilho para carregar o campo D1\_TOTAL constam no artigo**:**

**[MP - SIGACOM - Exemplo de gatilho tabela SD1 para carregar campo D1\_TOTAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022537891-MP-SIGACOM-Exemplo-de-gatilho-tabela-SD1-para-carregar-campo-D1-TOTAL?source=search)**

**![20220406_111354.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5271169287703/20220406_111354.gif)**

**Saiba mais em:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
