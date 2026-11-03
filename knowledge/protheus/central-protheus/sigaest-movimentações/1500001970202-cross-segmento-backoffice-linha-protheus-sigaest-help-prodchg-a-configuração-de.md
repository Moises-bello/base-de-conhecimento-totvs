---
article_id: 1500001970202
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 7f41163052efaf6ad322c637e0fefa27791d23343511653638477be5f252dc73
fetched_at: '2026-06-28T22:38:54.023674+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP PRODCHG - A configuração
  de lote do produto sofreu alteração apos este movimento.
type: support-article
updated_at: '2026-03-09T13:05:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001970202-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-PRODCHG-A-configura%C3%A7%C3%A3o-de-lote-do-produto-sofreu-altera%C3%A7%C3%A3o-apos-este-movimento
---

O erro HELP PRODCHG ocorre no Protheus Estoque ao tentar excluir um movimento de produto que passou a ter controle de rastreabilidade após a inclusão da nota. Para resolver, desative o controle de rastreabilidade (campo B1\_RASTRO), exclua a nota e depois retorne à configuração anterior, validando as tabelas SB2 e SB8.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38588422833943) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
Ao fazer estorno/exclusão de movimento ocorre o HELP PRODCHG.

![PRODCHG.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38588422835735)  
 **Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Causa**

O HELP "PRODCHG" é exibido quando um produto não tinha controle de rastreabilidade quando a movimentação de saldo foi incluída e agora no estorno/exclusão o produto possui este controle de rastreabilidade.

Dessa forma, o ***Protheus*** **não permite prosseguir pois causará desbalanceamento entre as tabelas SB2 x SB8**  
  
**Solução**  
Para que seja possível excluir, será necessário verificar quais produtos vinculados ao movimento estão com o controle de rastreabilidade ativo através do campo **B1\_RASTRO** e desabilitar. Em seguida, estorne/exclua a movimentação desejada.  
  
**Observação**: Validar as tabelas SB2 x SB8 do produto após realizar o processo, pois poderá gerar divergência nas tabelas devido à exclusão baixar o saldo somente da SB2.

### **O meu produto possui lotes distribuídos, após o movimento sem controle de lote:**

Se o movimento que você quer estornar, ou excluir, nasceu sem o controle de LOTE, mas o saldo já foi distribuído para os lotes pela "Manutenção de lotes MATA390", e o produto já possui movimentos com lote, a alternativa para esse caso é:

Fazer de modo exclusivo:

* Zerar os saldos do lote, atuais, disponíveis, empenhados etc, através de um inventario ou movimento interno de requisição por exemplo, certificando que o produto não tenha saldos nenhum, podendo avaliar via F4 no cadastro de produto, se todos os saldos estão ZERADOS.
* Após certificar disso, efetivar a desativação do controle de rastro do produto, no cadastro do produto, via B1\_RASTRO, e então, será possível "estornar ou excluir" o movimento que não tinha controle de rastreabilidade. (Caso dê help de saldo negativo na nova tentativa, será necessário ativar o parâmetro [**MV\_ESTNEG**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406452757399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-objetivo-do-par%C3%A2metro-MV-ESTNEG) para estornar essa movimentação, e após isso incluir um movimento devolvendo saldo para corrigir o saldo negativo e desativar o parâmetro. Dessa forma, o estorno do movimento sem lote será realizado sem algum tipo de help no saldo).
* Depois disso, acerte o saldo via movimento interno do produto AINDA SEM RASTRO, para que o saldo seja ZERO, caso ele tenha saldo negativo por causa do estorno ou exclusão do documento desejado.
* Por fim, ative o rastro do produto novamente, e realize um INVENTARIO de saldos, para criar o saldo corretamente para o produto e LOTE novamente.

Caso tenha ocorrido a **distribuição de saldos para o lote** e o objetivo seja estornar uma movimentação originada sem controle prévio de rastreabilidade, e não queira realizar o procedimento indicado acima, informamos que o sistema padrão não dispõe de rotinas nativas para essa operação.

Nessas circunstâncias, faz-se necessária a intervenção de um **analista especializado** ***in loco*** para a execução dos procedimentos cabíveis.

**Saiba mais:**

[*MP - SIGAEST - Como alterar o tipo de Controle de Rastreabilidade no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302187)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
