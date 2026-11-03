---
article_id: 4405550607127
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 377b8b709e111183b3ae5cc3bbc56e3e7fe4f2b13bfbfee49c79fea86cc3f938
fetched_at: '2026-06-28T22:38:57.220215+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - NNR_TIPO e SB2_TIPO
  funcionalidades na movimentação de Saldos
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405550607127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-NNR-TIPO-e-SB2-TIPO-funcionalidades-na-movimenta%C3%A7%C3%A3o-de-Saldos
---

**Dúvida**NNR\_TIPO e SB2\_TIPO qual o tratamento para utilização dos campos Padrão, Próprio ou Terceiros?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Ao criar o Armazém na rotina Locais de Estoque (AGRA045) deve avaliar como deseja utilizar o tipo de saldo que será movimentado nos Armazéns, criando os Armazéns com tipo diferente de "Padrão", os saldos somente serão movimentados para Armazéns do mesmo tipo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405572041111/mceclip0.png)   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405579752599/mceclip1.png)

Por exemplo:

**1 -** Para os Armazéns com o campo NNR\_TIPO igual Padrão somente é possível  movimentar o saldo desse Armazém para os Armazéns do mesmo tipo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405558439447/mceclip1.png)

**2 -** Para os Armazéns com o campo NNR\_TIPO igual Próprio somente é possível  movimentar o saldo desse Armazém para os Armazéns do mesmo tipo.

Utilizando a opção 2 (Próprio) quando queira que este armazém só tenha produtos próprio, ou seja, este saldo não irá se misturar com o saldo no Armazém do tipo Terceiros ou Padrão. Caso venha ter a necessidade de transferir um saldo do armazém do tipo 2 (Próprio), para qualquer outro tipo o sistema não irá permitir. o sistema entende que o saldo é próprio.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405551200791/mceclip2.png)

**3 -** Para os Armazéns com o campo NNR\_TIPO igual Terceiros somente é possível  movimentar o saldo desse Armazém para os Armazéns do mesmo tipo.

Esse tratamento é utilizado para que possa direcionar o saldo dos produtos conforme a necessidade específica em cada empresa.

Utilizando a opção 3 (Terceiros) quando queira que este armazém só tenha produtos de terceiro, ou seja, este saldo não irá se misturar com o saldo próprio ou padrão. Caso venha ter a necessidade de transferir um saldo do armazém do tipo 3 (Terceiros), para qualquer outro tipo o sistema não irá permitir. ele irá entender que o saldo é todo de terceiro.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405558477719/mceclip3.png)

Obs.: Ao tentar movimentar o saldo no cenário destacado acima é exibido o help BLOQLOC impedindo a transferência.

Veja também no link abaixo mais instruções sobre o help e como tratar caso tenha necessidade de alteração do tipo de Armazém dos Saldos.

[Help BLOQLOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020275791-MP-SIGAEST-HELP-BLOQLOC5-em-movimento-de-Transfer%C3%AAncia-entre-armaz%C3%A9ns-Causa-e-Corre%C3%A7%C3%A3o)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
