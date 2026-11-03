---
article_id: 360035872374
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c109f72bf9f34890867ff2ecf0ec26903d48571f3b056705ce79817106510c44
fetched_at: '2026-06-28T22:38:38.713793+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Help A440QTDL no
  faturamento
type: support-article
updated_at: '2023-01-19T20:02:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035872374-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-A440QTDL-no-faturamento
---

**Ocorrência**

Help **A440QTDL** apareceu, como corrigir?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) – A partir da release 11.80.

**Causa**

A quantidade a liberar é maior que a quantidade solicitada no pedido ou o saldo a liberar. 

C6\_QTDLIB > C6\_QTDVEN

**Soluções**

* 1 - Colocar quantidade no campo "Qtd. Liberada [C6\_QTDLIB]" menor que o do campo "Quantidade [C6\_QTDVEN]".
* 2 - Na validação do pedido de venda, é verificado a quantidade que está sendo liberado, subtraindo a quantidade que já foi liberada, permitindo sequência da operação somente se houver saldo.  
    
  O campo **C6\_QTDLIB**armazena a Quantidade Liberada do Item do Pedido de Venda (Para estar apto à faturar, estando as demais liberações válidas).  
    
  Para o campo "[**C6\_QTDLIB]** **Qtd.Liberada**", há um parâmetro que pode ser definido na própria rotina de Pedidos de Venda **(****MATA410)**através da tecla **F12**de seu teclado. Ao acessar a rotina e teclar "**F12"**, a primeira pergunta é "**Sugere Qtde Liber. ?**" Respondendo como **"Sim"** o sistema já preencherá tal campo com a quantidade registrada no Item do Pedido de Venda, caracterizando sua Liberação.  
    
  Se consultar a tabela **SC9** o campo **C9\_QTDLIB** estará preenchido com o mesmo valor da liberação do pedido de vendas (C6\_QTDLIB).  
    
  **Fluxograma usual genérico:** SC5/SC6 -> SC9 -> SF2/SD2 -> SE1
