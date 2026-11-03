---
article_id: 360020275791
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 00ac59d8cc98bb92f882172e8b43909d8cc09ec7fdac6dc7d933b8e17f3d098c
fetched_at: '2026-06-28T22:38:54.019137+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP BLOQLOC5 em movimento
  de Transferência entre armazéns - Causa e Correção
type: support-article
updated_at: '2026-02-20T16:48:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020275791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-BLOQLOC5-em-movimento-de-Transfer%C3%AAncia-entre-armaz%C3%A9ns-Causa-e-Corre%C3%A7%C3%A3o
---

O erro HELP BLOQLOC5 ocorre ao tentar transferir saldos entre armazéns de tipos diferentes no Protheus. Para evitar, ajuste o campo "Tipo de Armazém" para o mesmo tipo nos dois armazéns. Caso precise transferir entre tipos diferentes, siga processos específicos conforme o tipo de armazém, como notas fiscais ou baixa de qualidade.

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30249191876887)*** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Ao tentar efetuar transferência entre Armazéns pela rotina [***TRANSFERÊNCIAS MÚLTIPLAS (MATA261)***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002547841-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-fazer-Transfer%C3%AAncia-de-Saldo-entre-Armaz%C3%A9ns-) apresenta o ***HELP BLOQLOC5***. O que é este HELP e o que fazer para resolver?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016048371)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O ***HELP BLOQLOC5*** é apresentado devido um dos armazéns envolvidos na transferência ser do tipo diferente do outro (isso pode ser diagnosticado no campo NNR\_TIPO, na tabela NNR).

Para não apresentar este HELP (e caso realmente não utilize armazéns de tipos diferentes) basta acessar à rotina de Saldos em Estoque (MATA225), selecionar o Produto nos armazéns Origem e Destino e deixar o campo **"Tipo de Armazém" (B2\_TIPO)** para o mesmo tipo em ambos os armazéns.

**E como eu transfiro o saldos entre os armazens com tipos diferentes?**

Cada armazem tem o seu tipo, e cada tipo tem um processo especifio para liberação dos movimentos, depende do tipo voce pode movimentar somente com notas fiscais/baixa de qualidade/processos de produções etc, ou então para o mesmo tipo entre os armazens.

**Observações importantes**:

- Caso tenha saldo nos armazéns, ***não será possível*** **alterar o tipo de armazém**. É preciso consumir todo o saldo do armazém para em seguida realizar a alteração do tipo de mesmo.

- [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405550607127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-NNR-TIPO-e-SB2-TIPO-funcionalidades-na-movimenta%C3%A7%C3%A3o-de-Saldos?source=search) e leia sobre o tratamento padrão para o campo ***NNR\_TIPO e SB2\_TIPO*** envolvidos nesse cenário.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - NNR\_TIPO e SB2\_TIPO funcionalidades na movimentação de Saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405550607127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-NNR-TIPO-e-SB2-TIPO-funcionalidades-na-movimenta%C3%A7%C3%A3o-de-Saldos?source=search)
