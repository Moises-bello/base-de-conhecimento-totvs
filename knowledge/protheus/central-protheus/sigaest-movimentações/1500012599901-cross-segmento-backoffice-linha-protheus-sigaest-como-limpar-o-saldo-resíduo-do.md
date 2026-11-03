---
article_id: 1500012599901
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c677f5345181c77d16c7a102c96c57e4533451e2c0dab5825add1fdf99ca79eb
fetched_at: '2026-06-28T22:38:55.377626+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como limpar o saldo
  (resíduo) do Armazém de CQ (MV_CQ)?
type: support-article
updated_at: '2024-05-14T17:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012599901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-limpar-o-saldo-res%C3%ADduo-do-Armaz%C3%A9m-de-CQ-MV-CQ
---

**Dúvida**

Como efetuar uma limpeza dos saldos de produtos que estão no armazém de CQ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Existem muitos motivos que fazem com que o usuário precise remover o saldo do armazém de C.Q, seja para devolver ao cliente/fornecedor, ou simplesmente pelo fato de querer eliminar aquele saldo do estoque. Dentro dessas situações, veja abaixo 3 (três) formas alternativas para remover o saldo do armazém de C.Q:

**Primeira forma: Rejeitar e fazer a Devolução da Compra**  
1° - Via MATA175, fazer a **rejeição**e então ficará com a legenda vermelha (Saldo Liberado/Rejeitado);  
2° - Via MATA410, fazer a devolução da compra (D2\_TIPO = D) chamando o produto, quantidade, armazém de C.Q (delegado no MV\_CQ) e nota de origem (C6\_NFORI).

**Segunda forma: Liberar e fazer a Devolução da Compra**  
1° - Via MATA175, fazer a **liberação** do CQ e então ficará com a legenda vermelha e mandará o saldo ao armazém padrão (B1\_LOCPAD);  
2° - Via MATA410, fazer a devolução de compra chamando o produto, o armazém padrão e a nota de origem.

**Terceira forma: Liberar e fazer a saída do estoque por meio de Inventário:**

1° - Via MATA175, fazer a **liberação** do CQ e então ficará com a legenda vermelha e mandará o saldo ao armazém padrão (B1\_LOCPAD);

2° - Após efetuada a Baixa para o **Armazém padrão**, via MATA270/MATA340, efetuar, respectivamente, a digitação da quantidade contada e posteriormente o acerto de inventário atualizando o Saldo (***Obs.***: O inventário ***requisitando Saldo não é permitido no Armazém de CQ*** somente em Armazém Padrão).

**Quarta forma: Estornar todas as movimentações originais que geraram o Saldo no CQ:**

- Ao efetuar uma movimentação que inclui saldo no Armazém de CQ é gerado um registro de Baixa do CQ (tabela SD7) que aguarda a inspeção para envio ao Armazém padrão, também é possível estornar  as movimentações originais (MATA241, MATA340, MATA261, etc.) onde retira o registro origem da Baixa do CQ. ***Observações***: Nesse caso, somente é possível quando efetuado dentro do período que esteja aberto.

Veja também o vídeo abaixo sobre as instruções padrões de utilização da rotina Baixas do CQ (MATA175)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

[*SIGAEST - Rotina MATA175 - Instruções padrões sobre Controle de Qualidade no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)
