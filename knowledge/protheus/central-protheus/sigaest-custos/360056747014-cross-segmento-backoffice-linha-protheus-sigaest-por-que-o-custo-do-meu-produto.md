---
article_id: 360056747014
category: SIGAEST - CUSTOS
content_hash: 80dbe4a7eb1108b733271fb8e6eb14a4e66ae17927d082eff9b3dd307a8e3bff
fetched_at: '2026-06-28T22:39:02.309306+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Por que o Custo do
  meu Produto ficou zerado?
type: support-article
updated_at: '2025-03-12T12:23:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056747014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Por-que-o-Custo-do-meu-Produto-ficou-zerado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504094994839)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Ao verificar o relatório do meu produto, identifiquei que o custo/custo médio ficou zero. Por quê?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Solução**

Existem vários motivos que fazem o custo do produto ficar zerado. Veja os cenários abaixo e como corrigir em cada situação:

**1° -  Ao fazer qualquer Movimentação Interna (ex: Requisição, Transferência entre Armazéns, Inventário ou outro tipo que gere dados na SD3), o custo/custo médio traz zerado devido ao parâmetro** **MV\_CUSZERO**

Este caso é muito comum, pois este parâmetro habilitado zera o custo unitário quando a Quantidade ou Custo do Movimento for igual à zero, como a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098605473)

**Como corrigir?**

-Verifique se o parâmetro MV\_CUSZERO está preenchido com conteúdo "S". Se estiver, coloque como "N" e execute o Recálculo do Custo Médio:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009020461)

Após isso, veja que o Kardex abaixo trouxe o custo total e médio do movimento, o que alimentou nossa coluna "Valor Total" com R$ 1.200,00.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098605873)

**2**. **A primeira movimentação Interna (SD3) ou de Saida (SD2) está com custo/custo médio zerado.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096324774)

- Isso ocorre porque no saldos iniciais (SB9) não possui custo, então a primeira movimentação não terá. Uma sugestão é utilizar o parâmetro MV\_SEQ300 habilitado para que tente reordenar as movimentações.

**3. Ao fazer um movimento, traz quantidade, porém Custo Total/Custo Médio zerados**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098820393)

- Verifique se o campo [F4\_BONIF](https://tdn.totvs.com/pages/releaseview.action?pageId=6087404) está como "S". Pois, se estiver, o custo do item será zerado, caracterizando uma entrada por bonificação. Caso faça o ajuste no TES e queira ajustar o custo, execute a [Rotina MATA190 (Refaz Custo de Entrada);](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-MP-SIGAEST-Custo-de-entrada-MATA190-)

- Valide se o campo F4\_ESTOQUE está realmente configurado como "SIM" nos TES do movimento.

**4 .O Kardex apresenta somente o Custo Total, porém não possui Custo Médio:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098820553)

Nesse caso, como não possui quantidade de movimentação (quantidade 0), o custo médio não será preenchido.

Pois para preencher o custo médio segue a seguinte formula:

CUSTO/QUANTIDADE = CM.

Como a quantidade é zero, logo o Custo Médio será zero.

**Observação:**

Um outro cenário onde pode-se ter custo zerado é quando o produto está no C.Q e foi utilizado em movimentações. O custo começa a partir do Saldo Inicial (quando delegado algum valor de custo) ou, quando vai para o C.Q, após sua liberação. Para que a partir dela o Protheus, no Recálculo do Custo Médio, tenha um ponto de partida dos custos dos movimentos.

**Saiba mais:**

*[MP - SIGAEST - Como zerar custo de movimento no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023788792)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
