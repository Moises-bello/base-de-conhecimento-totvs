---
article_id: 40393703559959
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e8783a783d1ce00b29512e8a1d510ea552a815d2d9b724a019b2e99bb3190438
fetched_at: '2026-06-28T22:38:55.474354+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível movimentar
  produto fantasma(B1_FANTASM=S) no estoque?
type: support-article
updated_at: '2026-05-11T20:31:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40393703559959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-movimentar-produto-fantasma-B1-FANTASM-S-no-estoque
---

Não é possível movimentar produtos fantasma (B1\_FANTASM="S") nos movimentos internos (Tabela SD3) no TOTVS Protheus. O sistema permite entrada via nota fiscal, gerando saldo e possibilitando faturamento. Para baixar o saldo, é necessário fazer um inventário com quantidade zerada (MATA270) e depois o acerto de inventário (MATA340).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40393718146199) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
É possível movimentar produto Fantasma (B1\_FANTASM="S") no estoque?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Não possível movimentar produtos fantasma nos movimentos internos (Tabela SD3).

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40393703550871)

Atualmente o sistema permite dar entrada deste produto através de uma nota fiscal de entrada gerando saldo e com isso, permite faturar um pedido de venda de um produto fantasma (B1\_FANTASM="S").

**Como baixar o saldo em estoque de um produto fantasma no estoque?**

Para baixar o saldo de um produto fantasma é necessário fazer um inventário com quantidade zerada(MATA270) e depois o acerto de inventário(MATA340).

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[MATA410 - É possível movimentar produto Fantasma (B1\_FANTASM="S") no estoque?](https://tdn.totvs.com/pages/releaseview.action?pageId=691454452)
